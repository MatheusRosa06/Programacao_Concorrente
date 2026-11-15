# Programacao_Concorrente
Integrantes: Gabriel Igeski Donato, Matheus Gomes da Rosa, Rafael Luis Naslowski da Silva

## Linguagem Escolhida: Python

### Link Youtube:

# parte 1 Jantar dos Filósofos

## Contextualização:

5 filósofos estão numa mesa circular, onde entre cada dupla de filósofos há um garfo e na frente de cada um tem um prato. Para que seja possível comer, o filósofo tem que pegar os dois garfos mais próximos. O problema se encontra em que não tem como todos comerem ao mesmo tempo, pois é necessário compartilhar os garfos, os filósofos precisam ficar se alternando entre diferentes estados: pensando, com fome, comendo.Então, o desafio é de sincronismo para que seja possível que todos consigam alternar seus estados de uma forma que todos possam comer.

## Print do Console
### filosofos-1
<img width="318" height="430" alt="image" src="https://github.com/user-attachments/assets/ddea1459-1444-45b6-a243-5d59b835c492" />

### filosofos-2
<img width="422" height="560" alt="image" src="https://github.com/user-attachments/assets/393daa22-c3b0-4dcf-8bfc-2a35feca8d0d" />


### Explicação COFFMAN:
Ocorrem as 4 condições para Deadlock em filosofos-1.

Exclusão Mútua -> Quando filósofo 1 pega o garfo entre ele e o filósofo 2, o filósofo 2 não consegue pegar esse mesmo garfo, pois está na mão do filosofo 1, o filósofo 2 só tem acesso ao garfo quando o filósofo 1 o liberar.

Posse e Espera -> Todos os 5 filósofos pegam garfo que está à sua esquerda e ficam presos aguardando o garfo da direita

Não Preempção -> Os filósofos não soltam os garfos que pegaram até conseguir executar ação de comer

Espera Circular -> O primeiro filósofo espera liberar o garfo que está com o segundo filósofo, o segundo filósofo espera liberar o garfo que esta com o terceiro filósofo, e assim consecutivamente até o quinto filósofo que espera o primeiro filósofo liberar o garfo.

na versão filosofo-2, os problemas são corrigidos, pois se implementa o recurso que quando filósofo tenta pegar um segundo garfo que está ocupado, ele solta o primeiro garfo e tenta novamente mais tarde, assim os filósofos não ficam presos segurando um garfo aguardando infinitamente o segundo garfo ficar livre.

### Fluxograma
<img width="607" height="643" alt="diagrama dos filósofos drawio" src="https://github.com/user-attachments/assets/ca4c666a-079c-41ec-a116-4bef6db0417d" />

# Parte 2 Threads e semáforos
### resultados com semaforo
<img width="207" height="70" alt="image" src="https://github.com/user-attachments/assets/762632b4-dee6-4e08-9a31-7b59ab3a718f" />
<img width="192" height="73" alt="image" src="https://github.com/user-attachments/assets/9aa0155a-9baa-483c-bfac-56c589b12160" />
<img width="197" height="70" alt="image" src="https://github.com/user-attachments/assets/18a63b02-b701-43d9-ac6e-61008ab4e5e5" />

### resultados sem semaforo
<img width="187" height="63" alt="image" src="https://github.com/user-attachments/assets/07d682e0-0fac-4e0e-b3ac-8bb445140917" />
<img width="193" height="70" alt="image" src="https://github.com/user-attachments/assets/a43eac86-6fdf-4726-a2f5-0e7c0c482e82" />
<img width="200" height="67" alt="image" src="https://github.com/user-attachments/assets/945e1e04-4b4a-4f24-a75c-32778bd90482" />


Eu notei que a versão sem sincronização não estava nunca apresentando perda de incrementos nos testes, tendo sempre o mesmo valor que o esperado. Isso pode ter acontecido por causa do GIL do CPython, que limita a execução simultânea das threads e reduz a chance de ocorrer uma condição de corrida nesse caso, por isso as imagens de teste acabam mostrando o mesmo número que o esperado.
Mesmo assim, essa versão não é totalmente segura, pois não há garantia de que o resultado será sempre correto. 
Já a versão que tem o semáforo garante que apenas uma thread por vez acesse o contador, que muitas threads sejam executadas ao mesmo tempo.
O unico ponto ruim do semaforo, e que por ele executar apenas uma thread por vezes, a execução final acaba ficando mais lenta, já que as threads precisam esperar sua vez, em compensação, ele garante que as alterações feitas por uma thread sejam corretamente vistas pelas demais, mantendo a consistência dos dados.


# Parte 3 DeadLock

## Contextualização:

Em sistemas concorrentes, o gerenciamento inadequado de recursos compartilhados pode levar a falhas críticas de sincronização. O código analisado simula um cenário de DeadLock em Python. O problema ocorre porque duas threads (T1 e T2) competem por dois recursos exclusivos (LOCK_A e LOCK_B) em ordens invertidas, gerando um bloqueio mútuo permanente o DeadLock.

Como utilizar os códigos: Ao carregar o projeto em sua IDE que consiga utilizar Python 3.10+, abra os arquivos e rode com o botão RUN no arquivo selecionado, ou aperte o play no boão ao lado do código onde está localizado o MAIN (parte final dos arquivos).

## Print do Console
### DeadLock
<img width="1320" height="247" alt="image" src="https://github.com/user-attachments/assets/5c660311-4bd2-4bf9-a65e-baf5ec6baf07" />

### Corrigido
<img width="533" height="387" alt="image" src="https://github.com/user-attachments/assets/c54301f1-e146-4b35-a309-15f0e8ed1dcb" />

### Explicação COFFMAN:

No primeiro ocorre as 4 condições para o DeadLock:

Exclusão Mútua -> Quando T1 pega Lock A, T2 não consegue acessar Lock A, até a T1 liberar.

Posse e Espera -> T1 possui Lock A, e espera pelo Lock B, que por sua vez está na T2, que espera o Lock A que está na T1.

Não Preempção -> O Python não força a liberação de recursos que estão nas Threads, só porque uma outra thread precisa do mesmo recurso.

Espera Circular -> T1 espera por recurso em T2, e a T2 espera por recurso em T1.

Já na versão corrigida a condição quebrada foi a espera circular, com a ordem global de Lock A depois Lock B, as Threds precisam esperar até que o Lock A esteja disponivel, para depois avançarem para o Lock B. Evitando que as duas threads tenham um Lock em cada, causando uma espera infinita, por não conseguirem acessar o recurso que está alocado em outra Thread.

