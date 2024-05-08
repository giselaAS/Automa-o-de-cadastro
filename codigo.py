import pyautogui
import pandas as pd

# abrir o brave
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
# abrir o site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# fazer o login no sistema
pyautogui.press("tab")
pyautogui.write("gisasousa@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
