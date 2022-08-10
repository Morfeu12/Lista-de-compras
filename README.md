# Lista de compras - Python
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Morfeu12/Lista-de-compras/blob/main/LICENSE) 

## Sobre o projeto

A "Lista de compras" tem finalidade totalmente acadêmica para a prática da linguagem Python na sua versão 3.10 no que tange os conceitos básicos de programação. É uma aplicação de console que utiliza um arquivo TXT para manipular um dicionário (a lista de compras) possibilitando edições, remoções, pesquisas, inclusões e salvar todas as alterações realizadas.

### Layout Home
![Home menu de opções](https://github.com/Morfeu12/assets/blob/main/lc/lc1.png)


### Demonstração
Cadastro de produto (item) - Opção [1]

![Op1](https://github.com/Morfeu12/assets/blob/main/lc/lc2.png)

Remoção de produto (item) - Opção [3]

![Web 2](https://github.com/Morfeu12/assets/blob/main/lc/lc4.png)

Arquivo não encontrado ao salvar

![Web 2](https://github.com/Morfeu12/assets/blob/main/lc/lc5.png)![Web 2](https://github.com/Morfeu12/assets/blob/main/lc/lc6.png)


## Modelo conceitual
A estrutura foi baseada no modelo MVC (Model, View, Controller) em um contexto para aplicações de console. 

#### Model:
connect.py - Interações com o arquivo TXT (carregar, ler, editar e criar um arquivo TEMP_db caso não encontre o principal)
list_functions.py - Todas as funções (regras de negócio)

#### View:
controller_Interdace.py - Interações com o usuário. 

#### Controller: 
main.py - Fluxo principal e controlador das funcionalidades.


## Tecnologias utilizadas

Python 3.10.0.final.0

Venv 20.13.0

## Como executar o projeto

```bash
# Clonar repositório
$ git clone https://github.com/Morfeu12/Lista-de-compras

# Navegue até a pasta do projeto e inicie o arquivo main.py
$ python main.py 
ou
$ python3.10 main.py
```
![Op1](https://github.com/Morfeu12/assets/blob/main/lc/lcstart.png)

## Autor

Omar Costa

https://www.linkedin.com/in/omarcosta152/
