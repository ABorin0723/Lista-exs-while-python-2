import math

# 4
# Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário.
# Caso o primeiro número seja maior que o segundo, seu programa deve imprimir os valores da mesma forma.

num1 = int(input("Digite o primeiro valor inteiro "))
num2 = int(input("Digite o segundo valor inteiro "))

cont = num1 + 1

if num1 == num2 + 1:
    print("não existem números inteiros entre os dois números digitados")
elif num2 == num1 + 1:
    print("não existem números inteiros entre os dois números digitados")
elif num1 == num2:
    print("não existem números inteiros entre os dois números digitados")
else:
    if cont > num2:
        cont = num2 + 1
        while cont < num1:
            print(cont)
            cont += 1
    while cont < num2:
        print(cont)
        cont += 1
