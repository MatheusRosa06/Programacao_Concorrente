# Versão (ii): sem deadlock 
import random
import threading
import time

# Dados básicos
N = 5
garfos = [threading.Lock() for _ in range(N)]
garfos_em_mao = [0, 0, 0, 0, 0]
estados = ["pensando", "pensando", "pensando", "pensando", "pensando"]




def exist(filosofo_id):
  while True:
    # filósofo está pensando
    estados[filosofo_id] = "pensando"
    print(f"Filósofo {filosofo_id + 1} está pensando")
    time.sleep(0.5)

    # filósofo está com fome e tenta pegar os dois garfos juntos
    estados[filosofo_id] = "com fome"
    print(f"Filósofo {filosofo_id + 1} está com fome")
    pegar_garfos(filosofo_id)

    # filósofo está comendo
    estados[filosofo_id] = "comendo"
    print(f"Filósofo {filosofo_id + 1} está comendo")
      
    time.sleep(1)

    # liberando os garfos após comer
    soltar_garfos(filosofo_id)

# tentando pegar os garfos na mão
def pegar_garfos(filosofo_id):
  esquerdo = filosofo_id
  direito = (filosofo_id + 1) % N

  print(
      f"Filósofo {filosofo_id + 1} tenta pegar os garfos {esquerdo + 1} e"
      f" {direito + 1}"
  )

  # tentativa de pegar os dois garfos juntos
  while True:
    garfos[esquerdo].acquire()
    if garfos[direito].acquire(blocking=False):
      break
    # caso falhe
    garfos[esquerdo].release()
    time.sleep(0.5 * random.uniform(0.01, 0.1))
    # caso consiga 
  garfos_em_mao[filosofo_id] = 2
  print(
      f"Filósofo {filosofo_id + 1} pegou os garfos {esquerdo + 1} e"
      f" {direito + 1} (na mão: {garfos_em_mao[filosofo_id]})"
  )

# soltando os garfos da mõo 
def soltar_garfos(filosofo_id):
  esquerdo = filosofo_id
  direito = (filosofo_id + 1) % N

  garfos[esquerdo].release()
  garfos[direito].release()
  garfos_em_mao[filosofo_id] = 0
  print(
      f"Filósofo {filosofo_id + 1} soltou os garfos {esquerdo + 1} e"
      f" {direito + 1}"
  )


for i in range(N):
  threading.Thread(target=exist, args=(i,)).start()