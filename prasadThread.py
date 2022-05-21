import threading
from threading import *
from time import sleep



class prasadThread(Thread):
         def run(Self):
             for i in range(4):
              print('this is 1st thread',threading.current_thread().name)
              sleep(5)





class saiThread(Thread):
           def run(Self):
            for i in range(4):
               print("this is 2nd thread",threading.current_thread().name)
               sleep(5) 



A=prasadThread()
B=saiThread()
A.start()
print(A.is_alive())
sleep(2) 
B.start()
print(B.is_alive())
A.join(2)
B.join(2)
 