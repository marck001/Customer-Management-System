#!/usr/bin/python3
import tkinter as tk
import ttkbootstrap as ttk

class ProductSellingUI:
    def __init__(self, master=None):
        # Initialize the main window
        self.mainwindow = ttk.Window(master) if master else ttk.Window(themename="flatly")  # Choose your preferred theme
        self.mainwindow.title("Product Selling UI")
        self.mainwindow.geometry("800x700")  # Set size of the window

        # Treeview setup
        self.tree_view = ttk.Treeview(self.mainwindow, bootstyle="primary", name="tree_view")
        self.tree_view.configure(
            cursor="arrow",
            selectmode="extended",
            show="headings",
            takefocus=True
        )
        
        # Define columns
        self.tree_view_cols = ['col_name', 'col_product', 'col_category', 'col_price']
        self.tree_view_dcols = ['col_name', 'col_product', 'col_category', 'col_price']
        self.tree_view.configure(columns=self.tree_view_cols, displaycolumns=self.tree_view_dcols)

        # Configure individual columns
        col_info = {
            "col_name": ("Usuario", 100),
            "col_product": ("Producto", 100),
            "col_category": ("Categoria", 100),
            "col_price": ("Precio", 100),
        }
        
        for col, (heading, width) in col_info.items():
            self.tree_view.column(col, anchor="w", stretch=True, width=width, minwidth=20)
            self.tree_view.heading(col, anchor="w", text=f"{heading}\n")

        self.tree_view.place(anchor="nw", height=400, relx=0.16, rely=0.32, width=500, x=0, y=0)

        # Label for title
        self.lbl_text = ttk.Label(self.mainwindow, text='Registro ventas realizadas', bootstyle="info")
        self.lbl_text.place(anchor="nw", relx=0.38, rely=0.11, x=0, y=0)

        # Entry for product code
        entry_code = ttk.Entry(self.mainwindow)
        entry_code.place(anchor="nw", relx=0.22, rely=0.23, x=0, y=0)

        # Search button
        button_search = ttk.Button(self.mainwindow, text='Buscar por Codigo', bootstyle="outline-primary")
        button_search.place(anchor="nw", relx=0.45, rely=0.23, x=0, y=0)

        # Label for entry
        self.lbl_code = ttk.Label(self.mainwindow, text='Codigo Producto\n', bootstyle="secondary")
        self.lbl_code.place(anchor="nw", relx=0.07, rely=0.23, x=0, y=0)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = ProductSellingUI()
    app.run()
