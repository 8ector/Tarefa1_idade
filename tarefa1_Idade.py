from datetime import datetime



while True:
    try:
        idade = int(input("Qual é a sua idade?"))
        break
    except ValueError:
        print("Dados incorreto")


if idade >= 18 and idade <= 125:
    print("Maior de 18")

elif idade > 125:
    print("Idade muita elevada, já és uma múmia")

else:
    print("Idade deve ser maior do que zero!!")

