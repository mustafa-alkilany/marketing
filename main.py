from tkinter import *

root = Tk()

Label(root, text="Chose one").pack()


def whatsapp():
    root.destroy()
    import whatsappGui
    print(whatsappGui)


whatsappEntry = Button(root, text="WHATSAPP", command=whatsapp)
whatsappEntry.pack(fill=X)


def instagram():
    root.destroy()
    import instagramGui
    print(instagramGui)


instagramEntry = Button(root, text="INSTAGRAM", command=instagram)
instagramEntry.pack(fill=X)

root.geometry("+750+400")
root.mainloop()
