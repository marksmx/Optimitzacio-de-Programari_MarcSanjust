class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        self.a,self.b,self.c,self.d,self.e = self.eq.split(" ")
        self.A,self.B = self.a.split("x")

        try:
            self.A = float(self.A)
        except:
            print("Nomes poden ser Numeros")

        try:
            self.c = float(self.c)
        except:
            print("Nomes poden ser Numeros")

        try:
            self.e = float(self.e)
        except:
            print("Nomes poden ser Numeros")

        if self.b == "+":
            self.a = float(self.e) - float(self.c)
            self.B = float(self.a) / float(self.A)
        elif self.b == "-":
            self.a = float(self.e) + float(self.c)
            self.B = float(self.a) / float(self.A)
        else:
            print("Operador Invalid")

        return float(self.B)

