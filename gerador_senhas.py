import secrets
import string
import pyperclip
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


def gerador_de_senha():
        entrada = entry_tamanho.get().strip()

        if entrada == "":
            messagebox.showerror("Erro", "Não pode ser caractere vazio")
            return
        elif not entrada.isdigit():
            messagebox.showerror("Erro", "Deve ser um valor inteiro positivo")
            return
        
        tam = int(entrada)

        if tam < 6:
            messagebox.showerror("Erro", "A senha deve ter no mínimo 6 caracteres.")
            return

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
        
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)




def copiar_senha():
    senha = entry_senha.get()

    if senha == "":
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")
        return

    pyperclip.copy(senha)
    messagebox.showinfo("Sucesso", "Senha copiada para o clipboard.")       


def forca_senha():
    senha = entry_senha.get()

    if senha == "":
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")
        return
    
    if len(senha) < 8:
         messagebox.showwarning("Aviso", "Senha fraca.")
    elif len(senha) < 10:
         messagebox.showwarning("Aviso", "Senha mediana.")
    else:
         messagebox.showwarning("Aviso", "Senha forte.")

def salvar_senha():
    senha = entry_senha.get()

    if senha == "":
        messagebox.showwarning("Aviso", "Gere uma senha primeiro.")
        return

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open("senhas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Senha: {senha}\n")
        arquivo.write(f"Data: {data_hora}\n")
        arquivo.write("-" * 30 + "\n")

    messagebox.showinfo("Sucesso", "Senha salva com sucesso.")




janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("420x280")
janela.resizable(False, False)

label_titulo = tk.Label(janela, text="Gerador de Senhas", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)

label_tamanho = tk.Label(janela, text="Digite o tamanho da senha:")
label_tamanho.pack()

entry_tamanho = tk.Entry(janela, justify="center")
entry_tamanho.pack(pady=5)

botao_gerar = tk.Button(janela, text="Gerar senha", command=gerador_de_senha)
botao_gerar.pack(pady=8)

label_senha = tk.Label(janela, text="Senha gerada:")
label_senha.pack()

entry_senha = tk.Entry(janela, width=35, justify="center")
entry_senha.pack(pady=5)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_copiar = tk.Button(frame_botoes, text="Copiar", command=copiar_senha)
botao_copiar.grid(row=0, column=0, padx=10)

botao_forca = tk.Button(frame_botoes, text="Medir força", command=forca_senha)
botao_forca.grid(row=0, column=2, padx=10)

botao_salvar = tk.Button(frame_botoes, text="Salvar", command=salvar_senha)
botao_salvar.grid(row=0, column=1, padx=10)

janela.mainloop()



