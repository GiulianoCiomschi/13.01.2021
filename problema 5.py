#Afişaţi tabla înmulţirii cu numărul n. 
# Exemplu: pentru n=5, se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
#Din fişierul « numar.txt » se citeşte un număr,
#  în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr.

with open('numar.txt','r') as f:
    a=f.readline()
    x1='1'+'*'+ str(int(a)) +'='+str((int(a)*1))
    x2='2'+'*'+ str(int(a)) +'='+str((int(a)*2))
    x3='3'+'*'+ str(int(a)) +'='+str((int(a)*3))
    x4='4'+'*'+ str(int(a)) +'='+str((int(a)*4))
    x5='5'+'*'+ str(int(a)) +'='+str((int(a)*5))
    x6='6'+'*'+ str(int(a)) +'='+str((int(a)*6))
    x7='7'+'*'+ str(int(a)) +'='+str((int(a)*7))
    x8='8'+'*'+ str(int(a)) +'='+str((int(a)*8))
    x9='9'+'*'+ str(int(a)) +'='+str((int(a)*9))
    x10='10'+'*'+ str(int(a)) +'='+str((int(a)*10))
with open('inmultire.txt','w') as f:
    f.write(str(x1))
    f.write("\n")
    f.write(str(x2))
    f.write("\n")
    f.write(str(x3))
    f.write("\n")
    f.write(str(x4))
    f.write("\n")
    f.write(str(x5))
    f.write("\n")
    f.write(str(x6))
    f.write("\n")
    f.write(str(x7))
    f.write("\n")
    f.write(str(x8))
    f.write("\n")
    f.write(str(x9))
    f.write("\n")
    f.write(str(x10))
    