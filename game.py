import os
import tkinter
from tkinter import *
from tkinter import Tk, ttk
from PIL import ImageTk, Image

welcome_tk = Tk()


def welcome():
    # Welcome screen creation
    global welcome_tk
    welcome_tk.title("ABC magic")
    welcome_tk.resizable(False, False)

    # Icono de la ventana welcome
    image_path = "pictures/icon.ico"
    welcome_tk.iconbitmap(image_path)
    # Establecer la geometría de la ventana centrada
    welcome_tk.geometry(f"+{250}+{250}")

    # Contenedores ventana welcome
    frame_welcome = ttk.Frame(welcome_tk, padding=100)
    frame_welcome.pack(anchor="center")
    frame_buttons = ttk.Frame(welcome_tk, padding=30)
    frame_buttons.pack(anchor="s")

    # widgets ventana welcome
    ttk.Label(frame_welcome, text="Welcome!", font=("Courier", 75)).pack()
    ttk.Button(frame_buttons, text="Start", command=lambda: config()).grid(column=0, row=0)
    ttk.Button(frame_buttons, text="Exit", command=welcome_tk.destroy).grid(column=0, row=1)

    # Menu ventana welcome
    menubar = Menu(welcome_tk)
    messages = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Messages', menu=messages)
    messages.add_command(label="Add messages")
    messages.add_command(label="See messages")
    messages.add_command(label="Delete all messages")
    welcome_tk.config(menu=menubar)
    welcome_tk.mainloop()


def config():
    config_tk = tkinter.Toplevel()
    config_tk.title("Settings")
    config_tk.resizable(False, False)
    config_tk.geometry("500x250")
    config_tk.rowconfigure(0, weight=1)
    config_tk.columnconfigure(0, weight=1)

    # frames
    frame = tkinter.Frame(config_tk)
    frame.grid(row=0, column=0, padx=10, pady=10)
    frame_time = tkinter.Frame(frame)
    frame_time.grid(row=0)
    frame_scale = tkinter.Frame(frame)
    frame_scale.grid(row=1)
    frame_message = tkinter.Frame(frame)
    frame_message.grid(row=2)
    frame_start = tkinter.Frame(frame)
    frame_start.grid(row=3)

    # labels
    ttk.Label(frame_time, text="Time").pack(anchor="center")
    ttk.Label(frame_scale, text="Scale").pack(anchor="center")
    ttk.Label(frame_message, text="Active messages").pack(anchor="center")
    ttk.Button(frame_start, text="Play", command=lambda: game()).pack(anchor="center")

    config_tk.mainloop()


def game():
    # window
    game_tk = Tk()
    game_tk.geometry("1200x650")
    # game.attributes('-fullscreen', True)

    # frames
    frm_back = ttk.Frame(game_tk, padding=10)
    frm_back.pack(anchor="w")
    frm_center = ttk.Frame(game_tk, padding=10)
    frm_center.pack(anchor="center")
    # frm_pause = ttk.Frame(game, padding=10)
    # frm_pause.pack(anchor="se")

    # images
    img_path = os.getcwd() + "\\pictures\\"
    img_a = ImageTk.PhotoImage(Image.open(img_path + "Arb.png").resize((450, 450)))
    img_right = ImageTk.PhotoImage(Image.open(img_path + "right.png").resize((300, 100)))
    img_left = ImageTk.PhotoImage(Image.open(img_path + "left.png").resize((300, 100)))
    print("ruta img ", img_path)
    # etiquetas
    ttk.Label(frm_center, image=img_a).grid(row=0, column=1)
    ttk.Label(frm_center, image=img_right).grid(row=0, column=2)
    ttk.Label(frm_center, image=img_left).grid(row=0, column=0)
    ttk.Label(frm_center, text="subliminal message", font=("Courier", 30), foreground="red").grid(row=1, column=1)

    # botones
    ttk.Button(game_tk, text="  | |  ", padding=3).pack(anchor="se", side="bottom", pady=20, padx=20)
    ttk.Button(frm_back, text="Quit", command=game_tk.destroy).pack(anchor="n", side="top", pady=10, padx=10)

    # start
    game_tk.mainloop()

