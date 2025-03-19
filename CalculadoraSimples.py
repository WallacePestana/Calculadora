def calculadora():
    print("Selecione a operação")
    print("1 = Soma")
    print("2 = Subtração")
    print("3 = Multiplicação")
    print("4 = Divisão")

    escolha = int(input("Digite o número escolhido: "))

    while escolha not in (1, 2, 3, 4):
        print("Número escolhido inválido. Tente novamente.")
        escolha = int(input("Digite o número escolhido: "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif escolha == 2:
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif escolha == 3:
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif escolha == 4:
        if num1 == 0:
            print("Não é possível dividir números por zero")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)

# Chama a função calculadora para executar o programa
calculadora()