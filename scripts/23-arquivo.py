arquivo = open("22 - teclado.py", "r")

#executa um laco for por todas as linhas do arquivo
for i in arquivo.readlines():
    print(i)

arquivo.close()
