#!/usr/bin/python3
import tkinter as tk
import ttkbootstrap as ttk


class RegisterProductUI:
    def __init__(self, master=None):
        # Set up the main window using ttkbootstrap theme
        self.style = ttk.Style(theme="flatly")
        toplevel1 = self.style.master if master is None else tk.Toplevel(master)
        self.img_user_color = tk.PhotoImage(file="src/img/user_color.png")
        toplevel1.configure(
            background="#ffffff",
            height=700,
            highlightbackground="#64ddd1",
            width=700
        )
        toplevel1.iconphoto(True, self.img_user_color)
        toplevel1.resizable(True, True)
        toplevel1.title("Registro de Producto")

        # Canvas setup
        canvas3 = tk.Canvas(toplevel1)
        canvas3.configure(
            background="#f9f9f9",
            relief="flat",
            selectbackground="#c0c0c0",
            state="disabled"
        )
        canvas3.place(height=500, width=500, x=100, y=100)

        # Entries with ttkbootstrap styling
        self.txt_code = ttk.Entry(toplevel1, bootstyle="info")
        self.txt_code.place(anchor="nw", height=30, width=150, x=350, y=200)
        self.txt_name = ttk.Entry(toplevel1, bootstyle="info")
        self.txt_name.place(anchor="nw", height=30, width=150, x=350, y=250)
        self.spn_stock = ttk.Spinbox(toplevel1, bootstyle="info", increment=1)
        self.spn_stock.place(anchor="nw", height=30, width=150, x=350, y=350)
        self.txt_price = ttk.Entry(toplevel1, bootstyle="info")
        self.txt_price.place(anchor="nw", height=30, width=150, x=350, y=400)
        self.cbx_category = ttk.Combobox(toplevel1, bootstyle="info")
        self.cbx_category.place(anchor="nw", height=30, width=150, x=350, y=300)

        # Labels
        self.lbl_code = ttk.Label(toplevel1, text="Código:", background="#f9f9f9")
        self.lbl_code.place(anchor="nw", x=200, y=200)
        self.lbl_name = ttk.Label(toplevel1, text="Nombre:", background="#f9f9f9")
        self.lbl_name.place(anchor="nw", x=200, y=250)
        self.lbl_category = ttk.Label(toplevel1, text="Categoría:", background="#f9f9f9")
        self.lbl_category.place(anchor="nw", x=200, y=300)
        self.lbl_stock = ttk.Label(toplevel1, text="Stock:", background="#f9f9f9")
        self.lbl_stock.place(anchor="nw", x=200, y=350)
        self.lbl_price = ttk.Label(toplevel1, text="Precio:", background="#f9f9f9")
        self.lbl_price.place(anchor="nw", x=200, y=400)
        label8 = ttk.Label(toplevel1, text="Registro de Producto", background="#ffffff", font=("Helvetica", 16, "bold"))
        label8.place(anchor="nw", x=300, y=40)

        # Buttons with different ttkbootstrap styles
        self.btn_register = ttk.Button(toplevel1, text="Registrar", bootstyle="primary", command=self.on_btn_register)
        self.btn_register.place(anchor="e", x=400, y=500)
        
        self.btn_delete = ttk.Button(toplevel1, text="Eliminar", bootstyle="danger", command=self.on_btn_delete)
        self.btn_delete.place(anchor="e", x=500, y=500)
        
        self.btn_clear = ttk.Button(toplevel1, text="Limpiar", bootstyle="secondary", command=self.on_btn_clear)
        self.btn_clear.place(anchor="e", x=300, y=500)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def on_btn_register(self):
        pass  # Functionality for register button

    def on_btn_delete(self):
        pass  # Functionality for delete button

    def on_btn_clear(self):
        pass  # Functionality for clear button


if __name__ == "__main__":
    app = RegisterProductUI()
    app.run()
