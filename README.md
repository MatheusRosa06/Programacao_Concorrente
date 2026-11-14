# Programacao_Concorrente
Integrantes: Gabriel Igeski Donato

## Linguagem Escolhida: Python

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

