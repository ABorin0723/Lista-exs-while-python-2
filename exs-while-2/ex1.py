import math

# 1
# Solicite que o usuário digite um numero aleatório. Se o número for menor que zero, diga que é negativo
# se for igual a zero diga que é zero e se for maior que zero, diga que é positivo. Repita 10 vezes.

cont = 0

while cont < 10:
    numAleatorio = float(input("Digite um número aleatório "))
    if numAleatorio < 0:
        print(f"o número {numAleatorio} é negativo")
    elif numAleatorio == 0:
        print(f"o número {numAleatorio} é igual a zero")
    else:
        print(f"o número {numAleatorio} é positivo")
    cont += 1