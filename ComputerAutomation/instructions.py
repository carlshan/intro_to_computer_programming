import pyautogui
import pyperclip

# Here's how you get the width and height of your screen
width, height = pyautogui.size()

# Here's how you get the X and Y value of your mouse
mouse_x, mouse_y = pyautogui.position()


# Move your mouse to the top left corner of your screen to break out of
# PyAutoGui

# The below command will move your mouse to the X and Y coordinate you specify
# Note: your top left corner is (0, 0) and your bottom left corner is (width, height)
pyautogui.moveTo(100, 100)

# # This will click your mouse
pyautogui.click(button='left', clicks=2, interval=0.25)
## This will click your right mouse twice
pyautogui.doubleClick(button='right')

# This will slowly move your mouse to 500, 500 over the course of two seconds
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
pyautogui.click(button='left')
pyautogui.dragRel(30, 0, duration=2, button='left')

# This will press CMD + C (AKA copy)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')

# Here's how you get access to things that you copy
copied = pyperclip.paste()
print(copied)

# Here's how you type something. It'll type the text below with an interval of
# 0.1 seconds between letters.
pyautogui.typewrite("Yeah, I'm awesome.", interval=0.1)
