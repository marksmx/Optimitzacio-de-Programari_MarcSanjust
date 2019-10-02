class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        self.a,self.b,self.c,self.d,self.e = self.eq.split(" ")
        self.A,self.B = self.a.split("x")

        self.a = int(self.e) - int(self.c)
        self.B = int(self.a) / int(self.A)

        print int(self.B)

hghg = Equacio("2x + 3 = 7")
hghg.calcula()

#2x = 7 - 3
#x=(7 - 3) / 2
