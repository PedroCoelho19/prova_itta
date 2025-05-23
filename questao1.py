# questão 1
num = 0
listaDeNumeros = [100]

for num in range (100):
    if num % 2 == 0:
       listaDeNumeros.append(num)
    
    num = num + 1

print(listaDeNumeros)


