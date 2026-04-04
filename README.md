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
