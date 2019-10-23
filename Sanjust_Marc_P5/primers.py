import sys

""" 
Programa que mostra els X primers numeros primaris 
"""

class llista_primers:
    """
    >>> llista_primers(2).llista
    [2, 3]
    """
    """    
    La variable "llista" tindra tants numeros com entrem per terminal
    """

    def __init__(self, n):
        self.n = n
        self.llista = []
        self.busca()

    """    
    Si la llargada d'aquesta es 0, mostra el 2 i s'acaba
    """    

    def busca(self):
      
        if (len(self.llista) == 0):
            self.llista.append(2)
            self.busca()

            """   
            Si es mes llarga que 0, anira afegint a llista els X primers numeros, fins arribar al 2
            """

        elif (len(self.llista) < self.n):
            trobat = False
            seguent = self.llista[-1]+1
            while not trobat:
                for i in self.llista:
                    if seguent%i == 0:
                        seguent += 1
                        trobat = False
                        break
                    else:
                        trobat = True
            self.llista.append(seguent)
            self.busca()

"""
El valor que donem, per defecte sera un String. En el main es passa a int, i d'aquesta manera, el codi el pot utilitzar.
"""

if __name__ == '__main__': 
    #import doctest
    l = llista_primers(int(sys.argv[1]))
    print l.llista
    #doctest.testmod()
