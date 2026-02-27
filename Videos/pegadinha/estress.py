import time
import threading

def burn_cpu():
    while True:
        pass  

threads = []
num_threads = 16 

for _ in range(num_threads):
    t = threading.Thread(target=burn_cpu)
    t.daemon = True
    t.start()
    threads.append(t)

time.sleep(10)