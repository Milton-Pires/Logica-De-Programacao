x=int (input ("Digite um numero:"))
y=int (input ("Digite um numero:"))
if x>y:
    while y<x:
        y=y+1
        print (y)
else:
    while x<y:
        x=x+1
        print (x)