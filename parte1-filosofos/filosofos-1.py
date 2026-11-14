# versão (i) - sem deadlock
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

    # filósofo está com fome
    estados[filosofo_id] = "com fome"
    print(f"Filósofo {filosofo_id + 1} está com fome")
    # pegar garfo esquerdo
    pegar_garfo(filosofo_id)  
    time.sleep(1)   
    # pegar garfo direito
    pegar_garfo(filosofo_id) 

    # filósofo está comendo
    estados[filosofo_id] = "comendo"
    print(f"Filósofo {filosofo_id + 1} está comendo")
    time.sleep(1)

    soltar_garfo(filosofo_id )
    soltar_garfo(filosofo_id )


def pegar_garfo(filosofo_id):
  # determinando garfo esquerdo
  if garfos_em_mao[filosofo_id] == 0:
    garfo_id = filosofo_id  
  # determinando garfo direito
  else:
    garfo_id = (filosofo_id + 1) % N  

  print(f"Filósofo {filosofo_id + 1} tenta pegar o garfo {garfo_id + 1}")
  garfos[garfo_id].acquire()  
  garfos_em_mao[filosofo_id] += 1
  print(
      f"Filósofo {filosofo_id + 1} pegou o garfo {garfo_id + 1} (na mão:"
      f" {garfos_em_mao[filosofo_id]})"
  )


def soltar_garfo(filosofo_id):
  # identificando garfo direito para soltar
  if garfos_em_mao[filosofo_id] == 2:
    garfo_id = (filosofo_id + 1) % N  
   # identificando garfo esquerdo para soltar
  else:
    garfo_id = filosofo_id  

  garfos[garfo_id].release()
  garfos_em_mao[filosofo_id] -= 1


for i in range(N):
  threading.Thread(target=exist, args=(i,)).start()