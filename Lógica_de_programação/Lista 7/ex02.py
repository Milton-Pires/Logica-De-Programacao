numeros = [0] * 5
i = 0
while i < 5:
    print("Digite o número", i + 1)
    num = int(input())
    numeros[i] = num
    i = i + 1
    #Bubble-sort ensinado na ultima aula:
i = 0
while i < 4:
    j = 0
    while j < 4 - i:
        if numeros[j] > numeros[j + 1]:
            # Troca os valores
            aux = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = aux
        j = j + 1
    i = i + 1
print("Números em ordem crescente:")
i = 0
while i < 5:
    print(numeros[i])
    i = i + 1