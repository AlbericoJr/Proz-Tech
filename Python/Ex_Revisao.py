# Vocês foram designados para criarem uma calculadora simples que permita aos usuários realizar operações básicas, como adição, subtração, multiplicação e divisão. O programa deve continuar executando até que o usuário escolha sair. Cada vez que uma operação é concluída, o usuário deve ter a opção de realizar outra operação ou sair do programa.

while True:
  print("Escolha uma opção:")
  print("1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("5 - Sair")
  escolha = input("Digite o número da sua esolha: ")

  if escolha in ["1", "2", "3", "4"]:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == "1":
      resultado = num1 + num2
    elif escolha == "2":
      resultado = num1 - num2
    elif escolha == "3":
      resultado = num1 * num2
    elif escolha == "4":
      resultado = num1 / num2
  elif escolha == "5":
      print("Saindo do programa...")
      break
  else:
      print("Escolha inválida, por favor tente novamente.")

  print(f"O resultado é: {resultado}")