"""
Alunos:
Bruno Ciccio - RM 99097
José Luiz - RM 99488
"""

def menu():
    print(f"""
1 - Intervalo
2 - Intervalo Aberto e Fechado
3 - Intervalo em Ordem Crescente ou Decrescente
0 - SAIR
""")

def intervalo():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num1 < num2:
        print("[", end="")
        for i in range(num1, num2 + 1):
            print(f"{i} ", end="")
        print("]")
    elif num1 > num2:
        print("[", end="")
        for i in range(num2, num1 + 1):
            print(f"{i} ", end="")
        print("]")
    else:
        print(num1)

def intervalo_a_f():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    a_f = input("][ Aberto ou [] Fechado: ")
    if a_f.lower() == '][':
        if num1 < num2:
            print("]", end="")
            for i in range(num1 + 1, num2):
                print(f"{i} ", end="")
            print("[")
        elif num1 > num2:
            print("]", end="")
            for i in range(num2 + 1, num1):
                print(f"{i} ", end="")
            print("[")
        else:
            print("]", num1, "[")
    elif a_f.lower() == '[]':
        if num1 < num2:
            print("[", end="")
            for i in range(num1, num2 + 1):
                print(f"{i} ", end="")
            print("]")
        elif num1 > num2:
            print("[", end="")
            for i in range(num2, num1 + 1):
                print(f"{i} ", end="")
            print("]")
        else:
            print("[", num1, "]")

def intervalo_c_d():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num1 < num2:
        print("[", end="")
        for i in range(num1, num2 + 1):
            print(f"{i} ", end="")
        print("]")
    elif num1 > num2:
        print("[", end="")
        for i in range(num1, num2 - 1, -1):
            print(f"{i} ", end="")
        print("]")
    else:
        print("[", num1, "]")

def invalido():
    print("Opção não é valída!")

def continuar_menu():
    print(f"""
Continuar usando o menu:
(S)im
(N)ão
    """)

def exibir_contagem():
    print(f"""
1 - Intervalo - {cont1}
2 - Intervalo Aberto e Fechado - {cont2}
3 - Intervalo em ordem Crescente e Decrescente - {cont3}""")
cont1 = 0
cont2 = 0
cont3 = 0

while True:
    menu()
    escolha = input("Escolha a opção: ")
    if escolha == "1":
        intervalo()
        cont1 +=1
    elif escolha == "2":
        intervalo_a_f()
        cont2 +=1
    elif escolha == "3":
        intervalo_c_d()
        cont3 +=1
    elif escolha == "0":
        exibir_contagem()
        break
    else:
        invalido()
    continuar_menu()
    continuar = input("Digite aqui: ")
    if continuar.lower() == "n":
        exibir_contagem()
        break
    elif continuar.lower() == "s":
        continue
    else:
        invalido()