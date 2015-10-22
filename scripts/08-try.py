try:
    print(10 / 0)
except ZeroDivisionError:
    print("ops...")

try:
    raise Exception('Deu errado')
except Exception as e:
    print(e)
finally:
    print("Exemplo de bloco try-except")
