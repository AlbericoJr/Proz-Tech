# condiçãos

# nota = 7
# if (5 > 10):
#   print("Aprovado")

# elif (5 < 3):
#   print("Recuperação")

# else:
#   print("Reprovado")

# operadores codicionais
# <
# >
# <=
# >=
# ==
# !=

# logico
# or
# and
# not

# nota = 7
# if nota == 7 or nota < 10:
#   print("Aprovado")
# else:
#   print("Reprovado")

# repetição
# for i in range(5):
#   print(i)

# contador = 0

# while contador <= 8:
#   print(contador)
#   contador += 1


def classificar_produto(preco, condicao):
    if preco < 50:
        if condicao.lower() == 'sim':
            return 'Baixo'
        else:
            return 'FIM'
    elif 50 <= preco <= 100:
        if condicao.lower() == 'sim':
            return 'Médio'
        else:
            return 'FIM'
    elif preco > 100:
        if condicao.lower() == 'sim':
            return 'Alto'
        else:
            return 'FIM'
    else:
        return 'FIM'

def main():
    print("Início")
    
    # Receber produtos (entrada do usuário)
    preco = float(input("Digite o preço do produto: R$ "))
    condicao = input("Condição do produto (SIM/NÃO): ")
    
    # Classificar produto
    resultado = classificar_produto(preco, condicao)
    
    print("Classificação do produto:", resultado)
    print("FIM")

if __name__ == "__main__":
    main()
