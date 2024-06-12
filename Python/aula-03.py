# lista = ["Alberico", "Rebeka", "Junior"]

# for nome in lista:
#   print(nome)

# Achar elementos em um array

def achar_elementos(elem, arr):
  achou = False

  for i in range(len(arr)):
    if arr[i] == elem:
      achou = True
      

    if (achou == False):
      print("Não achamos o elemento: " + elem)
    else:
      print("Achamos o elemento: " + elem)
      
nomes = ["Rafael", "Arthur", "Lucas", "Pedro"]

achar_elementos("Alberico", nomes)