from zeep import Client

client = Client('http://localhost:8000/?wsdl')

while True:
    print("Escolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 5:
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    match opcao:
        case 1:
            print("Resultado:", client.service.soma(a, b))
        case 2:
            print("Resultado:", client.service.subtracao(a, b))
        case 3:
            print("Resultado:", client.service.multiplicacao(a, b))
        case 4:
            try:
                print("Resultado:", client.service.divisao(a, b))
            except ValueError as e:
                print("Erro:", e)
        case _:
            print("Opção inválida")