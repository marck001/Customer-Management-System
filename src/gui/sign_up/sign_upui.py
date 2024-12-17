#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from db.database import Database
from models.User import User
from gui.menu.main_menuui import MenuUI
import cv2
import face_recognition
import numpy as np
from gui.camera.camera import FaceRecognitionApp

class sign_upUI:
    def __init__(self, master=None):
        # build ui
        self.frame = tk.Tk(master)
        self.frame.configure(
            height=700,
            relief="raised",
            takefocus=True,
            background="#f5f5f5",
            width=1100)
        self.frame.resizable(True, False)
        
        # Variables
        self.face_encoding = None

        # Títulos y entradas
        self.lbl_titulo = ttk.Label(self.frame, text="Registro\n", font="{times new roman} 36 {}", background="#f5f5f5")
        self.lbl_titulo.place(x=650, y=60)
        self.lbl_usuario = ttk.Label(self.frame, text="Usuario", font="{times} 16 {}", background="#f5f5f5")
        self.lbl_usuario.place(x=480, y=190)
        self.entry_usuario = ttk.Entry(self.frame, width=60)
        self.entry_usuario.place(x=480, y=240, height=40)

        self.lbl_contrasenia = ttk.Label(self.frame, text="Contraseña", font="{times} 16 {}", background="#f5f5f5")
        self.lbl_contrasenia.place(x=480, y=310)
        self.entry_contrasenia = ttk.Entry(self.frame, width=60, show="*")
        self.entry_contrasenia.place(x=480, y=380, height=40)

        self.lbl_correo = ttk.Label(self.frame, text="Correo Electrónico", font="{times} 16 {}", background="#f5f5f5")
        self.lbl_correo.place(x=480, y=450)
        self.entry_correo = ttk.Entry(self.frame, width=60)
        self.entry_correo.place(x=480, y=510, height=40)

        # Botones
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.TButton",
                        background="#00ffff", 
                        foreground="black", 
                        font=("Roboto", 10, "bold"))
        self.btn_reconocer = ttk.Button(self.frame, text="Reconocimiento Facial", command=self.capture_face, style="Custom.TButton")
        self.btn_reconocer.place(x=480, y=570, width=250)

        self.btn_registrarse = ttk.Button(self.frame, text="Registrarse", command=self.register_user, style="Custom.TButton")
        self.btn_registrarse.place(x=740, y=570, width=250)

        self.btn_irInicio = ttk.Button(self.frame, text="Ir a Login", command=self.go_to_login_window, style="Custom.TButton")
        self.btn_irInicio.place(x=610, y=635, width=250)

        self.mainwindow = self.frame
        FaceRecognitionApp(self.mainwindow)

    def capture_face(self):
       
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "No se puede abrir la cámara.")
            return

        messagebox.showinfo("Instrucción", "Mire hacia la cámara. Se capturará su rostro.")
        face_encoding = None

        while True:
            ret, frame = cap.read()
            if not ret:
                break

        
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

          
            face_locations = face_recognition.face_locations(rgb_frame)
            if face_locations:
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                if face_encodings:
                    face_encoding = face_encodings[0]
                 
                    username = self.entry_usuario .get().strip()
                if username:
                        image_path = f"src/img/faces/{username}.jpg"
                        cv2.imwrite(image_path, frame)  # Guardar la imagen original
                        print(f"Imagen capturada y guardada como {image_path}")
                        break
                else:
                        messagebox.showerror("Error", "El nombre de usuario no puede estar vacío.")
                        break

          
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()

        if face_encoding is not None:
            self.face_encoding = face_encoding.tolist()
            messagebox.showinfo("Éxito", "Rostro capturado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo capturar el rostro. Intente de nuevo.")

    def register_user(self):
      
        username = self.entry_usuario.get()
        password = self.entry_contrasenia.get()
        email = self.entry_correo.get()

        if not username or not password or not email:
            messagebox.showerror("Error", "Llene los campos de texto.")
            return
        if self.face_encoding is None:
            messagebox.showerror("Error", "Por favor capture su rostro primero.")
            return

        try:
            # Guardar el usuario en la base de datos con el encoding facial
            if User.insert(username, email, password):
                self.mainwindow.destroy()
                MenuUI(user_name=username)
                messagebox.showinfo("Éxito", "Usuario registrado correctamente. Iniciando sesión.")
            else:
                messagebox.showerror("Error", "Nombre de usuario ya se encuentra registrado.")
        except Exception as e:
            messagebox.showerror("Error de registro", f"Ocurrió un error: {e}")

    def go_to_login_window(self):
        from gui.login.loginui import loginUI
        self.mainwindow.destroy()
        loginUI()

    def run(self):
        self.mainwindow.mainloop()
      


if __name__ == "__main__":
    app = sign_upUI()
    app.run()
