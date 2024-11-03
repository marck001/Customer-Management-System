#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class sign_upUI:
    def __init__(self, master=None):
        # build ui
        self.frame = tk.Tk(master)
        self.frame.configure(
            height=700,
            relief="raised",
            takefocus=True,
            width=1100)
        self.frame.overrideredirect("false")
        self.frame.resizable(True, False)
        self.lbl_titulo = ttk.Label(self.frame, name="lbl_titulo")
        self.lbl_titulo.configure(
            anchor="e",
            compound="center",
            cursor="bogosity",
            font="{times new roman} 36 {}",
            justify="center",
            padding=5,
            relief="flat",
            state="normal",
            text='Registro\n')
        self.lbl_titulo.place(anchor="nw", x=650, y=60)
        self.lbl_usuario = ttk.Label(self.frame, name="lbl_usuario")
        self.lbl_usuario.configure(font="{times} 16 {}", text='Usuario')
        self.lbl_usuario.place(anchor="nw", x=480, y=190)
        self.entry_usuario = ttk.Entry(self.frame, name="entry_usuario")
        self.entry_usuario.configure(width=60)
        self.entry_usuario.place(anchor="nw", height=40, x=480, y=240)
        self.lbl_contrasenia = ttk.Label(self.frame, name="lbl_contrasenia")
        self.lbl_contrasenia.configure(
            font="{times} 16 {}",
            relief="flat",
            text='Contraseña')
        self.lbl_contrasenia.place(anchor="nw", x=480, y=310)
        self.entry_contrasenia = ttk.Entry(
            self.frame, name="entry_contrasenia")
        self.entry_contrasenia.configure(width=60)
        self.entry_contrasenia.place(anchor="nw", height=40, x=480, y=380)
        self.btn_Registrarse = ttk.Button(self.frame, name="btn_registrarse")
        self.btn_Registrarse.configure(text='   Registrarse   ', width=25)
        self.btn_Registrarse.place(anchor="nw", x=630, y=585)
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
        self.lbl_correo = ttk.Label(self.frame, name="lbl_correo")
        self.lbl_correo.configure(
            font="{times} 16 {}",
            text='Correo Elecontronico')
        self.lbl_correo.place(anchor="nw", x=480, y=450)
        self.entry_correo = ttk.Entry(self.frame, name="entry_correo")
        self.entry_correo.configure(width=60)
        self.entry_correo.place(anchor="nw", height=40, x=480, y=510)
        self.btn_irInicio = ttk.Button(self.frame, name="btn_irinicio")
        self.btn_irInicio.configure(text='   Ir a Login   ', width=25)
        self.btn_irInicio.place(anchor="nw", x=630, y=635)

        # Main widget
        self.mainwindow = self.frame

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = sign_upUI()
    app.run()