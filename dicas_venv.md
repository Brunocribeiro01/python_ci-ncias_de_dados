# Manipulando Virtual Environment

## Definição
VEnv ou Virtural Envioronmente é equivalente a um container ou docker,
ou seja, um ambinente virtual dentro da máquina com bibliotecas ou 
ferramentas empecificas de um projeto.

## Dinamica de trabalho

1) Criar uma venv

python -m venv venv


2) ativar uma venv

Windows: c:\XXX>venv\Scripts\activate (nao pode ser no terminal powershel) (Usar o Command Prompt)
Unix:   source venv/bin/activate

3) instalar ou configurar tecnologia

python -m pip install pandas

4) depois de criar, instalar, atualizar configurar a venv, é necessário criar o arquivo
requirements.txt

python -m pip freeze > requirements.txt

5) toda vez que o repositorio  for clonado (usado pela primeira vez), é necessário:
    a)criar e ativar a venv
    b) instalar os pacotes que estão no arquivo requirements.txt

    python -m pip install -r requirements.txt


6) se for trocar de projeto ou repositório, lembre para desativar
deactivate