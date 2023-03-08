def calc():
    try:
        num1 = int(input("Digte o primeiro número: "))
        op = input("Selecione a operação: (+, -, /, *): ")
        num2 =  int(input("Digite o segundo número: "))
    except ValueError:
        print ("Caractere inválido")
    pass


    while True:
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "/":
            resultado = num1 / num2
            if num2 == 0:
                print("Erro: Divisão por zero!")
                return
            
        else: 
            print ("Deu não, tenta de novo")
        print (f"O resultado é: {resultado}")
        return menu()

def menu():
    print("Selecione a operação.")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    continuando = input("Selecione uma das opções acima: ")
    if continuando == ("1"):
        #inicio()
        calc()
    elif continuando == ("2"):
        print("Até mais! :)")
        exit()
    else:
        print("Entrada inválida. Por favor digite um número entre 1 e 5.")
        return menu()

menu()


