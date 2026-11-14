import threading
import time

# REcursos a serem utilizados.
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def log(msg):
    # print para time, thread, recurso
    print(f"[{time.strftime('%H:%M:%S')}] [{threading.current_thread().name}] {msg}", flush=True)


# Roda uma para cada T, sempre buscando A primeiro, evitando deadlock
def worker(nome_final):
    log("tentando adquirir LOCK_A...")
    LOCK_A.acquire()
    log("adquiriu LOCK_A")

    time.sleep(0.05)

    log("tentando adquirir LOCK_B...")
    LOCK_B.acquire()
    log("adquiriu LOCK_B")

    log(f"{nome_final} concluiu")

    LOCK_B.release()
    LOCK_A.release()
    log("liberou LOCK_B e LOCK_A")


if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("T1",), name="Thread 1")
    t2 = threading.Thread(target=worker, args=("T2",), name="Thread 2")

    t1.start()
    t2.start()

# Assim que terminarem dispara a mensagem
    t1.join()
    t2.join()

    print("\n>>> As duas threads terminaram. Sem deadlock. <<<")