listaDesordenada = [5]
listaOrdenada = [5]

for i in range(5):
    num = int(input('número: '))
    listaDesordenada.append(num)

for i in range(0,5):
    if listaDesordenada[i] < listaDesordenada[i+1]:
        listaOrdenada.append(listaDesordenada[i+1])
    elif listaDesordenada[i] < listaDesordenada[i+1]:
        listaOrdenada.append(listaDesordenada[i])

print(listaOrdenada)