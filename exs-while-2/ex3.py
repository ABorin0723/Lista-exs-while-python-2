import math

# 3
# Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digirados pelo usuário
# (num1 e num2). Caso num1 seja menor que num2, imprima uma mensagem de erro e não imprima.

num1 = int(input("Digite o primeiro valor inteiro "))
num2 = int(input("Digite o segundo valor inteiro "))

cont = num1 + 1

while cont < num2:
    print(cont)
    cont += 1
if cont > num2:
    print("Erro, o primeiro número não pode ser maior que o segundo número.")