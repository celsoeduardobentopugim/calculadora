sair = "sair"

numero01 = input("digite o primeiro numero")
numero02 = input("digite o segundo numero")
operador = input("digite o operador (+,-,/,*)")

numero01_float = 0
numero02_float = 0

try:
    numero01_float = float(numero01)
    numero02_float = float(numero02)
except:
    print("valor não aceito")



if operador == "+":
    print(f"{numero01_float} + {numero02_float} =", numero01_float + numero02_float)


 
if operador == "-":
    print(f"{numero01_float} - {numero02_float} =", numero01_float - numero02_float) 


    
if operador == "*":
    print(f"{numero01_float} * {numero02_float} =", numero01_float * numero02_float)


    
if operador == "/":
    print(f"{numero01_float} / {numero02_float} =", numero01_float / numero02_float)
    








