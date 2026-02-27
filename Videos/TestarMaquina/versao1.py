import os
import time
import csv
import math
import psutil
import numpy as np
import multiprocessing
import platform
import threading
import warnings
import subprocess
from tkinter import *
from tkinter import ttk

warnings.filterwarnings("ignore", category=RuntimeWarning)

# ======================
# CAMINHOS
# ======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "results.csv")

# ======================
# CONFIG
# ======================
RUNS = 3
WARMUP_TIME = 2
CPU_TEST_TIME = 4
MEM_SIZE_MB = 800
DISK_SIZE_MB = 500

WEIGHTS = {"cpu": 0.4, "memory": 0.25, "disk": 0.2}
BASELINES = {"cpu": 250, "memory": 4000, "disk": 500}


# ======================
# TESTES
# ======================
def warmup():
    start = time.time()
    while time.time() - start < WARMUP_TIME:
        np.dot(np.random.rand(300, 300), np.random.rand(300, 300))


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
    processes = []

    for i in range(psutil.cpu_count(logical=True)):
        p = multiprocessing.Process(target=cpu_worker, args=(results, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    return sum(results.values()) / CPU_TEST_TIME


def memory_test():
    size = MEM_SIZE_MB * 1024 * 1024 // 8
    start = time.time()
    arr = np.ones(size, dtype=np.float64)
    arr *= 2
    duration = time.time() - start
    return MEM_SIZE_MB / duration


def disk_test():
    filename = os.path.join(BASE_DIR, "disk_test.tmp")
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
# UTIL
# ======================
def stats(values):
    mean = sum(values) / len(values)
    std = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
    return mean, std


def normalize(value, baseline):
    return (value / baseline) * 100


def classify(score):
    if score > 130:
        return "🟢 Máquina Forte"
    elif score > 90:
        return "🟡 Máquina Boa"
    elif score > 60:
        return "🟠 Máquina Mediana"
    else:
        return "🔴 Máquina Atrasada"


def save_csv(cpu, mem, disk, final):
    exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not exists:
            writer.writerow([
                "CPU", "Cores", "Threads", "RAM(GB)",
                "CPU Score", "Memory Score", "Disk Score",
                "Final Score"
            ])

        writer.writerow([
            platform.processor(),
            psutil.cpu_count(logical=False),
            psutil.cpu_count(logical=True),
            round(psutil.virtual_memory().total / (1024 ** 3), 2),
            round(cpu, 2),
            round(mem, 2),
            round(disk, 2),
            round(final, 2)
        ])


# ======================
# BENCHMARK
# ======================
def run_benchmark(progress, result_label):
    progress.start()

    warmup()

    cpu_scores, mem_scores, disk_scores = [], [], []

    for _ in range(RUNS):
        cpu_scores.append(cpu_test())
        mem_scores.append(memory_test())
        disk_scores.append(disk_test())

    cpu_avg, _ = stats(cpu_scores)
    mem_avg, _ = stats(mem_scores)
    disk_avg, _ = stats(disk_scores)

    cpu_norm = normalize(cpu_avg, BASELINES["cpu"])
    mem_norm = normalize(mem_avg, BASELINES["memory"])
    disk_norm = normalize(disk_avg, BASELINES["disk"])

    final_score = (
        cpu_norm * WEIGHTS["cpu"] +
        mem_norm * WEIGHTS["memory"] +
        disk_norm * WEIGHTS["disk"]
    )

    save_csv(cpu_avg, mem_avg, disk_avg, final_score)

    progress.stop()

    result_label.config(
        text=f"""
CPU Score: {cpu_avg:.2f}
Memory Score: {mem_avg:.2f}
Disk Score: {disk_avg:.2f}

FINAL SCORE: {final_score:.2f}
{classify(final_score)}
"""
    )


# ======================
# GUI MODERNA
# ======================
def start_gui():
    root = Tk()
    root.title("Python Benchmark Pro")
    root.geometry("600x500")
    root.configure(bg="#1e1e1e")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TProgressbar", thickness=20)

    Label(
        root,
        text="PYTHON BENCHMARK PRO",
        font=("Segoe UI", 18, "bold"),
        fg="white",
        bg="#1e1e1e"
    ).pack(pady=15)

    info_text = f"""
CPU: {platform.processor()}
Cores: {psutil.cpu_count(logical=False)} | Threads: {psutil.cpu_count(logical=True)}
RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB
Sistema: {platform.system()} {platform.release()}
"""

    Label(
        root,
        text=info_text,
        fg="#bbbbbb",
        bg="#1e1e1e",
        font=("Segoe UI", 10),
        justify=LEFT
    ).pack(pady=10)

    progress = ttk.Progressbar(root, mode="indeterminate", length=400)
    progress.pack(pady=20)

    result_label = Label(
        root,
        text="Clique em INICIAR para rodar o benchmark",
        fg="white",
        bg="#1e1e1e",
        font=("Segoe UI", 11),
        justify=LEFT
    )
    result_label.pack(pady=15)

    Button(
        root,
        text="🚀 INICIAR BENCHMARK",
        font=("Segoe UI", 12, "bold"),
        bg="#007acc",
        fg="white",
        relief="flat",
        command=lambda: threading.Thread(
            target=run_benchmark,
            args=(progress, result_label)
        ).start()
    ).pack(pady=10)

    Button(
        root,
        text="📂 Abrir Pasta dos Resultados",
        font=("Segoe UI", 10),
        bg="#333333",
        fg="white",
        relief="flat",
        command=lambda: subprocess.Popen(f'explorer "{BASE_DIR}"')
    ).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    start_gui()