# 🛠️ Automação de Cadastro de Produtos - Sistema Saipos

Este projeto automatiza o processo de cadastro de produtos no sistema Saipos, utilizando **Python**, **PyAutoGUI** e **Pandas**. Desenvolvido inicialmente para uma cafeteria durante uma experiência pessoal e profissional transformadora, o script tem como objetivo economizar tempo, evitar erros manuais e facilitar a rotina de pequenos negócios.

## 🚀 Contexto

Este script foi desenvolvido enquanto eu trabalhava na **Cafeteria Sr. Grão**, durante o ano de 2023. Enquanto estudava para o ENEM e economizava para me mudar, percebi uma oportunidade de aplicar programação para resolver um problema real: o cadastro repetitivo de produtos no sistema ERP da cafeteria. Hoje, curso **Sistemas de Informação na UFF - Niterói** e sigo em transição para a área de desenvolvimento.

## ✨ Funcionalidades

- Abertura automática do navegador e login no sistema Saipos
- Navegação até a tela de cadastro de produtos
- Leitura de planilha `.csv` com dados dos produtos
- Cadastro automatizado dos itens com vínculo ao fornecedor

## 🧰 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)

## 📁 Estrutura de Arquivos

- `produtosCadastro.csv` — Arquivo com a base de dados dos produtos a serem cadastrados
- `automacao_cadastro_saipos.py` — Script principal que executa a automação

## 📋 Requisitos

- Sistema operacional com interface gráfica (preferencialmente Windows)
- Google Chrome instalado
- Conta ativa na plataforma Saipos
- Instalar as bibliotecas necessárias com:

pip install pyautogui pandas
⚠️ Importante: o script utiliza coordenadas fixas da tela para clicar nos elementos. É necessário ajustar os valores de x e y conforme a resolução e layout da interface da sua máquina.

✅ Como usar
Abra o sistema Saipos manualmente e faça os testes de coordenadas com pyautogui.position() para ajustar os cliques.

Prepare um arquivo .csv com as colunas Item com Estoque e produto vinculado.

Execute o script:

bash
Copiar
Editar
python automacao_cadastro_saipos.py
💡 Aprendizados e Impacto
Este projeto foi um marco na minha trajetória — mostrou como a programação pode 
gerar valor prático em qualquer contexto. Automatizar um processo simples, mas repetitivo, 
permitiu que a equipe do Sr. Grão tivesse mais tempo para se concentrar no que realmente importa:
o atendimento ao cliente e a operação do negócio.
