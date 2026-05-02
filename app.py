import secrets
import string
import pyperclip
from datetime import datetime


while True:
    while True:
        entrada = input("Digite o tamanho da senha: ").strip()

        if entrada == "":
            print("Não pode ser caractere vazio")
        elif not entrada.isdigit():
            print("Deve ser um valor inteiro positivo")
        elif int(entrada) < 6:
            print("A senha deve ter no mínimo 6 caracteres.")
        else:
            tam = int(entrada)
            break

    simbolos = "!$#&*"
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits

    todos_caracteres = maiusculas + minusculas + numeros + simbolos



    lista_senha = [
            secrets.choice(simbolos),
            secrets.choice(maiusculas),
            secrets.choice(minusculas),
            secrets.choice(numeros)
        ]
    

    for i in range(tam - 4):
            lista_senha.append(secrets.choice(todos_caracteres))
    
            
    secrets.SystemRandom().shuffle(lista_senha)

    senha = "".join(lista_senha)
    print("Senha gerada: ", senha)
    pyperclip.copy(senha)

    with open("senhas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(senha + "\n")
        arquivo.write(f"Data: {datetime.now().strftime("%d/%m/%Y %H:%M")}\n")
        arquivo.write("-" * 30 + "\n")
    print("Senha salva e copiada para o cliipboard com sucesso.")

    while True:
        repetir = input("Deseja gerar outra senha? (s/n): ").strip().lower()

        if repetir == "s":
            break
        elif repetir == "n":
            print("Programa encerrado.")
            exit()
        else:
            print("Digite apenas s ou n.")
        
