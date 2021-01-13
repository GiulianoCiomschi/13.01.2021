#Ion spune 10, Vasile spune 8 9 10 11 12. 
# Ajutaţi-l pe Vasile să găsească răspunsul mai repede. 
# Din fişierul « input.txt » se citeşte un număr, 
# în fişierul « output.txt » - se înscrie consecutivitatea numerelor.
with open('input.txt','r') as f:
    a=f.readline()
    x3=int(a)
    x1=x3-2
    x2=x3-1
    x4=x3+1
    x5=x4+1
with open('output.txt','w') as f:
    f.write(str(x1))
    f.write(" ")
    f.write(str(x2))
    f.write(" ")
    f.write(a)
    f.write(" ")
    f.write(str(x4))
    f.write(" ")
    f.write(str(x5))


