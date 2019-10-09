class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        try:
            self.a,self.b,self.c,self.d,self.e = self.eq.split(" ")
            self.A,self.B = self.a.split("x")
        except:
            return("l'equacio no segueix el format: ax + b = c")

        try:
            self.A = float(self.A)
            self.c = float(self.c)
            self.e = float(self.e)
        except:
            return("l'equacio conte caracter no calculables: "+self.eq)

        if self.b == "+":
            self.a = float(self.e) - float(self.c)
            self.B = float(self.a) / float(self.A)
        elif self.b == "-":
            self.a = float(self.e) + float(self.c)
            self.B = float(self.a) / float(self.A)
        else:
            return("Operador no valid: "+self.b)

        return float(self.B)

