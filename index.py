# Função para realizar a adição
def adicao(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

# Função principal
def main():
    print("Calculadora de Operações Matemáticas")
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == "1":
        resultado = adicao(num1, num2)
    elif escolha == "2":
        resultado = subtracao(num1, num2)
    elif escolha == "3":
        resultado = multiplicacao(num1, num2)
    elif escolha == "4":
        resultado = divisao(num1, num2)
    else:
        resultado = "Opção inválida."

    print(f"Resultado: {resultado}")

if __name__ == "__main":
    main()
