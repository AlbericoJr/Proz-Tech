# teste 1
def Mostrarnumero():
  valor_liberado = False
  while(not valor_liberado):
    try:
      num = int(input("Escolha um número entre 0 e 100."))
      if(num >= 0 and num <= 100):
        print("O numero escolhido foi:" + str(num))
        valor_liberado = True
      else:
        print("O número tem que ser entre 0 e 100.")
    except:
      print("Coloque um valor válido. Entre 0 e 100.")

Mostrarnumero()

# teste 2
def Mostrarnumero():
  valor_liberado = False
  while(not valor_liberado):
    try:
      num = int(input("Digite um valor: "))
      if(num % 2 == 0):
        print("O numero escolhido foi: " + str(num) + ", e é divísivel por 2.")
        valor_liberado = True
      else:
        print("O número não é divísivel por 2.")
    except:
      print("Coloque um valor válido.")

Mostrarnumero()

# teste 3
def Mostrarnumero():
  valor_liberado = False
  while(not valor_liberado):
    try:
      num = int(input("Digite um valor: "))
      if(num % 2 == 0 and num % 3 == 0):
        print("O numero escolhido foi: " + str(num) + ", e é divísivel por 2 e por 3.")
        valor_liberado = True
      else:
        print("O número não é divísivel por 2 e 3.")
    except:
      print("Coloque um valor válido.")

Mostrarnumero()