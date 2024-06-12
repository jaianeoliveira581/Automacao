#importação da biblioteca
import pyautogui as auto
import time

#tempo que cada comando demora para executar
auto.PAUSE = 0.6


auto.press('win')

auto.write('chrome')
auto.press('enter')

auto.hotkey('alt', 'space')
auto.press('x')


auto.write('github.com')
auto.press('enter')

time.sleep(3)
auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')
