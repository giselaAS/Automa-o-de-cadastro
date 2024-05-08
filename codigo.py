import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.press("tab")
pyautogui.write("gisasousa@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


tabela = pd.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:
    pyautogui.click(x=680, y=226)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna("obs"):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
