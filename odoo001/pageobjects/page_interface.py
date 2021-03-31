# -*- coding:utf8 -*-

#实时获取鼠标位置
import sys,os
import pyautogui

def mouse_keyboard():
    # try:
    #     while True:
    #         x, y = pyautogui.position()  # 返回鼠标坐标
    #         posStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print(posStr, end='')
    #         print('\b' * len(posStr), end='', flush=True)
    # except KeyboardInterrupt:
    #     print('\n')
    pyautogui.moveTo(645,777)
    pyautogui.click()
    pyautogui.write("F:\YXexcel\mc_detail.xlsx", interval=0.2)
    pyautogui.press('enter')
    pyautogui.press('enter')