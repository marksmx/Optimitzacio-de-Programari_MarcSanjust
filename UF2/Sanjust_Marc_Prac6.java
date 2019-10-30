import datetime
import time
from multiprocessing import Process

def t(s):
    while (True):
        print datetime.datetime.now().time()
        time.sleep(s)

def main():
    p = Process(target=t,args=(1,))
    p.start()
    for i in range(10):
        time.sleep(0.5)
        print (p.pid)
    p.terminate()
    print("Fi")


if __name__ == "__main__":
    main()
