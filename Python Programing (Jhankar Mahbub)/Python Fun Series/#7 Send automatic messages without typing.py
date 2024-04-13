# Send automatic messages without typing
import pyautogui
import time
#message = 3
#while message > 0:
while True:
    time.sleep(4)
    pyautogui.typewrite('I need you.')
    time.sleep(2)
    pyautogui.press('enter')
    #message -= 1