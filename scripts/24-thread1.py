from threading import *
import time as t
def f(nome, atraso):
	for i in range(4):
		t.sleep(atraso) #para a thread por 1 segundo
		#imprime o tempo atual
		print(nome + ":" + t.ctime(t.time()) + "\n", end = "")
#inicia uma nova thread que executa a funcao 'f' com parametros "Thread 1"
t1 = Thread(target=f, args=("Thread 1", 1))
t2 = Thread(target=f, args=("Thread 2", 2))
t1.start()
t2.start()
t1.join() #aguarda as threads terminarem de executar
t2.join()
