# for i in  range(3):
#   print("Hello World")

# for i in range(0, 10, 2):
#   planta_atual = str(i)
#   print("Regue a planta " + planta_atual)

  # for i in range(0, 10):
  #   print("Molhe a planta " + str(i))

# numero = 0
# while numero < 6:
#   planta_atual = str(numero)
#   print("Regue a planta " + planta_atual)
#   numero = numero + 1

# for i in range(0, 20, 2):
#   tomates = str(i)
#   print("Regue so as tomates " + tomates)

# for i in range(20):
#   if(i % 2 != 0):
#     continue
#   print("Regue a planta " + str(i))

#   contador = 0
#   while(contador < 10):
#     print("Regue a planta " + str(contador))
#     contador = contador + 1

# def escrever_mutiplicacao(num1, num2):
#   resultado = num1 * num2
#   return resultado

# res = escrever_mutiplicacao(6, 9)
# print(res)

# def escrever_mutiplicacao():
#   resultado = 6 * 9
#   return resultado

# res = escrever_mutiplicacao()
# print(res)

# def escreva_soma(numero1, numero2):
#   resultado = numero1 * numero2
#   frase = str(numero1) + " X " + str(numero2) + " = " + str(resultado)
#   return frase

# res = escreva_soma(5, 2)
# print(res)


# def escrever_multiplicacao(a, b):
#     return f"{a} x {b} = {a * b}"

# for i in range(1, 11):
#     frase_atual = escrever_multiplicacao(9, i)
#     print(frase_atual)


def obter_nome():
    nome = input("Digite seu nome completo: ")
    return nome

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

def main():
    nome = obter_nome()
    ano_nascimento = obter_ano_nascimento()
    ano_atual = 2022
    idade = calcular_idade(ano_nascimento, ano_atual)
    print(f"{nome}, você completou ou completará {idade} anos em {ano_atual}.")

if __name__ == "__main__":
    main()
