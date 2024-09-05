continue_usando = "sim"

while continue_usando == "sim":break
#crie um menu de operação 

print("SELECIONE A OPERAÇÃO DESEJADA")
print("+ PARA SOMAR")
print("- PARA SUBTRAIR")
print("* PARA MULTIPLICAR")
print("/ PARA DIVIDIR")

#INTERAÇÃO COM O USUARIO 
operacao = input("\n qual operação você deseja realizar? ")

#criando a operação e apresentação de resposta 

# adição

if operacao == "+":
    a1 = float(input("\n digite o primeiro valor:"))
    a2 = float(input("\n digite o segundo valor:"))
adicao = a1 + a2 
print("na soma de ",a1,"e",a2,"o resultado é ",adicao,"\n")
print("*"*53,"\n")
continuar_usando = input("gostaria de fazer um novo calculo?").upper()
print("*"*33,"/n")
   
   #subtração
if operacao == "-":
    b1 = float(input("/n digite o primeiro valor:"))
    b2 = float(input("/n digite o segundo valor:"))
subtracao = b1 - b2 
print("na subtração de ",b1,"e",b2,"o resultado é ",subtracao,"/n")
print("*"*33,"/n")
continuar_usando = input("gostaria de fazer um novo calculo?").upper()
print("*"*33,"/n")

    #multiplicação 
    
if operacao == "*":
    c1 = float(input("/n digite o primeiro valor:"))
    c2 = float(input("/n digite o segundo valor:"))
multiplicacao = c1 * c2 
print("na multiplicação de ",c1,"e",c2,"o resultado é ",multiplicacao,"/n")
print("*"*33,"/n")
continuar_usando = input("gostaria de fazer um novo calculo?").upper()
print("*"*33,"/n")

    # divizão
    
if operacao == "/":
    d1 = float(input("/n digite o primeiro valor:"))
    d2 = float(input("/n digite o segundo valor:"))
    while d2 == 0:
        print("o seguinte valor não pode ser zero!")
    d2 = float (input("/n digite o segundo valor (diferente de zero):"))
divizao = d1 / d2 
print("na divizão de ",d1,"e",d2,"o resultado é ",divizao,"/n")
print("*"*33,"/n")
continuar_usando = input("gostaria de fazer um novo calculo?").upper()
print("*"*33,"/n")