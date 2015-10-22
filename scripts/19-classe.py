class Funcionario:
    #contador estatico de funcionarios
    contador = 1
	
        #construtor
    def __init__(self, nome, salario):
        #self eh o nome padrao para o objeto que realizou a chamada
        #equivalente ao 'this' de outras linguagens
        #nota: pode ter outro nome, self eh somente um padrao
        self.nome = nome
        self.salario = salario
        self.id = Funcionario.contador
        Funcionario.contador += 1
            
    #define como o objeto deve ser exibido se convertido para string
    def __str__(self):
        return "Funcionario {}\nNome: {}\nSalario: R${:.2f}".format(self.id, self.nome, self.salario)
	 
funcionarios = {}
funcionarios['Jose'] = Funcionario('Jose da Silva', 2000)
funcionarios['Maria'] = Funcionario('Maria da Silva', 2000)

for _, i in funcionarios.items():
	print(i)
