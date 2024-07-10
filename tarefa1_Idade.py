from datetime import datetime
#função
def obter_data_nascimento():
    while True: 
        try:
            data_nascimento = int(input("Digite seu ano de nascimento (formato AAAA) "))
            return data_nascimento
        except ValueError:
            print("Data inválida. Por favor, digite no formato AAAA")


nome = input("Digite seu nome: ")
data_nascimento = obter_data_nascimento()
pessoa = {
    'nome': nome,
    'data_nascimento': data_nascimento
}

print(f"\nNome: {pessoa['nome']}, Ano de Nascimento: {pessoa['data_nascimento']}")

data_atual = datetime.now()
ano_atual = data_atual.year
print(f"Estamos no ano de: {ano_atual}\n")
idade = ano_atual - data_nascimento
print(f"Idade: {idade} anos")


if (idade <= 10) and (idade >= 0):
    print("Criança")

elif 10 < idade <= 18:
    print("Adolescente")

elif 18 < idade <= 65:
    print("Adulto")

elif 65 < idade <= 125:
    print("Sénior")    

elif idade > 125:
    print("Múmia")   

elif idade < 0:
    print("Ainda não Nasceu")   

