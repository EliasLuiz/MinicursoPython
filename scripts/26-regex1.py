import re
texto = """Meu telefone
e 8888-8888"""
padrao = "[0-9]{4}-[0-9]{4}"
#Flag re.M permite conferir em strings multilinha
#Flag re.I torna a busca insensível a case
resultado = re.match(padrao, texto, re.M|re.I)
if(resultado):
    print("Segue o padrao")
else:
    print("Nao segue o padrao")
resultado = re.search(padrao, texto, re.M|re.I)
if(resultado):
    print("Padrao encontrado:", resultado.group())
else:
    print("Padrao nao encontrado")
