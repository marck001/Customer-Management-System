#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk


class ProductSellingUI:
    def __init__(self, master=None):
        self.mainwindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.mainwindow.title("Product Selling UI")
        self.mainwindow.geometry("800x700")

  
        self.tree_view_cols = ['col_name', 'col_product', 'col_category', 'col_price', 'col_date']
        
        self.tree_view = ttk.Treeview(self.mainwindow, columns=self.tree_view_cols, name="tree_view", show="headings")
        self.tree_view.configure(cursor="arrow", selectmode="extended", takefocus=True)


        col_info = {
            "col_name": ("Usuario", 100),
            "col_product": ("Producto", 100),
            "col_category": ("Categoria", 100),
            "col_price": ("Precio", 100),
            "col_date": ("Fecha", 100),
        }


        for col, (heading, width) in col_info.items():
            self.tree_view.column(col, anchor="w", stretch=True, width=width, minwidth=20)
            self.tree_view.heading(col, anchor="w", text=f"{heading}\n")

       
        self.tree_view.place(anchor="nw", height=400, relx=0.16, rely=0.32, width=600, x=0, y=0)

        
        self.lbl_text = tk.Label(self.mainwindow, text="Registro ventas realizadas", bg="#e7f4f9", font=("Helvetica", 12))
        self.lbl_text.place(anchor="nw", relx=0.38, rely=0.11, x=0, y=0)


        entry_code = ttk.Entry(self.mainwindow)
        entry_code.place(anchor="nw", relx=0.22, rely=0.23, x=0, y=0)

   
        button_search = ttk.Button(self.mainwindow, text="Buscar")
        button_search.place(anchor="nw", relx=0.45, rely=0.23, x=0, y=0)

        
        self.lbl_code = tk.Label(self.mainwindow, text="Cliente", bg="#f0f0f0", font=("Helvetica", 10))
        self.lbl_code.place(anchor="nw", relx=0.07, rely=0.23, x=0, y=0)

    def run(self):
        self.mainwindow.mainloop()

