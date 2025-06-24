notas = [0.0] * 20
medias = [0.0] * 5

i = 0
while i < 5:
    print("Aluno número")
    print(i + 1)

    j = 0
    soma = 0.0
    while j < 4:
        posicao = i * 4 + j

        print("Digite a nota")
        print(j + 1)
        nota = float(input())

        if nota >= 0 and nota <= 10:
            notas[posicao] = nota
            soma = soma + nota
            j = j + 1
        else:
            print("Nota inválida. Digite entre 0 e 10.")
    
    medias[i] = soma / 4
    i = i + 1
i = 0
while i < 5:
    print("Notas do aluno")
    print(i + 1)

    j = 0
    while j < 4:
        posicao = i * 4 + j
        print("Nota")
        print(j + 1)
        print(":")
        print(notas[posicao])
        j = j + 1

    print("Média:")
    print(medias[i])
    i = i + 1