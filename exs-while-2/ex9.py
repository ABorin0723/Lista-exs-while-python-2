import math

# 9
# Exercício 8, mas o usuário define o login e a senha

correctUser = input("defina seu usuário ")
correctPass = input("defina sua senha ")

user = input("digite o usuário ")
password = input("digite a senha ")

    
tentativas = 2

while user.upper() != correctUser.upper() or password.upper() != correctPass.upper():
    print("Usuário ou senha incorretos, tente novamente:")
    user = input("digite o usuário ")
    password = input("digite a senha ")
    if user.upper() == correctUser.upper() and password.upper() == correctPass.upper():
        print("LOGIN EFETUADO COM SUCESSO")
        break
    tentativas -= 1
    if tentativas == 0:
        print("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO")
        break
