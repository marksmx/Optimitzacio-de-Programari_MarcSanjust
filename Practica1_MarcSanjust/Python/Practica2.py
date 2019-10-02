class Equacio:
    def __init__(self,eq):
        self.eq = eq

    def calcula(self):
        self.a,self.b,self.c,self.d,self.e = self.eq.split(" ")
        self.A,self.B = self.a.split("x")

        if self.b == "+":
            self.a = float(self.e) - float(self.c)
            self.B = float(self.a) / float(self.A)
        else:
            self.a = float(self.e) + float(self.c)
            self.B = float(self.a) / float(self.A)

        print float(self.B)

#hghg = Equacio("200x - 50 = -78")
#hghg.calcula()
