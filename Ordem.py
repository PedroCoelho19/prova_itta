lista = list()
listaOrdenada = list()
n = int(input("Digite quantos números você quer na lista: "))
for i in range(0,n):
    num = int(input("Digite um número: "))
    lista.append(num)
    maior = lista[0]
    if lista[i] > maior:
        maior = lista[i]
        listaOrdenada.append(maior)
    else:
        menor = lista[i]
listaOrdenada.append(menor)





print(listaOrdenada)

