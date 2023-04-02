import math

# 6
# Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando o usuário digitar
# um número que não seja solicitado, imprima na tela a soma dos valores positivos e pares digitados.

num = int(input("Digite números positivos e pares "))
somaPares = 0

while num >= 0 and num % 2 == 0:
    somaPares += num
    num = int(input("Digite números positivos e pares "))

if num % 2 != 0 or num < 0:
    print(f"o Programa acabou, a soma total de números positivos e pares é {somaPares}")