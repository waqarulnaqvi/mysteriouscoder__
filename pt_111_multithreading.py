import threading
import os
from threading import Thread

def double(x):
    return x*2

double_ag=lambda x:x*2

cube=lambda x:x**3

avg=lambda x,y=3: (x+y)/2


def app(fx,value):
    return value +fx(value)


print(app(cube,6))
print(app(lambda x:x**2,6))

def two():
    import pt_37_import_usuage
    Thread(target=pt_37_import_usuage).start()
 # 7 10