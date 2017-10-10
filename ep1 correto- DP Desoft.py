from turtle import *

print('''

Exemplo: 
Regra inicial: F-G
Regra de producao:  F-G-F-G-F-G-F-G-F-G-F-G-F-G-F-G-F-G-F
Repeticao: 6
''')
inicial = str(input("Entre com string inicial: " ))
regra = str(input("Entre com a regra de producao: "))
repeticao = int(int(input("Repeticao: " )))
regra_final=""  

print(inicial)
print(regra)
print(repeticao)





e=0
regra_final = inicial
while e < repeticao:
    regra_final = str.replace(regra_final, "F", regra)
    
    #regra_final = regra_final.replace("F", 'F-FF+F-' )
    e += 1

print(regra_final)

regra_final = regra

    
     

def producao(inicial, regra, repeticao):
    
    regra = regra.split(' ')
    
    for i in range(repeticao):
        regra_final= i
    return i
            
print(regra_final)

            


speed(4)
for e in regra_final.upper():
    if e == "F":
       color('yellow')
       forward(250)
       pendown()
    elif e == "G":
       color("blue")
       forward(120)
    elif e == "-":
        left(266)
    elif e == "+":
        right(144)
        
    elif abs(pos()) < 1:
        break
done()





