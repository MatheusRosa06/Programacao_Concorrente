import threading
import time

T = 8
M = 200000
count = 0

sem = threading.Semaphore(1)

def tarefa():
    global count

    for i in range(M):
        sem.acquire()

        try:
            count = count + 1
        finally:
            sem.release()

inicio = time.time()

threads = []

for i in range(T):
    t = threading.Thread(target=tarefa)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

fim = time.time()
tempo = round(fim - inicio, 4)

print("Esperado:", T * M)
print("Obtido:", count)
print("Tempo:", tempo, "segundos")