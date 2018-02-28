import pyautogui
from googletrans import Translator
import time
import tkinter as tk

def main(repeat):
    """
    This function opens Google Chrome, types in Duolingo.com/practice and then
    copies the text, translates it and enters it.

    params:
        repeat : int
            Chooses the number of times to repeat solving DuoLingo exercises

    returns: None
    """
    awesomeDict={}

    root=tk.Tk()
    root.withdraw()
    c=root.clipboard_get()

    pyautogui.keyDown('command')

    pyautogui.press('space')

    pyautogui.keyUp('command')
    pyautogui.press(['g','o','o','g','l','e','space','c','h','r','o','m','e'])
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.keyDown('command')

    pyautogui.press('t')

    pyautogui.keyUp('command')

    pyautogui.press(['h','t','t','p','s',':','/','/','w','w','w','.','d','u','o','l','i','n','g','o','.','c','o','m','/','p','r','a','c','t','i','c','e'])
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(1100, 750)
    time.sleep(5)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    for g in range(0, repeat):
        pyautogui.moveTo(100, 325)
        pyautogui.dragTo(1000, 325, .05)
        pyautogui.keyDown('command')

        pyautogui.press('c')

        pyautogui.keyUp('command')
        pyautogui.dragTo(100, 325, .05)


        root=tk.Tk()
        root.withdraw()
        c=root.clipboard_get()



        c=c.replace('\n','')

        try:
            c = awesomeDict[c]
        except:

            translator = Translator()
            if (translator.translate(c, dest='en')).text==c:
                c = translator.translate(c, dest='es')

            else:
                c = translator.translate(c, dest='en')

        pyautogui.moveTo(700, 500)
        pyautogui.click()
        for i in c.text:
            pyautogui.press(i)
        pyautogui.press("1")
        pyautogui.press("backspace")
        pyautogui.moveTo(1100, 750)

        pyautogui.click()
        time.sleep(.5)
        pyautogui.moveTo(300, 750)
        pyautogui.dragTo(1200, 750, .05)
        pyautogui.keyDown('command')

        pyautogui.press('c')

        pyautogui.keyUp('command')
        pyautogui.moveTo(1100, 750)
        pyautogui.click()
        d=root.clipboard_get()
        d=d.replace('\n','')
        print(c.origin + d)
        if d != "You are correct":
            awesomeDict[c.origin]=d

main(8)
