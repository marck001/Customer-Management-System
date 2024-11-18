#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from models.Selling import Selling
from tkinter import messagebox

class ProductSellingUI:
    def __init__(self, user_name, master=None):
        self.mainwindow = tk.Tk() if master is None else tk.Toplevel(master)
        self.mainwindow.title("Product Selling UI")
        self.mainwindow.geometry("800x700")
        self.user_name = user_name

  
        self.tree_view_cols = ['col_code', 'col_product', 'col_category', 'col_price', 'col_date']
        
        self.tree_view = ttk.Treeview(self.mainwindow, columns=self.tree_view_cols, name="tree_view", show="headings")
        self.tree_view.configure(cursor="arrow", selectmode="extended", takefocus=True)


        col_info = {
            "col_code": ("Codigo", 100),
            "col_product": ("Nombre Producto", 100),
            "col_category": ("Categoria", 100),
            "col_price": ("Monto", 100),
            "col_date": ("Fecha", 100),
        }


        for col, (heading, width) in col_info.items():
            self.tree_view.column(col, anchor="w", stretch=True, width=width, minwidth=20)
            self.tree_view.heading(col, anchor="w", text=f"{heading}\n")

       
        self.tree_view.place(anchor="nw", height=400, relx=0.16, rely=0.32, width=600, x=0, y=0)

        
        self.lbl_text = tk.Label(self.mainwindow, text="Registro ventas realizadas", bg="#e7f4f9", font=("Helvetica", 12))
        self.lbl_text.place(anchor="nw", relx=0.38, rely=0.11, x=0, y=0)


        self.entry_code = ttk.Entry(self.mainwindow)
        self.entry_code.place(anchor="nw", relx=0.22, rely=0.23, x=0, y=0)

   
        button_search = ttk.Button(self.mainwindow, text="Buscar",command=self.search_selling_by_code)
        button_search.place(anchor="nw", relx=0.45, rely=0.23, x=0, y=0)

        
        self.lbl_code = tk.Label(self.mainwindow, text="Codigo Venta", bg="#f0f0f0", font=("Helvetica", 10))
        self.lbl_code.place(anchor="nw", relx=0.07, rely=0.23, x=0, y=0)
        
        self.btnMostra = ttk.Button(self.mainwindow, name="btndisplay",command=self.list_by_date)
        self.img_Lista = tk.PhotoImage(file="src/img/Lista.gif")
        self.btnMostra.configure(
            cursor="arrow",
            image=self.img_Lista,
            takefocus=False,
            text='Por Fecha\n')
        self.btnMostra.place(anchor="nw", relx=0.84, rely=0.22, x=0, y=0)
        
        self.cbxFecha = DateEntry(
            self.mainwindow, 
            width=12, 
            date_pattern="yyyy-MM-dd"  
            )
        self.cbxFecha.place(
            anchor="nw",
            relx=0.65,
            rely=0.22,
            width=110
            )
        self.list_all()

    def run(self):
        self.mainwindow.mainloop()
        
    def list_all(self):
        sellings = Selling.list_all(user=self.user_name) 
        self.tree_view.delete(*self.tree_view.get_children()) 
        for sell in sellings:
            self.tree_view.insert("", "end", values=(
            sell.code,    
            sell.product_name,      
            sell.category,        
            sell.price,    
            sell.date      
        ))
    
    def search_selling_by_code(self):
        code = self.entry_code.get()
        selling = Selling.find_by_code(code)
        self.tree_view.delete(*self.tree_view.get_children())

        if selling:
            self.tree_view.insert("", "end", values=(
                selling.code,
                selling.product_name,
                selling.category,
                selling.price,
                selling.date
            ))
        else:
            messagebox.showerror("Error", "Producto no encontrado.",self.mainwindow)
        

        
    
    def list_by_date(self):
        
        user = self.user_name
        date = self.cbxFecha.get_date()
        date = date.strftime("%Y-%m-%d")
        
        sellings = Selling.list_by_user(user,date) 
        self.tree_view.delete(*self.tree_view.get_children()) 
        for sell in sellings:
            self.tree_view.insert("", "end", values=(
            sell.code,    
            sell.product_name,      
            sell.category,        
            sell.price,    
            sell.date      
        ))
    

