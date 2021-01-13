#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre.Numărul globuleţelor albe se citeşte din fişierul « globulet.txt ». 
#Câte globuleţe are brăduţul, ştiind că numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, 
# iar globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. 
#Numărul total de globuleţe este înscris în fişierul « bradut.txt »

with open('globulet.txt','r') as f:
    a=f.readline()
    x=int(a)+3
    y=((int(a))+x)-2
    z= int(a)+x+y
with open('bradut.txt','w') as f:
    f.write(str(z))