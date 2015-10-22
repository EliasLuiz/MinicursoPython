class Pai:
    def Print(self):
        print('classe pai')

class Filho(Pai):
    def Print(self):
        print('classe filho')

class Filho2(Pai):
    #declarado mas nao implementado
    pass

a = Pai()
a.Print()

b = Filho()
b.Print()

c = Filho2()
c.Print()
