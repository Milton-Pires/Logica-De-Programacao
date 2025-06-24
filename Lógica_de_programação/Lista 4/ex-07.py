x=int (input ("Digite um numero: ")) 
y=int (input ("Digite um numero: "))
z=int (input ("Digite um numero: "))
menor=x
meio=y
maior=z
if menor > maior:
    menor, maior = maior,menor
if menor> meio:
    menor, meio = meio, menor
if meio> maior:
    meio, maior= maior, meio
print (menor,meio,maior)