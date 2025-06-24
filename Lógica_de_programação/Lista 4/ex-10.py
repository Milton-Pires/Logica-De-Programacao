x=int (input ("Digite um numero: ")) 
y=int (input ("Digite um numero: "))
if x>y:
    z=y*10
    m=x/2
else:
    z=x*10
    m=y/2
h=m+z
if h % 2 == 0:
    print (h, (" é par!"))
else:
    print (h, (" é impar!"))