import threading
import time

def f():
    print('Thread function\n')
    return

def f3(i):
    for p in range(3):
        time.sleep(i+1)
        print('Thread #',i,"\n")
        time.sleep(i)
    return

class Custom(threading.Thread):
    def f2(self):
        print('Custom thread function')

    def run(self):
        self.f2()    

#for i in range(3):
    t1 = threading.Thread(target=f3,args=(1,))
    t2 = threading.Thread(target=f3,args=(2,))
    t3 = threading.Thread(target=f3,args=(3,))

    t1.start()
    t2.start()
    t3.start()