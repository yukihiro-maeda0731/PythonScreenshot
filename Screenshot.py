import pyautogui as pag
from time import sleep

i = 1
savepath = 'D:\portfolio\PythonScreenshot'

try:
    while True:
        img = pag.screenshot(savepath + '/screenshot' + str(i) + '.png')
        sleep(10)
        i = i + 1
except KeyboardInterrupt:
    print('\n')