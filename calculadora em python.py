while True:   
#crie um menu de operação 

    print("SELECIONE A OPERAÇÃO DESEJADA")
    print("[1] PARA SOMAR")
    print("[2] PARA SUBTRAIR")
    print("[3] PARA MULTIPLICAR")
    print("[4] PARA DIVIDIR")

    #INTERAÇÃO COM O USUARIO 
    operacao = input("qual operação você deseja realizar?\n")

    #criando a operação e apresentação de resposta 

    # adição

    if operacao == "1":
        a1 = float(input("digite o primeiro valor:\n"))
        a2 = float(input("digite o segundo valor:\n"))
        adicao = a1 + a2 
        print(f"na soma de {a1} e {a2} o resultado é {adicao}\n")
        print("*"*53,"\n")

        
    #subtração
    elif operacao == "2":
        b1 = float(input("\n digite o primeiro valor:"))
        b2 = float(input("\n digite o segundo valor:"))
        subtracao = b1 - b2 
        print(f"na subtração de {b1} e {b2} o resultado é {subtracao} \n")
        print("*"*33,"\n")


        #multiplicação 
        
    elif operacao == "3":
        c1 = float(input("digite o primeiro valor:\n"))
        c2 = float(input("digite o segundo valor:\n"))
        multiplicacao = c1 * c2 
        print(f"na MULTIPLICAÇÃO de {c1} e {c2} o resultado é {multiplicacao} \n")
        print("*"*33,"\n")


        # divizão
        
    elif operacao == "4":
        d1 = float(input("\n digite o primeiro valor:"))
        d2 = float(input("\n digite o segundo valor:"))
        while d2 == 0:
            print("o seguinte valor não pode ser zero!")
        d2 = float (input("digite o segundo valor (diferente de zero):\n"))
        divizao = d1 / d2 
        print(f"na divisao de {d1} e {d2} o resultado é {divizao} \n")
        print("*"*33,"\n")

    else :
        print("OPERAÇÃO INVALIDA!\n TENTE NOVAMENTE.")

    continuar_usando = input("gostaria de fazer um novo calculo? (s/n):\n").strip().lower()
    print("*\n"*33)
    if continuar_usando != "s":
        break
