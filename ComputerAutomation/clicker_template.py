import pyautogui
import pyperclip

# First, let's move to the make paperclip button
make_paperclip_x = 80
make_paperclip_y = 300
pyautogui.moveTo(make_paperclip_x, make_paperclip_y)

# Now let's click 100 times
# count = 0
# while count < 100:
#     pyautogui.click(button='left', clicks=1, interval=0.25)
#
#     count = count + 1


# How can we get the wire

# wire_x = 30
# wire_y = 570

# pyautogui.moveTo(50, 570)
pyautogui.click(button='left', clicks=1)
# pyautogui.dragRel(20, 0, duration=1)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')


copied = pyperclip.paste()
inches = copied[copied.find('Wire') + 5 : copied.find('inches')]
wire_left = int(inches)
