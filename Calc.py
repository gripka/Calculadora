# Importar o módulo math para operações matemáticas avançadas
import math

# Obter a entrada do usuário para selecionar a operação e verificar se é válida
while True:
    try:
        op = int(input(print("Selecione a operação: \n1. Somar \n2. Subtrair \n3. Multiplicar \n4. Dividir \n5. Exponenciação \n6. Raiz Quadrada \n7. Logaritmo")))
        if op not in [1, 2, 3, 4, 5, 6, 7]: 
            raise ValueError
        break
    except ValueError:
        print ("Opção inválida, tente novamente!")

# Definir as operações matemáticas
while True:
    try:
        num1 = float(input("Digte o primeiro número: "))
        if op != 6:
            num2 =  float(input("Digite o segundo número: "))
            if op == 4 and num2 == 0:
                raise ZeroDivisionError
        break
    except ValueError:
        print("Número inválido")
    except ZeroDivisionError:
        print ("Erro! Divisão por zero")

# Executar a operação selecionada
if op == 1:
    resultado = (num1 + num2)
    sinalop = "+"
elif op == 2:
    resultado = (num1 - num2)
    sinalop = "-"
elif op == 3:
    resultado = num1 * num2
    sinalop = "*"
elif op == 4:
    resultado = num1 / num2
    sinalop = "/"
elif op == 5:
    resultado = num1 ** num2
    sinalop = "^"
elif op == 6:
    resultado = num1 ** 0.5
    sinalop = "√"
elif op == 7:
    base = float(input("Digite a base do logaritmo: "))
    resultado = math.log(num1, base)
    sinalop = "log"
    #return
#return menu()

# Exibir o resultado
if op in [1, 2, 3, 4, 5, 7]:
    print(f"{num1} {sinalop} {num2} = {resultado}")
elif op == 6:
    print(f"A raiz quadrada de {num1} é {resultado:.2f}")

#def menu():
#    continuando = input("Iniciar a calculadora? \n1-Sim \n2-Não \n")
#    if continuando == ("1"):
#        calc()
#    elif continuando == ("2"):
#        print("Até mais! :)")
#        exit()
#    else:
#        print("Entrada inválida. Por favor escolha 1 ou 2.")
#        return menu()

#menu():