# def enviar_convites():

#   print("Informe a quantidade de convites: ")

#   convites = int(input())


#   for i in range(convites):
#     nome = input(f"Informe o nome do convidado de número {i + 1} ")
#     print(f"Enviando convite para {nome}")

# enviar_convites()

# while

# def enviar_convites():

#   print("Informe quantidade de convites: ")

#   qconvites = int(input())

#   contador = 0 

#   while(contador < qconvites):
#     nome = input(f"Informe o nome do convidado de número {contador + 1} ")
#     print(f"Enviando convite para {nome}")
#     contador = contador + 1

# enviar_convites()	


# Exercicos
# Programa de Contagem de Caracteres ou Número de Palavras

# Desenvolva um programa Python que oferece a funcionalidade de contar o número de caracteres ou o número de palavras em um texto fornecido pelo usuário. O programa continuará executando até que o usuário opte por sair do sistema.

def contar_sem_espaco(texto):
  return len(texto.replace(" ", ""))

def contar_palavras(texto):
  return len(texto.split())

while True:
  print("Escolha uma opção:")
  print("1 - Contador de caracteres")
  print("2 - Contador de palavras")
  print("3 - Sair")
  
  escolha = input("Digite o número da sua esolha: ")

  if escolha == "1":
    texto = input("Digite o  texto: ")
    caracter = contar_sem_espaco(texto)
    print(f"O número de caracteres no texto é: {caracter}")
  elif escolha == "2":
    texto = input("Digite o texto: ")
    num_palavras = contar_palavras(texto)
    print(f"O número de palavras no texto é: {num_palavras}")
  elif escolha == "3":
    print("Saindo do programa...")
    break
  else:
    print("Escolha inválida, por favor tente novamente.")

    