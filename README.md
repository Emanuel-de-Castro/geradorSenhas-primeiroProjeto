Gerador de senhas seguras em Python

Um gerador de senhas robusto em Python com interface gráfica Tkinter, validação completa, salvamento em arquivo e análise de força.


 Funcionalidades

     Gera senhas com maiúscula, minúscula, número e símbolo obrigatórios

     Validação do tamanho (mínimo 6 caracteres)

     Interface gráfica intuitiva com Tkinter

     Cópia automática para clipboard

     Salvamento com data/hora em arquivo TXT

     Medidor simples de força da senha (fraca/média/forte)

     Tratamento completo de erros


   

Instalação


    pip install pyperclip

Executar

    python gerador_senhas.py

Funcionamento

    Digite o tamanho da senha (mínimo 6)

    Clique em "Gerar senha"

    A senha aparece no campo

    Clique "Copiar" para área de transferência

    Clique "Salvar" para arquivo senhas.txt

    Clique "Medir força" para análise



Tecnologias

    secrets:	Geração criptograficamente segura
    Tkinter:	Interface gráfica nativa
    pyperclip:	Cópia para clipboard
    datetime:	Timestamp nos logs

Estrutura do projeto
   
     gerador_senhas/
         ├── gerador_senhas.py     # App principal
         ├── senhas.txt           # Senhas salvas
         └── README.md            # Este arquivo





# Código Funcionando


Validação para apenas gerar senhas maiores que 6 caracteres 


<img width="800" height="450" alt="1" src="https://github.com/user-attachments/assets/426b965d-b115-435e-b0c2-b8ca1713b6c7" />




Gerando a senha e salvando a senha para o Clip Board



<img width="800" height="450" alt="2" src="https://github.com/user-attachments/assets/82a40acc-de1c-4596-881e-ee4e7f8bc012" />




Medindo a força da senha (segurança), de acordo com a quantidade de caracteres



<img width="800" height="450" alt="3" src="https://github.com/user-attachments/assets/fb1c41ea-fd58-4d2b-8334-fbc03198b952" />


