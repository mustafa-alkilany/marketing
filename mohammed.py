import os, time, pyautogui, keyboard, pyperclip, instaloader
from getpass import getpass


def whatsapp():
    print("Hi friend you need to setup the program first ")
    time.sleep(0.3)
    print("https://youtube.com/mustafa-alkilany")
    print("in this video you will see how to setup the program for whatsapp only :) open it !!")
    while True:
        try:
            if keyboard.is_pressed("m"):
                mouse_position_first = pyautogui.position()
                break
        except:
            break

    whatsapp_range = int(input("Enter how many numbers you have in the file: "))
    whatsapp_file = input("Enter the file that have the numbers: ")
    whatsapp_message = input("Enter the message file: ")
    whatsapp_object_ = open(whatsapp_file)
    # pyautogui.hotkey("alt", "shift")
    # os.system(f"start {whatsapp_message}")
    pyautogui.press("win")
    pyautogui.typewrite(whatsapp_message, 0.2)
    # pyperclip.copy(whatsapp_message)
    time.sleep(0.8)
    pyautogui.press("enter")
    time.sleep(0.7)
    # pyautogui.keyDown('alt')
    # pyautogui.keyDown('tab')
    # pyautogui.keyUp('alt')
    # pyautogui.keyUp('tab')
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("a")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")
    os.system("start timer/timer.exe")
    # pyautogui.press("win")
    # pyautogui.typewrite("chrome.exe", 0.2)
    # pyautogui.press("enter")
    time.sleep(1)
    os.system("start chrome.exe")
    for _ in range(whatsapp_range):
        # os.system(f"start chrome.exe https://web.WhatsApp.com/send?phone={whatsapp_object_.readline()}")
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
        #pyautogui.hotkey("alt", "shift")
        # pyautogui.typewrite(whatsapp_message)
        time.sleep(5)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
    whatsapp_object_.close()
 

def Instagram():
    print("[ 01 ] Instagram sender""         ""[ 02 ] Get someone followers")
    main_instagram__input = input("Enter your choice >>> ")
    if main_instagram__input == "1" or main_instagram__input == "01":
        print("[ 01 ] 1 account ""           ""[ 02 ] 10 accounts")
        main2_instagram_input = input("Enter your choice >>> ")
        if main2_instagram_input == "1" or main2_instagram_input == "01":
            pass
        elif main2_instagram_input == "2" or main2_instagram_input == "02":
            insta10()
    elif main_instagram__input == "2" or main_instagram__input == "02":
        def followers():
            L = instaloader.Instaloader()

            acc_username = input("Username: ")
            password = getpass()
            target = input("Target username: ")
            print("file name to save the users into ")
            file_username = input("file name: ")

            L.login(acc_username, password)
            profile = instaloader.Profile.from_username(L.context, target)

            follow_list = []
            count = 0
            file = open(file_username, "a+")
            for followee in profile.get_followers():
                username = followee.username
                file.write(username + "\n")
                print("done one ")

            file.close()
        followers()
        __markting__()
    print("Hi friend you need to setup the program first ")
    time.sleep(0.3)
    print("https://youtube.com/mustafa-alkilany")
    print("in this video you will see how to setup the program for instagram only :) open it !!")
    while True:
        try:
            if keyboard.is_pressed("m"):
                instgram_key__ = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("u"):
                instgram_key_two__ = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("s"):
                instgram_key_three__ = pyautogui.position()
                break
        except:
            break

    Instagram_range = int(input("how many ids you have : "))
    Instagram_file = input("file that have the ids : ")
    Instagram_message = input("Enter message file: ")
    Instagram_object = open(Instagram_file)
    pyautogui.press("win")
    pyautogui.typewrite(Instagram_message, 0.2)
    time.sleep(0.8)
    pyautogui.press("enter")
    time.sleep(0.7)
    # os.system(f"start {Instagram_message}")
    # pyautogui.keyDown('alt')
    # pyautogui.keyDown('tab')
    # pyautogui.keyUp('alt')
    # pyautogui.keyUp('tab')
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("a")
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("a")
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("c")
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("c")
    # pyautogui.hotkey("alt", "shift")
    # pyperclip.copy(Instagram_message)
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("a")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")
    os.system("start timer/timer2.exe")
    # pyautogui.typewrite("chrome.exe", 0.2)
    time.sleep(1)
    os.system("start chrome.exe")
    for _ in range(Instagram_range):
        time.sleep(1)
        pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
        pyautogui.press("enter")
        time.sleep(10)
        pyautogui.typewrite(Instagram_object.readline(), 0.1)
        time.sleep(8)
        pyautogui.click(instgram_key__)
        pyautogui.click(instgram_key_two__)
        time.sleep(5)
        pyautogui.click(instgram_key_three__)
        time.sleep(7)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(7)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        pyautogui.hotkey("ctrl", "l")
    Instagram_object.close()

def insta10():
    print("Hi friend you need to setup the program first ")
    time.sleep(0.3)
    print("https://youtube.com/mustafa-alkilany")
    print("in this video you will see how to setup the program for instagram only :) open it !!")
    while True:
        try:
            if keyboard.is_pressed("m"):
                instgram_key__ = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("u"):
                instgram_key_two__ = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("s"):
                instgram_key_three__ = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("t"):
                instagram_key_acc = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("a"):
                instagram_key_acc2 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("f"):
                instagram_key_acc3 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("a"):
                instagram_key_acc4 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("1"):
                instagram_key_acc5 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("2"):
                instagram_key_acc6 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("3"):
                instagram_key_acc7 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("4"):
                instagram_key_acc8 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("5"):
                instagram_key_acc9 = pyautogui.position()
                break
        except:
            break
    while True:
        try:
            if keyboard.is_pressed("6"):
                instagram_key_acc10 = pyautogui.position()
                break
        except:
            break

    Instagram_range = int(input("how many ids you have : "))
    Instagram_file = input("file that have the ids : ")
    Instagram_message = input("Enter message file: ")
    Instagram_object = open(Instagram_file)
    pyautogui.press("win")
    pyautogui.typewrite(Instagram_message, 0.2)
    time.sleep(0.8)
    pyautogui.press("enter")
    time.sleep(0.7)
    # os.system(f"start {Instagram_message}")
    # pyautogui.keyDown('alt')
    # pyautogui.keyDown('tab')
    # pyautogui.keyUp('alt')
    # pyautogui.keyUp('tab')
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("a")
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("a")
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("c")
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("c")
    # pyautogui.hotkey("alt", "shift")
    # pyperclip.copy(Instagram_message)
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("a")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("a")
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("c")
    os.system("start timer/timer2.exe")
    # pyautogui.typewrite("chrome.exe", 0.2)
    time.sleep(1)
    os.system("start chrome.exe")
    if Instagram_range == 200:
        for _ in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc3)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc4)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc5)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc6)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc7)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc8)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc8)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc9)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
        for i in range(20):
            time.sleep(1)
            pyautogui.typewrite(f"instagram.com", 0.1)
            pyautogui.press("enter")
            time.sleep(4)
            # pyautogui.click(instagram_key_acc4)
            time.sleep(0.4)
            pyautogui.click(instagram_key_acc)
            time.sleep(0.2)
            pyautogui.click(instagram_key_acc2)
            time.sleep(0.3)
            pyautogui.click(instagram_key_acc10)
            time.sleep(4)
            pyautogui.hotkey("ctrl", "l")
            time.sleep(0.3)
            pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
            pyautogui.press("enter")
            time.sleep(10)
            pyautogui.typewrite(Instagram_object.readline(), 0.1)
            time.sleep(8)
            pyautogui.click(instgram_key__)
            pyautogui.click(instgram_key_two__)
            time.sleep(5)
            pyautogui.click(instgram_key_three__)
            time.sleep(7)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(7)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            pyautogui.hotkey("ctrl", "l")
    Instagram_object.close()



def __markting__():
    print("[1] Whatsapp""   ""[2] Instagram")
    markting = input("Enter the social that you want >>> ")
    if markting == '1':
        def whatsapp__web():
            whatsapp_web = input(" do you want to sign into whatsapp web y or n >>> ")
            if whatsapp_web == 'n':
                pass
            elif whatsapp_web == 'y':
                os.system("start chrome.exe web.whatsapp.com")
            else:
                whatsapp__web()

        whatsapp__web()

        def __whatsapp_photo__():
            whatsapp_want_photo = input("do you want to add a photo? y or n ")
            if whatsapp_want_photo == 'y':
                print("Hi friend you need to setup the program first ")
                time.sleep(0.3)
                print("https://youtube.com/mustafa-alkilany")
                print("in this video you will see how to setup the program for whatsapp only :) open it !!")
                while True:
                    try:
                        if keyboard.is_pressed("m"):
                            mouse_position_second = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("u"):
                            mouse_position_three = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("s"):
                            mouse_position_forth = pyautogui.position()
                            break
                    except:
                        break

                whatsapp_photo = input("photo location : ")
                whatsapp_photo_ = input("photo name : ")
                whatsapp_photo_range = int(input("how many numbers you have ? "))
                whatsapp_photo_file = input("file name that have the numbers: ")
                whatsapp_photo_object = open(whatsapp_photo_file)
                whatsapp_message_photo = input("Enter the message: ")
                pyautogui.press("win")
                pyautogui.typewrite(whatsapp_message_photo, 0.2)
                time.sleep(0.8)
                pyautogui.press("enter")
                time.sleep(0.7)
                # os.system(f"start {whatsapp_message_photo}")
                # pyautogui.press("win")
                # pyautogui.typewrite(whatsapp_message_photo)
                # time.sleep(0.8)
                # pyautogui.press("enter")
                # time.sleep(0.7)
                # pyautogui.hotkey("alt", "shift")
                # pyperclip.copy(whatsapp_message_photo)
                # pyautogui.keyDown('alt')
                # pyautogui.keyDown('tab')
                # pyautogui.keyUp('alt')
                # pyautogui.keyUp('tab')
                # pyautogui.keyDown("ctrl")
                # pyautogui.keyDown("a")
                # pyautogui.keyUp("ctrl")
                # pyautogui.keyUp("a")
                # pyautogui.keyDown("ctrl")
                # pyautogui.keyDown("c")
                # pyautogui.keyUp("ctrl")
                # pyautogui.keyUp("c")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("a")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("a")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("c")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("c")
                os.system("start timer/timer3.exe")
                # pyautogui.typewrite("chrome.exe")
                time.sleep(1)
                os.system("start chrome.exe")
                for _ in range(whatsapp_photo_range):
                    # os.system(f"start chrome.exe https://web.WhatsApp.com/send?phone={whatsapp_photo_object.readline()}")
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("l")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("l")
                    pyautogui.typewrite(f"https://web.WhatsApp.com/send?phone={whatsapp_photo_object.readline()}", 0.1)
                    pyautogui.press("enter")
                    pyautogui.press("enter")
                    time.sleep(14)
                    pyautogui.click(mouse_position_second)
                    pyautogui.click(mouse_position_three)
                    time.sleep(5)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("l")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("l")
                    pyautogui.typewrite(whatsapp_photo, 0.1)
                    time.sleep(0.4)
                    pyautogui.press("enter")
                    time.sleep(4)
                    pyautogui.click(mouse_position_forth)
                    time.sleep(0.5)
                    pyautogui.typewrite(whatsapp_photo_)
                    time.sleep(0.4)
                    pyautogui.keyDown("enter")
                    pyautogui.keyUp("enter")
                    time.sleep(5)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("v")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("v")
                    time.sleep(5)
                    pyautogui.keyDown("enter")
                    pyautogui.keyUp("enter")
            elif whatsapp_want_photo == 'n':
                whatsapp()
            else:
                print("pleas Enter y or n")
                __whatsapp_photo__()
        __whatsapp_photo__()
        os.system("cls")
        __markting__()

        whatsapp()
    elif markting == '2':
        def Instagram_photo():
            # __markting__()
            want_instagram_photo = input("do you want to add a photo? y or n ")
            if want_instagram_photo == 'y':
                print("Hi friend you need to setup the program first ")
                time.sleep(0.3)
                print("https://youtube.com/mustafa-alkilany")
                print("in this video you will see how to setup the program for instagram only :) open it !!")
                while True:
                    try:
                        if keyboard.is_pressed("m"):
                            instgram_key = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("u"):
                            instgram_key_two = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("s"):
                            instgram_key_three = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("t"):
                            instagram_key__ = pyautogui.position()
                            break
                    except:
                        break
                while True:
                    try:
                        if keyboard.is_pressed("a"):
                            instagram_key___ = pyautogui.position()
                            break
                    except:
                        break
                Instagram_photo = input("photo location : ")
                Instagram_photo_ = input("photo name : ")
                Instagram_photo_range = int(input("how many ids you have ? "))
                Instagram_photo_file = input("file that have ids: ")
                Instagram_photo_object = open(Instagram_photo_file)
                Instagram_message_photo  = input("Enter the message : ")
                pyautogui.press("win")
                pyautogui.typewrite(Instagram_message_photo, 0.2)
                time.sleep(0.8)
                pyautogui.press("enter")
                time.sleep(0.7)
                # os.system(f"start {Instagram_message_photo}")
                # pyautogui.keyDown('alt')
                # pyautogui.keyDown('tab')
                # pyautogui.keyUp('alt')
                # pyautogui.keyUp('tab')
                # pyautogui.keyDown("ctrl")
                # pyautogui.keyDown("a")
                # pyautogui.keyUp("ctrl")
                # pyautogui.keyUp("a")
                # pyautogui.keyDown("ctrl")
                # pyautogui.keyDown("c")
                # pyautogui.keyUp("ctrl")
                # pyautogui.keyUp("c")
                # pyautogui.hotkey("alt", "shift")
                # pyperclip.copy(Instagram_message_photo)
                # os.system("start chrome.exe")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("a")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("a")
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("c")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("c")
                os.system("start timer/timer4.exe")
                # pyautogui.typewrite("chrome.exe")
                time.sleep(1)
                os.system("start chrome.exe")
                for _ in range(Instagram_photo_range):
                    time.sleep(0.6)
                    pyautogui.typewrite(f"https://www.instagram.com/direct/new", 0.1)
                    pyautogui.press("enter")
                    time.sleep(10)
                    pyautogui.typewrite(Instagram_photo_object.readline())
                    time.sleep(8)
                    pyautogui.click(instgram_key)
                    pyautogui.click(instgram_key_two)
                    time.sleep(5)
                    pyautogui.click(instgram_key_three)
                    time.sleep(4)
                    # pyautogui.typewrite(Instagram_photo, 0.1)
                    # pyautogui.keyDown("ctrl")
                    # pyautogui.keyDown("l")
                    # pyautogui.keyUp("ctrl")
                    # pyautogui.keyUp("l")
                    # time.sleep(0.5)
                    pyautogui.press("enter")
                    pyautogui.click(instagram_key__)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("l")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("l")
                    time.sleep(0.2)
                    pyautogui.typewrite(Instagram_photo, 0.1)
                    time.sleep(0.2)
                    pyautogui.click(instagram_key___)
                    time.sleep(0.2)
                    pyautogui.typewrite(Instagram_photo_, 0.1)
                    pyautogui.keyDown("enter")
                    pyautogui.keyUp("enter")
                    time.sleep(1)
                    pyautogui.keyDown("ctrl")
                    pyautogui.keyDown("v")
                    pyautogui.keyUp("ctrl")
                    pyautogui.keyUp("v")
                    time.sleep(7)
                    pyautogui.keyDown('enter')
                    pyautogui.keyUp('enter')
                    pyautogui.hotkey("ctrl", "l")
            elif want_instagram_photo == 'n':
                Instagram()
            else:
                print('pleas Enter y or n')
        Instagram_photo()
        os.system("cls")
        __markting__()

        # Instagram_photo()
    # elif markting == '3':
    #     def __facebook_want_photo_():
    #         facebook_want_photo = input("do you want a photo ? y or n  ")
    #         if facebook_want_photo == 'y':
    #             facebook_photo_path = input("Enter the path of the photo: ")
    #             facebook_photo_name = input("Enter the name of the photo: ")
    #             facebook_photo_range = int(input("Enter how many names you have in the file: "))
    #             facebook_photo_file = input("Enter the file that have names: ")
    #             facebook_photo_message = input("Enter the file that have message: ")
    #             facebook_photo_object = open(facebook_photo_file)
    #             os.system(f"start {facebook_photo_message}")
    #             pyautogui.keyDown("alt")
    #             pyautogui.keyDown("tab")
    #             pyautogui.keyUp("alt")
    #             pyautogui.keyUp("tab")
    #             pyautogui.keyDown("ctrl")
    #             pyautogui.keyDown("a")
    #             pyautogui.keyUp("ctrl")
    #             pyautogui.keyUp("a")
    #             pyautogui.keyDown("ctrl")
    #             pyautogui.keyDown("c")
    #             pyautogui.keyUp("ctrl")
    #             pyautogui.keyUp("c")
    #             for _ in range(facebook_photo_range):
    #                 os.system(f"start https://www.messenger.com/")
    #                 time.sleep(10)
    #                 pyautogui.click(x=1788, y=200)
    #                 pyautogui.typewrite(facebook_photo_object.readline())
    #                 time.sleep(8)
    #                 pyautogui.click(x=1136, y=1011)
    #                 time.sleep(5)
    #                 pyautogui.click(x=1492, y=1004)
    #                 time.sleep(0.5)
    #                 pyautogui.keyDown("ctrl")
    #                 pyautogui.keyDown("l")
    #                 pyautogui.typewrite(facebook_photo_path)
    #                 time.sleep(1)
    #                 pyautogui.click(x=377, y=477)
    #                 pyautogui.typewrite(facebook_photo_name)
    #                 time.sleep(1)
    #                 pyautogui.keyDown("enter")
    #                 pyautogui.keyUp("enter")
    #                 time.sleep(1)
    #                 pyautogui.keyDown("ctrl")
    #                 pyautogui.keyDown("v")
    #                 pyautogui.keyUp("ctrl")
    #                 pyautogui.keyUp("v")
    #                 time.sleep(5)
    #                 pyautogui.keyDown("enter")
    #                 pyautogui.keyUp("enter")
    #         elif facebook_want_photo == 'n':
    #             facebook()
    #         else:
    #             print("y or n")
    #             __facebook_want_photo_()
    #     __facebook_want_photo_()

    else:
        print("pleas Enter 1 or 2 ")
        time.sleep(0.3)
        __markting__()


__markting__()

exit()
