from threading import *
import time as t

class MinhaThread(Thread):
    def __init__(self, nome, atraso):
        Thread.__init__(self) #chamando o construtor da super-classe
        self.nome = nome
        self.atraso = atraso
    def run(self):
        for i in range(4):
            t.sleep(self.atraso)
            print(self.nome, ":", t.ctime(t.time()), "\n", end = "")
            
t1 = MinhaThread("Thread 1", 1)
t1.start()
t1.join()
