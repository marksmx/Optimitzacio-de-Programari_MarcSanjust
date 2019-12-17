from datetime import datetime
from multiprocessing import Pool

def primers(num):
    for i in range(2, num/2):
        if num % i == 0:
            return False
        else:
            pass
    return True

if __name__ == '__main__':
#El Pool ens servira per indicar quants processos volem executar a la vegada.
    pool = Pool(processes=2)
    l = range(40000000, 40000100)
#Aquesta linia inicia el contador per poder saber quan tarda.
    start = datetime.now()
    it = pool.imap(primers, l)
    i = 0
    m = 40000000

#El valor I defineix quants numeros volem mostrar

    while(i<100):
        print str(m), str(it.next())
        m+=1
        i+=1
#Aquesta ultima linia es la que mostrara el temps que ha tardat
    print datetime.now() - start

#TEMPS DE PROCESSOS
# 3 processos - 0:00:52.142956
# 5 processos - 0:00:57.524602
# 10 processos - 0:00:58.565069
