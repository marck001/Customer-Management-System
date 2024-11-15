#!/usr/bin/python3
import tkinter as tk
import ttkbootstrap as ttk

class ProductSellingUI:
    def __init__(self, master=None):
        # Si se proporciona un master, se usa Toplevel para crear una ventana secundaria
        # Si no hay master, se toma el master por defecto y se inicia la ventana principal
        self.mainwindow = tk.Toplevel(master) if master else ttk.Window(themename="flatly")  
        self.mainwindow.title("Product Selling UI")
        self.mainwindow.geometry("800x700")  # Tamaño de la ventana

        # Configuración de Treeview
        self.tree_view = ttk.Treeview(self.mainwindow, bootstyle="primary", name="tree_view")
        self.tree_view.configure(
            cursor="arrow",
            selectmode="extended",
            show="headings",
            takefocus=True
        )

        # Columnas del Treeview
        self.tree_view_cols = ['col_name', 'col_product', 'col_category', 'col_price', 'col_date']
        self.tree_view_dcols = ['col_name', 'col_product', 'col_category', 'col_price', 'col_date']
        self.tree_view.configure(columns=self.tree_view_cols, displaycolumns=self.tree_view_dcols)

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

        # Etiqueta de texto
        self.lbl_text = ttk.Label(self.mainwindow, text='Registro ventas realizadas', bootstyle="info")
        self.lbl_text.place(anchor="nw", relx=0.38, rely=0.11, x=0, y=0)

        # Campo de entrada de código
        self.entry_code = ttk.Entry(self.mainwindow)
        self.entry_code.place(anchor="nw", relx=0.22, rely=0.23, x=0, y=0)

        # Botón de búsqueda
        button_search = ttk.Button(self.mainwindow, text='Buscar por Codigo', bootstyle="outline-primary")
        button_search.place(anchor="nw", relx=0.45, rely=0.23, x=0, y=0)

        # Etiqueta de código
        self.lbl_code = ttk.Label(self.mainwindow, text='Codigo Producto\n', bootstyle="secondary")
        self.lbl_code.place(anchor="nw", relx=0.07, rely=0.23, x=0, y=0)

    def run(self):
        self.mainwindow.mainloop()

# Solo creamos la ventana principal si no hay un master
if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    root.title("Main Application")
    app = ProductSellingUI(root)
    app.run()
