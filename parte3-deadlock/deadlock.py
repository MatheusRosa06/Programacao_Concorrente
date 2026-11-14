import threading
import time

# REcursos a serem utilizados.
LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def log(msg):
    #print para time, thread, recurso
    print(f"[{time.strftime('%H:%M:%S')}] [{threading.current_thread().name}] {msg}", flush=True)


def thread1():
    log("tentando adquirir LOCK_A...")
    LOCK_A.acquire()
    log("adquiriu LOCK_A")

    time.sleep(0.05)

    log("tentando adquirir LOCK_B... (vai esperar)")
    LOCK_B.acquire()  # não vai conseguir adquirir pois está com a T2
    log("adquiriu LOCK_B")

    log("T1 concluiu")

    LOCK_B.release()
    LOCK_A.release()


def thread2():
    log("tentando adquirir LOCK_B...")
    LOCK_B.acquire() # adquire B antes da A para realizar o DeadLock
    log("adquiriu LOCK_B")

    time.sleep(0.05)

    log("tentando adquirir LOCK_A... (vai esperar)")
    LOCK_A.acquire()  # fica bloqueada aqui LOCK_A está com a T1
    log("adquiriu LOCK_A")

    log("T2 concluiu")

    LOCK_A.release()
    LOCK_B.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=thread1, name="Thread 1", daemon=True)
    t2 = threading.Thread(target=thread2, name="Thread 2", daemon=True)

    t1.start()
    t2.start()

    # Tempo de espera/contagem para as threads, afim de identigicar se as T ainda estão rodando
    # e sinalizar o DeadLock
    t1.join(timeout=3)
    t2.join(timeout=3)

    if t1.is_alive() and t2.is_alive():
        print("\n>>> DEADLOCK DETECTADO: as duas threads estão bloqueadas. <<<")
        print(">>> Nem 'T1 concluiu' nem 'T2 concluiu' foram impressos.")
    else:
        print("\nExecução terminou sem deadlock.") # Nunca vai rodar, ou chance extremamente baixa
