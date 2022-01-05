from tkinter import *

import os
import time

def btn_clicked1():
    os.system(".\Processes\SpotifySetup.exe")

def btn_clicked2():
    os.system(".\Processes\spotiumroket.exe")

def btn_clicked3():
    os.system(".\Processes\spotiumuntime.exe")

def btn_clicked4():
    os.system(".\Processes\spotiumreplaceadminfile.exe")




window = Tk()
window.title('Spotium GUI')

window.geometry("883x486")
window.configure(bg = "#191919")
canvas = Canvas(
    window,
    bg = "#191919",
    height = 486,
    width = 883,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b0.place(
    x = 616, y = 130,
    width = 228,
    height = 60)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b1.place(
    x = 616, y = 367,
    width = 228,
    height = 60)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b2.place(
    x = 616, y = 274,
    width = 228,
    height = 60)


img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked4,
    relief = "flat")

b3.place(
    x = 608, y = 49,
    width = 250,
    height = 58)


background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    447.5, 234.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
