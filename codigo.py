import pyautogui
import pandas as pd


pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')