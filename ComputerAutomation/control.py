import pyautogui as auto
import time

# pyautogui.moveTo(x=500, y=500, duration=5)
#
# pyautogui.click(button='left', clicks=2, interval=0.5)

# pyautogui.hotkey('command', 'space')
#
# pyautogui.typewrite('Google Chrome')
#
# pyautogui.press('enter')

time.sleep(5)

answer = pyautogui.prompt(text='This is text', title='Hello', default='Carl')

print(answer)
