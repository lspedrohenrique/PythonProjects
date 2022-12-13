import pyautogui

pyautogui.PAUSE = 2

pyautogui.click(x=500, y=900)

while(True):
    pyautogui.write("I love you")
    pyautogui.press("enter")

