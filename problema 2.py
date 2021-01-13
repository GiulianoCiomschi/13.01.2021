#Se dau două numere. Să se înmulţească cel mai mare cu doi şi cel mai mic cu trei şi să se afişeze rezultatele. 
with open("numere.txt","r") as f:
    a=f.readline()
    b=f.readline()
if int(a)> int(b):
    x=int(a)*2
    y=int(b)*3
if int(a)<int(b):
    x=int(a)*3
    y=int(b)*2
else:
    x=y="Numerele date sunt egale"
with open("produs.txt","w") as f:  
    f.write(str(x))
    f.write(" ")
    f.write(str(y))     