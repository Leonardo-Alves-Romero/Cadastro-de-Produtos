import pyautogui
from time import sleep
# 0 - registrar um novo usuário
pyautogui.click(987,611,duration=0.5)
# 0.1 - registrar nome novo usuário
pyautogui.click(1033,542,duration=0.5)
pyautogui.write('Leonardo')
# 0.2 - registrar senha novo usuário
pyautogui.click(1005,573,duration=0.5)
pyautogui.write('123456')
# 0.3 - registrar usuário
pyautogui.click(924,607,duration=0.5)
# 1 - cliacar e digitar meu usuário
pyautogui.click(1013,542,duration=0.5)
pyautogui.write('Leonardo')
# 2 - clicar e digitar minha senha
pyautogui.click(1006,573,duration=0.5)
pyautogui.write('123456')
# 3 - clicar em "entrar"
pyautogui.click(843,611,duration=0.5)
# 4 - extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #   1 - clicar e digitar produto
        pyautogui.click(610,526,duration=0.5)
        pyautogui.write(produto)
        #   2 - clicar e digitar quantidade
        pyautogui.click(608,559,duration=0.5)
        pyautogui.write(quantidade)
        #   3 - clicar e digitar preço
        pyautogui.click(603,592,duration=0.5)
        pyautogui.write(preco)
        #   4 - clicar em "registrar"
        pyautogui.click(506,786,duration=0.5)
        sleep(0.5)
