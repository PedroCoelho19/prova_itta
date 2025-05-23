vetor1 = [5, 1, 8, 2, 3]
vetor2 = []

maior = 0

for i in range(len(vetor1)):
    if vetor1 > maior:
        maior = vetor1
        
vetor2.append(maior)

for i in range(len(vetor1)):
    if vetor1 < vetor2