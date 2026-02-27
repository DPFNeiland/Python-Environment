import time
import os
import csv
import math
import psutil
import numpy as np
import multiprocessing
import platform
import threading
from tkinter import *


# ======================
# CONFIGURAÇÕES GERAIS
# ======================
RUNS = 3
WARMUP_TIME = 2
CPU_TEST_TIME = 4
MEM_SIZE_MB = 800
DISK_SIZE_MB = 500

WEIGHTS = {
    "cpu": 0.40,
    "memory": 0.25,
    "disk": 0.20,
    "gpu": 0.15
}

BASELINES = {
    "cpu": 250,
    "memory": 4000,
    "disk": 500,
    "gpu": 100
}


# ======================
# WARM-UP
# ======================
def warmup():
    start = time.time()
    while time.time() - start < WARMUP_TIME:
        np.dot(np.random.rand(300, 300), np.random.rand(300, 300))


# ======================
# CPU MULTI-THREAD
# ======================
def cpu_worker(results, idx):
    start = time.time()
    ops = 0
    while time.time() - start < CPU_TEST_TIME:
        np.dot(np.random.rand(500, 500), np.random.rand(500, 500))
        ops += 1
    results[idx] = ops


def cpu_test():
    manager = multiprocessing.Manager()
    results = manager.dict()
    threads = []

    for i in range(psutil.cpu_count(logical=True)):
        p = multiprocessing.Process(target=cpu_worker, args=(results, i))
        p.start()
        threads.append(p)

    for t in threads:
        t.join()

    total_ops = sum(results.values())
    return total_ops / CPU_TEST_TIME


# ======================
# MEMÓRIA
# ======================
def memory_test():
    size = MEM_SIZE_MB * 1024 * 1024 // 8
    start = time.time()
    arr = np.ones(size, dtype=np.float64)
    arr *= 2
    duration = time.time() - start
    return MEM_SIZE_MB / duration


# ======================
# DISCO
# ======================
def disk_test():
    filename = "disk_test.tmp"
    data = os.urandom(DISK_SIZE_MB * 1024 * 1024)

    start = time.time()
    with open(filename, "wb") as f:
        f.write(data)
    write_time = time.time() - start

    start = time.time()
    with open(filename, "rb") as f:
        f.read()
    read_time = time.time() - start

    os.remove(filename)
    return DISK_SIZE_MB / ((write_time + read_time) / 2)


# ======================
# NORMALIZAÇÃO
# ======================
def normalize(value, baseline):
    return (value / baseline) * 100


def stats(values):
    mean = sum(values) / len(values)
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
    return mean, std


# ======================
# BENCHMARK PRINCIPAL
# ======================
def run_benchmark():
    warmup()

    cpu_scores = []
    mem_scores = []
    disk_scores = []

    for _ in range(RUNS):
        cpu_scores.append(cpu_test())
        mem_scores.append(memory_test())
        disk_scores.append(disk_test())

    cpu_avg, cpu_std = stats(cpu_scores)
    mem_avg, mem_std = stats(mem_scores)
    disk_avg, disk_std = stats(disk_scores)

    cpu_norm = normalize(cpu_avg, BASELINES["cpu"])
    mem_norm = normalize(mem_avg, BASELINES["memory"])
    disk_norm = normalize(disk_avg, BASELINES["disk"])

    final_score = (
        cpu_norm * WEIGHTS["cpu"] +
        mem_norm * WEIGHTS["memory"] +
        disk_norm * WEIGHTS["disk"]
    )

    save_csv(cpu_avg, cpu_std, mem_avg, mem_std, disk_avg, disk_std, final_score)

    return cpu_avg, mem_avg, disk_avg, final_score


# ======================
# CSV
# ======================
def save_csv(cpu, cpu_std, mem, mem_std, disk, disk_std, final):
    exists = os.path.exists("results.csv")
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow([
                "CPU Model", "Cores", "Threads", "RAM(GB)",
                "CPU Score", "CPU Std",
                "Memory Score", "Memory Std",
                "Disk Score", "Disk Std",
                "Final Score"
            ])

        writer.writerow([
            platform.processor(),
            psutil.cpu_count(logical=False),
            psutil.cpu_count(logical=True),
            round(psutil.virtual_memory().total / (1024 ** 3), 2),
            round(cpu, 2), round(cpu_std, 2),
            round(mem, 2), round(mem_std, 2),
            round(disk, 2), round(disk_std, 2),
            round(final, 2)
        ])


# ======================
# GUI
# ======================
def start_gui():
    def run():
        status.set("Rodando benchmark... isso pode demorar")
        cpu, mem, disk, final = run_benchmark()
        status.set(
            f"CPU: {cpu:.2f}\nMemória: {mem:.2f}\nDisco: {disk:.2f}\n\n"
            f"SCORE FINAL: {final:.2f}"
        )

    root = Tk()
    root.title("Benchmark Python Profissional")
    root.geometry("500x350")

    Label(root, text="Benchmark de Desempenho", font=("Arial", 16)).pack(pady=10)

    Button(root, text="Iniciar Benchmark", command=lambda: threading.Thread(target=run).start()).pack(pady=10)

    global status
    status = StringVar()
    Label(root, textvariable=status, justify=LEFT).pack(pady=10)

    Label(root, text="Resultados salvos em results.csv").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    start_gui()