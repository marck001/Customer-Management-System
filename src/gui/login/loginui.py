#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from gui.sign_up.sign_upui import sign_upUI as RegisterUI
from gui.menu.main_menuui import MenuUI
from models.User import User
from tkinter import messagebox
from functions.utils import *
import cv2
import face_recognition
import os
from gui.camera.camera import FaceRecognitionApp

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
        
        # Nuevo botón para logeo facial
        self.btn_FacialLogin = ttk.Button(
            self.frame, name="btn_faciallogin", command=self.facial_login_action, style="Custom.TButton")
        self.btn_FacialLogin.configure(
            text='Logeo Facial', width=25)
        self.btn_FacialLogin.place(anchor="nw", x=630, y=660)

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
        #FaceRecognitionApp(self.mainwindow)
        

    def open_register_window(self):
        self.mainwindow.destroy()
        RegisterUI()
        

    # Acción para logeo tradicional
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

    # Acción para logeo facial
    def facial_login_action(self):
        known_encodings = []
        known_usernames = []

        faces_dir = "src/img/faces"  
        for filename in os.listdir(faces_dir):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)[0]
                known_encodings.append(encoding)
                known_usernames.append(filename.split(".")[0])

        video_capture = cv2.VideoCapture(0)
        if not video_capture.isOpened():
            messagebox.showerror("Error", "No se pudo abrir la cámara")
            return

        success, frame = video_capture.read()
        if success:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_encodings, face_encoding)
                if True in matches:
                    matched_index = matches.index(True)
                    #aqui extraer nombre el archivo y ponerlo como username
                    user=User.find_user(matched_index)
                    if user:
                    #username = known_usernames[matched_index]
                     messagebox.showinfo("Éxito", f"Inicio de sesión exitoso: {user.username}")
                     self.mainwindow.destroy()
                     MenuUI(user_name=user.username)
                     video_capture.release()
                     return

            messagebox.showerror("Error", "No se reconoció el rostro.")
        else:
            messagebox.showerror("Error", "No se pudo capturar la imagen.")

        video_capture.release()

    def run(self):
        self.mainwindow.mainloop()
