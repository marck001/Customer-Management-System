#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from gui.sign_up.sign_upui import sign_upUI as RegisterUI
from gui.menu.main_menuui import MenuUI
from models.User import User
from tkinter import messagebox
from functions.utils import *
class loginUI:
    def __init__(self, master=None):
        # build ui
        self.frame = tk.Tk(master)
        self.frame.configure(height=700, relief="flat", background="#f5f5f5", width=1100)
        self.frame.overrideredirect("false")
        self.frame.resizable(True, True)
        self.lbl_titulo = ttk.Label(self.frame, name="lbl_titulo")
        self.lbl_titulo.configure(
            anchor="e",
            compound="center",
            cursor="bogosity",
            font="{times new roman} 36 {}",
            justify="center",
            padding=5,
            background="#f5f5f5",
            relief="flat",
            state="normal",
            text='Inicio de Sesion\n')
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.TButton",
                        background="#00ffff", 
                        foreground="black", 
                        font=("Roboto", 10, "bold")) 
        style.map("Custom.TButton", background=[("active", "#a0ffff"), ("!disabled", "#00ffff")]) 
        self.lbl_titulo.place(anchor="nw", x=540, y=60)
        self.lbl_usuario = ttk.Label(self.frame, name="lbl_usuario", background="#f5f5f5",)
        self.lbl_usuario.configure(font="{times} 16 {}", text='Usuario')
        self.lbl_usuario.place(anchor="nw", x=480, y=210)
        self.entry_usuario = ttk.Entry(self.frame, name="entry_usuario")
        self.entry_usuario.configure(width=60)
        self.entry_usuario.place(anchor="nw", height=40, x=480, y=280)
        self.lbl_contrasenia = ttk.Label(self.frame, name="lbl_contrasenia")
        self.lbl_contrasenia.configure(
            font="{times} 16 {}",
            relief="flat",
            background="#f5f5f5",
            text='Contraseña')
        self.lbl_contrasenia.place(anchor="nw", x=480, y=360)
        self.entry_contrasenia = ttk.Entry(
            self.frame, name="entry_contrasenia", show="*")
        self.entry_contrasenia.configure(width=60)
        self.entry_contrasenia.place(anchor="nw", height=40, x=480, y=430)
        self.btn_IniciarSesion = ttk.Button(
            self.frame, name="btn_iniciarsesion", command=self.login_action, style="Custom.TButton")
        self.btn_IniciarSesion.configure(
            compound="top",
            cursor="arrow",
            text='Iniciar Sesion',
            width=25)
        self.btn_IniciarSesion.place(anchor="nw", x=630, y=525)
        self.btn_Registrarse = ttk.Button(self.frame, name="btn_registrarse", command=self.open_register_window, style="Custom.TButton")
        self.btn_Registrarse.configure(text='   Registrarse   ', width=25)
        self.btn_Registrarse.place(anchor="nw", x=630, y=600)
        canvas4 = tk.Canvas(self.frame)
        canvas4.configure(background="#4ad5f7", height=1100, width=400)
        canvas4.place(anchor="nw", x=0, y=0)
        label7 = ttk.Label(self.frame)
        self.img_usuario3 = tk.PhotoImage(file="src/img/usuario3.png")
        label7.configure(
            background="#4ad5f7",
            compound="top",
            font="{Yu Gothic UI} 14 {}",
            image=self.img_usuario3,
            justify="center",
            text='©Derechos reservados ')
        label7.place(anchor="nw", x=20, y=150)

        # Main widget
        self.mainwindow = self.frame

    def center(self, event):
        wm_min = self.mainwindow.wm_minsize()
        wm_max = self.mainwindow.wm_maxsize()
        screen_w = self.mainwindow.winfo_screenwidth()
        screen_h = self.mainwindow.winfo_screenheight()
        """ `winfo_width` / `winfo_height` at this point return `geometry` size if set. """
        x_min = min(screen_w, wm_max[0],
                    max(self.main_w, wm_min[0],
                        self.mainwindow.winfo_width(),
                        self.mainwindow.winfo_reqwidth()))
        y_min = min(screen_h, wm_max[1],
                    max(self.main_h, wm_min[1],
                        self.mainwindow.winfo_height(),
                        self.mainwindow.winfo_reqheight()))
        x = screen_w - x_min
        y = screen_h - y_min
        self.mainwindow.geometry(f"{x_min}x{y_min}+{x // 2}+{y // 2}")
        self.mainwindow.unbind("<Map>", self.center_map)

    def open_register_window(self):
        self.mainwindow.destroy()
        RegisterUI()

    #login action event
    def login_action(self):

        username = self.entry_usuario.get()
        password1 = self.entry_contrasenia.get()

        if not username or not password1:
            messagebox.showwarning("Por favor ingresa tanto el usuario como la contraseña", self.mainwindow)
            return
        user_data = User.find_user(username) 
        if user_data:
           if decode_hash_function(password1, user_data.password):          
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.mainwindow.destroy()  
            MenuUI(user_name=username) 
           else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        else:
            messagebox.showerror("Error", "Usuario no registrado")


    def run(self, center=False):
        if center:
            """ If `width` and `height` are set for the main widget,
            this is the only time TK returns them. """
            self.main_w = self.mainwindow.winfo_reqwidth()
            self.main_h = self.mainwindow.winfo_reqheight()
            self.center_map = self.mainwindow.bind("<Map>", self.center)
        self.mainwindow.mainloop()

