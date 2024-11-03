#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class menuUI:
    def __init__(self, master=None):
        # build ui
        self.menu = tk.Tk(master)
        self.menu.configure(
            height=900,
            relief="flat",
            takefocus=True,
            width=1200)
        self.menu.overrideredirect("false")
        self.menu.resizable(True, False)
        self.menu.title("menu")
        self.canva1 = tk.Canvas(self.menu, name="canva1")
        self.canva1.configure(
            background="#45fcf8",
            confine=False,
            cursor="arrow",
            relief="flat",
            state="normal",
            takefocus=False,
            width=300)
        self.canva1.pack(anchor="sw", expand=True, fill="y", side="right")
        self.btn_menu2 = ttk.Button(self.menu, name="btn_menu2")
        self.btn_menu2.configure(
            compound="bottom",
            cursor="hand2",
            default="normal",
            state="normal",
            takefocus=False,
            text='Registrar Producto')
        self.btn_menu2.place(
            anchor="nw",
            height=50,
            relx=0.0,
            rely=0.37,
            width=300,
            x=0,
            y=0)
        self.btn_menu2.configure(command=self.on_window_products)
        self.btn_menu2.bind("<Button>", self.callback, add="+")
        self.btn_menu3 = ttk.Button(self.menu, name="btn_menu3")
        self.btn_menu3.configure(
            compound="left",
            cursor="hand2",
            default="active",
            state="normal",
            takefocus=False,
            text='Hacer compra')
        self.btn_menu3.place(
            anchor="nw",
            height=50,
            relx=0.0,
            rely=0.44,
            width=300,
            x=0,
            y=0)
        self.btn_menu3.configure(command=self.on_window_selling)
        self.btn_menu3.bind("<Button>", self.callback, add="+")
        self.btn_menu4 = ttk.Button(self.menu, name="btn_menu4")
        self.btn_menu4.configure(
            compound="left",
            cursor="hand2",
            default="active",
            state="normal",
            takefocus=False,
            text='Ver productos Comprados')
        self.btn_menu4.place(
            anchor="nw",
            height=50,
            relx=0.0,
            rely=0.51,
            width=300,
            x=0,
            y=0)
        self.btn_menu4.configure(command=self.on_window_sell_products)
        self.btn_menu4.bind("<Button>", self.callback, add="+")
        self.btn_menu5 = ttk.Button(self.menu, name="btn_menu5")
        self.btn_menu5.configure(
            cursor="hand2",
            default="active",
            state="normal",
            takefocus=False,
            text='Log out')
        self.btn_menu5.place(
            anchor="nw",
            height=50,
            relx=0.0,
            rely=0.58,
            width=300,
            x=0,
            y=0)
        self.btn_menu5.configure(command=self.on_window_logout)
        self.btn_menu5.bind("<Button>", self.callback, add="+")
        label2 = ttk.Label(self.menu)
        self.img_user_colored = tk.PhotoImage(file="src/img/user_colored.png")
        label2.configure(
            compound="none",
            font="TkDefaultFont",
            image=self.img_user_colored,
            justify="center",
            text='User\n')
        label2.place(x=59, y=40)
        self.btn_dispose = ttk.Button(self.menu, name="btn_dispose")
        self.btn_dispose.configure(
            cursor="hand2",
            default="active",
            state="normal",
            takefocus=False,
            text='Salir')
        self.btn_dispose.place(
            anchor="nw",
            height=50,
            relx=0.0,
            rely=0.65,
            width=300,
            x=0,
            y=0)
        self.btn_dispose.configure(command=self.on_window_dispose)
        self.btn_dispose.bind("<Button>", self.callback, add="+")
        self.menu.pack_propagate(0)

        # Main widget
        self.mainwindow = self.menu

    def run(self):
        self.mainwindow.mainloop()

    def on_window_products(self):
        pass

    def callback(self, event=None):
        pass

    def on_window_selling(self):
        pass

    def on_window_sell_products(self):
        pass

    def on_window_logout(self):
        pass

    def on_window_dispose(self):
        pass


if __name__ == "__main__":
    app = menuUI()
    app.run()
