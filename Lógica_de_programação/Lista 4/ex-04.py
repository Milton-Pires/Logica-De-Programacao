x=int (input ("Digite um numero: "))
y=int (input ("Digite um numero: "))
z=int (input ("Digite um numero: "))
if x>y and x>z:
    maior=x
else:
    if y>x and y>z:
        maior=y
    else:
        maior=z 
print (maior) 