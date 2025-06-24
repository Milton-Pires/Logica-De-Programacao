x=int (input ("Digite um numero:"))
y=int (input ("Digite um numero:"))
z=int (input ("Digite um numero:"))
maior=x
#descobrindo o maior aqui ó:
if y>maior:
    maior=y
if z>maior:
    maior=z
#descobrindo o segundo maior aqui ó:
if maior==y:
    if z>x:
        segun_maior=z
    else:
        segun_maior=x
if maior==x:
    if z>y:
        segun_maior=z
    else:
        segun_maior=y
if maior==z:
    if x>z:
        segun_maior=x
    else:
        segun_maior=z
#fazendo o looping aqui:
while segun_maior<maior:
    segun_maior=segun_maior+1
    print(segun_maior)