from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(2)
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(2)

obj1= Hello()
obj2 = Hi()

obj1.start()
sleep(0.5)
obj2.start()




