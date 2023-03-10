import time
import pyautogui

# while True:
#     time.sleep(2)
#     pyautogui.click(339,456, button='left',clicks=10, interval=0.1)
#     pyautogui.mouseUp()
#     pyautogui.mousedown()

print(pyautogui.position())
pyautogui.moveTo(x=335, y=448)
# pyautogui.click(x=335, y=448, clicks=10000, button='left')
pyautogui.mouseDown(button='left')
time.sleep(1)
pyautogui.mouseUp(button='left')