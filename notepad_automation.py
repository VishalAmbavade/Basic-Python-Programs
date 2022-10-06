import pyautogui
import time
import random
import string
from pywinauto.application import Application

def randomStringInNotepad():
    while True:
        N = random.randint(10, 100)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        app = Application().start("notepad.exe")
        app.UntitledNotepad.menu_select("Help->About Notepad")
        app.AboutNotepad.OK.click()
        for i in res:
            app.UntitledNotepad.Edit.type_keys(i, with_spaces = True)
            time.sleep(random.randint(0, 1))
        time.sleep(5)
        app.UntitledNotepad.menu_select("File->Exit")
        diag = app.window(title="Notepad")
        diag.type_keys('{RIGHT}')
        diag.type_keys('{ENTER}')

if __name__ == '__main__':
    randomStringInNotepad()