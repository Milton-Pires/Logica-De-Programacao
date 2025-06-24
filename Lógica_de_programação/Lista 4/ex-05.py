x=int (input ("Digite um numero: "))
y=int (input ("Digite um numero: "))
z=int (input ("Digite um numero: "))
if x>z and y>z:
    menor=z
else:
    if z>y and x>y:
        menor=y
    else:
        menor=x
menor= menor+5
print (menor)