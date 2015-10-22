idade = 21

if idade >= 18:
    if idade >= 70:
        print("Voto facultativo")
    else:
        print("Voto obrigatorio")
elif not idade < 16:
    print("Voto facultativo")
else:
    print("Nao pode votar")
