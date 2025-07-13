import pyautogui
import time
import pandas as pd

#1- ABERTURA DE NAVEGADOR E LOGIN
pyautogui.PAUSE = 1
pyautogui.press("Win")

pyautogui.write("Google Chrome")

pyautogui.press("Enter")
time.sleep(1)
pyautogui.write("https://conta.saipos.com/#/access/login")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(2)
pyautogui.write("EmailSaipos@teste.com")#Login
time.sleep(1)
pyautogui.press("TAB")
time.sleep(0.5)
pyautogui.write("InserirSenha")#Senha


pyautogui.click(x=1202, y=559)
time.sleep(3)
pyautogui.click(x=1487, y=321)
time.sleep(1.5)
pyautogui.click(x=29, y=109)
time.sleep(1)

#2- SELECAO DE ABA DE CADASTRO DE PRODUTOS
pyautogui.click(x=292, y=161)
time.sleep(1.5)
pyautogui.write("insumo")
time.sleep(1)
pyautogui.click(x=278, y=226)
pyautogui.click(x=50, y=177)
time.sleep(1)

#3- IMPORTAÇÃO DA BASE DE DADOS
tabelaProdutos = pd.read_csv("produtosCadastro.csv")
print(tabelaProdutos)
#4- CADASTRO DO PRIMERIO PRODUTO E VINCULO NA COMPRA
'''pyautogui.click(x=128,y=285)
pyautogui.write("Torta Oreo - Estoque")
pyautogui.click(x=635, y=278)
pyautogui.write("Unidade")
time.sleep(1)
pyautogui.click(x=938, y=634)
pyautogui.click(x=938, y=634)
pyautogui.click(x=588, y=628)
pyautogui.click(x=1593, y=280)
pyautogui.write("Fornecedores")
pyautogui.click(x=1588, y=318)
pyautogui.click(x=153, y=478)
pyautogui.write("Torta Oreo 22cm")
pyautogui.click(x=169, y=545)
pyautogui.click(x=1819, y=181)
#pyautogui.click(x=189, y=552)'''

pyautogui.click(x=128,y=285)
#5- LAÇO DE REPETIÇÃO PARA CADASTRO DOS DEMAIS PRODUTOS
for linha in tabelaProdutos.index:
    pyautogui.click(x=128,y=285)

    produto = tabelaProdutos.loc[linha,"Item com Estoque"]
    pyautogui.write(str(produto))
    pyautogui.click(x=635, y=278)
    pyautogui.write("Unidade")
    time.sleep(1)
    pyautogui.click(x=938, y=634)
    pyautogui.click(x=938, y=634)
    pyautogui.click(x=588, y=628)
    pyautogui.click(x=1593, y=280)
    pyautogui.write("Fornecedores")
    pyautogui.click(x=1588, y=318)
    pyautogui.click(x=153, y=478)

    produtoVinculado = tabelaProdutos.loc[linha,"produto vinculado"]
    pyautogui.write(str(produtoVinculado))
    pyautogui.click(x=169, y=545)
    pyautogui.click(x=1819, y=181)
    time.sleep(3)
    pyautogui.click(x=50, y=178)
