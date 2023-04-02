import math

# 8
# O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa
# que solicita ao usuário que ele digite seu usuário e senha. O programa só termina quando ele acertar.
# Você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas (3) o programa
# deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO.


user = input("digite o usuário ")
password = input("digite a senha ")

correctUser = "USER10"
correctPass = "PASSWORD1234"
    
tentativas = 2

while user.upper() != correctUser or password.upper() != correctPass:
    print("Usuário ou senha incorretos, tente novamente:")
    user = input("digite o usuário ")
    password = input("digite a senha ")
    if user.upper() == correctUser and password.upper() == correctPass:
        print("LOGIN EFETUADO COM SUCESSO")
        break
    tentativas -= 1
    if tentativas == 0:
        print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO")
        break
