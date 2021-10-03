import keyboard, os, pyautogui, time
from tkinter import *

while True:
    try:
        if keyboard.is_pressed("m"):
            mouse_position_first = pyautogui.position()
            break
    except:
        break

root = Tk()

int_result = ''


def returnEntry(arg=None):
    global int_result
    result = myEntry.get()
    int_result = int(result)
    # print(int_result)
    myEntry.delete(0, END)


Label(root, text="Hi friend you need to setup the program first").pack()

Label(root, text="Enter how many numbers you have in the file").pack()
myEntry = Entry(root, width=40)
myEntry.focus()
myEntry.pack()

enterEntry = Button(root, text="Enter", command=returnEntry)
enterEntry.pack(fill=X)

twoResult = ''


def returnEntryTwo(arg=None):
    global twoResult
    twoResult = TwoEntry.get()
    # print(twoResult)
    TwoEntry.delete(0, END)


Label(root, text="Enter the file that have the numbers").pack()
TwoEntry = Entry(root, width=40)
TwoEntry.focus()
TwoEntry.pack()

TwoEnterEntry = Button(root, text="Enter", command=returnEntryTwo)
TwoEnterEntry.pack(fill=X)

threeResult = ''


def returnEntryThree(arg=None):
    global threeResult
    threeResult = threeEntry.get()
    # print(threeResult)
    threeEntry.delete(0, END)


Label(root, text="Enter the message file").pack()
threeEntry = Entry(root, width=40)
threeEntry.focus()
threeEntry.pack()

threeEnterEntry = Button(root, text="Enter", command=returnEntryThree)
threeEnterEntry.pack(fill=X)

Button(root, text="Start the program", command=root.destroy).pack()
root.geometry("+750+400")
root.mainloop()


def whatsapp():
    whatsapp_object_ = open(twoResult)
    pyautogui.press("win")
    time.sleep(0.4)
    pyautogui.typewrite(threeResult, 0.2)
    time.sleep(0.8)
    pyautogui.press("enter")
    time.sleep(0.7)
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("a")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")
    os.system("start timer/timer.exe")
    time.sleep(1)
    os.system("start chrome.exe")
    for _ in range(int_result):
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("l")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("l")
        pyautogui.typewrite(f"https://web.WhatsApp.com/send?phone={whatsapp_object_.readline()}", 0.1)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(14)
        pyautogui.click(mouse_position_first)
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("v")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("v")
        time.sleep(5)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
    whatsapp_object_.close()


whatsapp()
