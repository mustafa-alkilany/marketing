from tkinter import *

import instaloader

import os

root = Tk()

userName = ''


def instaUsername():
    global userName
    userName = EntryUsername.get()
    # print(userName)
    EntryUsername.delete(0, END)


Label(root, text="Enter Your username").pack()
EntryUsername = Entry(root, width=40)
EntryUsername.focus()
EntryUsername.pack()

enterEntryUsername = Button(root, text="ENTER", command=instaUsername)
enterEntryUsername.pack(fill=X)

password = ''


def instapassword():
    global password
    password = EntryPassword.get()
    # print(password)
    EntryPassword.delete(0, END)


Label(root, text="Enter password").pack()
EntryPassword = Entry(root, show="*", width=40)
EntryPassword.focus()
EntryPassword.pack()

enterEntryPassword = Button(root, text="ENTER", command=instapassword)
enterEntryPassword.pack(fill=X)

targetUsername = ''


def instaTargetUsername():
    global targetUsername
    targetUsername = targetEntryUsername.get()
    # print(targetUsername)
    targetEntryUsername.delete(0, END)


Label(root, text="target Username").pack()
targetEntryUsername = Entry(root, width=40)
targetEntryUsername.focus()
targetEntryUsername.pack()

targetEnterEntryUsername = Button(root, text="ENTER", command=instaTargetUsername)
targetEnterEntryUsername.pack(fill=X)

file_name = ''


def instaFileName():
    global file_name
    file_name = file_name_entry.get()
    # print(file_name)
    file_name_entry.delete(0, END)


Label(root, text="file name ( To add the users into )").pack()
file_name_entry = Entry(root, width=40)
file_name_entry.focus()
file_name_entry.pack()

file_name_enter_entry = Button(root, text="ENTER", command=instaFileName)
file_name_enter_entry.pack(fill=X)


def backToHome():
    root.destroy()
    main = os.system("python3 main.py")
    print(main)


theentry = Button(root, text="Start the program", command=root.destroy).pack()
print(type(theentry))
Button(root, text="BACK", command=backToHome).pack()
root.geometry("+750+400")
root.mainloop()


def followers():
    L = instaloader.Instaloader()

    L.login(userName, password)
    profile = instaloader.Profile.from_username(L.context, targetUsername)

    follow_list = []
    count = 0
    file = open(file_name, "a+")
    for followee in profile.get_followers():
        username = followee.username
        file.write(username + "\n")
        print("done one ")

    file.close()


followers()
