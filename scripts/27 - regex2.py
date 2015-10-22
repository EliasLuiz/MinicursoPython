import re
texto = """Meu telefone
e 8888-8888"""
padrao = re.compile("[0-9]{4}-[0-9]{4}")
resultado = padrao.match(texto, re.M|re.I)
if(resultado):
    print("Segue o padrao")
else:
    print("Nao segue o padrao")
resultado = padrao.search(texto, re.M|re.I)
if(resultado):
    print("Padrao encontrado:", resultado.group())
else:
    print("Padrao nao encontrado")
