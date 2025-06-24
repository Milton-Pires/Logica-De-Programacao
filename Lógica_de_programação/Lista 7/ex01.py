x=int(input ("Digite o 1° numero"))
y=int(input ("Digite o 2° numero"))
z=int(input ("Digite o 3° numero"))
h=int(input ("Digite o 4° numero"))
p=int(input ("Digite o 5° numero"))
arr1 = [x, y, z, h, p]
i=0
while i < 5:
    minimo=i
    j=i+1
    while j<5:
        if arr1[j]<arr1[minimo]:
            minimo=j
        j=j+1

    if minimo != i:
        arr1[i], arr1[minimo]= arr1[minimo], arr1[i]
    i=i+1
print("Em ordem crescente fica:", arr1)