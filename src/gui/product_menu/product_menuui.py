#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox
from tkcalendar import DateEntry
from models.Selling import Selling
from models.Product import Product
class product_menuUI:
    def __init__(self, master=None):
        # build ui
        self.productMenu = tk.Tk() if master is None else tk.Toplevel(master)
        self.productMenu.configure(
            cursor="arrow",
            height=200,
            relief="raised",
            width=200)
        self.productMenu.geometry("969x689")
        self.tablaVentas = ttk.Treeview(self.productMenu, name="tablaventas")
        self.tablaVentas.configure(
            height=5,
            selectmode="extended",
            show="headings")
        self.tablaVentas_cols = [
            'columnCodigo',
            'columnProducto',
            'columnStock',
            'columnCategoria',
            'columnPrecio']
        self.tablaVentas_dcols = [
            'columnCodigo',
            'columnProducto',
            'columnStock',
            'columnCategoria',
            'columnPrecio']
        self.tablaVentas.configure(
            columns=self.tablaVentas_cols,
            displaycolumns=self.tablaVentas_dcols)
        self.tablaVentas.column(
            "columnCodigo",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.tablaVentas.column(
            "columnProducto",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.tablaVentas.column(
            "columnStock",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.tablaVentas.column(
            "columnCategoria",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.tablaVentas.column(
            "columnPrecio",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.tablaVentas.heading("columnCodigo", anchor="w", text='Codigo\n')
        self.tablaVentas.heading(
            "columnProducto",
            anchor="w",
            text='Producto\n')
        self.tablaVentas.heading("columnStock", anchor="w", text='Stock\n')
        self.tablaVentas.heading(
            "columnCategoria",
            anchor="w",
            text='Categoria\n')
        self.tablaVentas.heading("columnPrecio", anchor="w", text='Precio\n')
        self.tablaVentas.place(
            anchor="nw",
            height=300,
            relx=0.08,
            rely=0.3,
            width=800,
            x=0,
            y=0)
        self.lblStock = ttk.Label(self.productMenu, name="lblstock")
        self.lblStock.configure(
            relief="flat",
            state="normal",
            takefocus=False,
            text='Stock:')
        self.lblStock.place(anchor="e", relx=0.42, rely=0.16, x=0, y=0)
        self.lblCodigo = ttk.Label(self.productMenu, name="lblcodigo")
        self.lblCodigo.configure(
            font="TkDefaultFont",
            takefocus=False,
            text='Codigo:')
        self.lblCodigo.place(anchor="nw", relx=0.06, rely=0.15, x=0, y=0)
        self.lblProducto = ttk.Label(self.productMenu, name="lblproducto")
        self.lblProducto.configure(
            justify="left",
            relief="flat",
            text='Producto:\n')
        self.lblProducto.place(anchor="nw", relx=0.21, rely=0.15, x=0, y=0)
        self.lblPrecio = ttk.Label(self.productMenu, name="lblprecio")
        self.lblPrecio.configure(text='Precio:')
        self.lblPrecio.place(anchor="nw", relx=0.65, rely=0.15, x=0, y=0)
        self.lblDisponible = ttk.Label(self.productMenu, name="lbldisponible")
        self.lblDisponible.configure(
            foreground="#7d4fcc", text='Disponible:\n')
        self.lblDisponible.place(anchor="nw", relx=0.8, rely=0.15, x=0, y=0)
        self.txtCodigo = ttk.Entry(self.productMenu, name="txtcodigo")
        self.txtCodigo.place(
            anchor="nw",
            relx=0.06,
            rely=0.19,
            width=110,
            x=0,
            y=0)
        self.txtProducto = ttk.Entry(self.productMenu, name="txtproducto")
        self.txtProducto.configure(font="TkFixedFont")
        self.txtProducto.place(
            anchor="nw",
            relx=0.21,
            rely=0.19,
            width=110,
            x=0,
            y=0)
        self.txtStock = ttk.Entry(self.productMenu, name="txtstock")
        self.txtStock.place(
            anchor="nw",
            relx=0.38,
            rely=0.19,
            width=110,
            x=0,
            y=0)
        self.txtPrecio = ttk.Entry(self.productMenu, name="txtprecio")
        self.txtPrecio.place(
            anchor="nw",
            relx=0.65,
            rely=0.19,
            width=110,
            x=0,
            y=0)
        self.txtDisponible = ttk.Entry(self.productMenu, name="txtdisponible")
        self.txtDisponible.configure(
            exportselection=False,
            font="TkDefaultFont",
            justify="left")
        self.txtDisponible.place(
            anchor="nw",
            relx=0.8,
            rely=0.19,
            width=110,
            x=0,
            y=0)
        self.btnVaciar = ttk.Button(self.productMenu, name="btnvaciar",command=self.empty)
        self.img_delete = tk.PhotoImage(file="src/img/delete.gif")
        self.btnVaciar.configure(image=self.img_delete, text='\n')
        self.btnVaciar.place(
            anchor="nw",
            height=30,
            relx=0.94,
            rely=0.14,
            width=30,
            x=0,
            y=0)
        self.lblFecha = ttk.Label(self.productMenu, name="lblfecha")
        self.lblFecha.configure(text='Fecha:\n')
        self.lblFecha.place(anchor="nw", relx=0.77, rely=0.05, x=0, y=0)
        self.lblTotal = ttk.Label(self.productMenu, name="lbltotal")
        self.lblTotal.configure(
            compound="right",
            font="TkDefaultFont",
            justify="left",
            relief="flat",
            state="normal",
            text='Total a Pagar:\n')
        self.lblTotal.place(anchor="nw", relx=0.65, rely=0.81, x=0, y=0)
        self.txtPagar = ttk.Entry(self.productMenu, name="txtpagar")
        self.txtPagar.place(
            anchor="nw",
            relx=0.76,
            rely=0.81,
            width=110,
            x=0,
            y=0)
        self.lblCliente = ttk.Label(self.productMenu, name="lblcliente")
        self.lblCliente.configure(
            anchor="n",
            compound="top",
            cursor="arrow",
            font="TkDefaultFont",
            text='Cliente\n')
        self.lblCliente.place(anchor="nw", relx=0.13, rely=0.77, x=0, y=0)
        self.txtCodigoCliente = ttk.Entry(
            self.productMenu, name="txtcodigocliente")
        self.txtCodigoCliente.place(
            anchor="nw",
            relx=0.13,
            rely=0.82,
            width=110,
            x=0,
            y=0)
        self.btnGuardar = ttk.Button(self.productMenu, name="btnguardar",command=self.save)
        self.img_save = tk.PhotoImage(file="src/img/save.gif")
        self.btnGuardar.configure(image=self.img_save, text='button2')
        self.btnGuardar.place(anchor="nw", relx=0.57, rely=0.82, x=0, y=0)
        self.btnBuscar = ttk.Button(self.productMenu, name="btnbuscar")
        self.img_search = tk.PhotoImage(file="src/img/search.gif")
        self.btnBuscar.configure(
            image=self.img_search,
            style="Toolbutton",
            takefocus=False,
            text='button3')
        self.btnBuscar.place(
            anchor="nw",
            height=30,
            relx=0.2,
            rely=0.76,
            width=30,
            x=0,
            y=0)
        self.lblCate = ttk.Label(self.productMenu, name="lblcate")
        self.lblCate.configure(
            compound="top",
            cursor="arrow",
            relief="flat",
            text='Categoria:\n')
        self.lblCate.place(anchor="nw", relx=0.52, rely=0.15, x=0, y=0)
        self.cbxCategoria = ttk.Combobox(self.productMenu, name="cbxcategoria")
        self.cbxCategoria.configure(values='Ropa Comida Muebles Herramientas')
        self.cbxCategoria.place(
            anchor="nw",
            relx=0.39,
            rely=0.89,
            width=90,
            x=0,
            y=0)
        self.btnMostra = ttk.Button(self.productMenu, name="btnmostra",command=self.list_by_category)
        self.img_Lista = tk.PhotoImage(file="src/img/Lista.gif")
        self.btnMostra.configure(
            cursor="arrow",
            image=self.img_Lista,
            takefocus=False,
            text='Por Categoria\n')
        self.btnMostra.place(anchor="nw", relx=0.44, rely=0.82, x=0, y=0)
        self.lblMostrar = ttk.Label(self.productMenu, name="lblmostrar")
        self.lblMostrar.configure(
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mostrar por Categoria:\n')
        self.lblMostrar.place(anchor="nw", relx=0.27, rely=0.82, x=0, y=0)
        self.lblGuardar = ttk.Label(self.productMenu, name="lblguardar")
        self.lblGuardar.configure(text='Guardar:\n')
        self.lblGuardar.place(anchor="nw", relx=0.5, rely=0.82, x=0, y=0)
        self.txtCategoria = ttk.Entry(self.productMenu, name="txtcategoria")
        self.txtCategoria.place(
            anchor="nw",
            relx=0.52,
            rely=0.19,
            width=90,
            x=0,
            y=0)
        self.btnBuscarProducto = ttk.Button(
            self.productMenu, name="btnbuscarproducto",command=self.searchProduct)
        self.btnBuscarProducto.configure(
            compound="top",
            cursor="arrow",
            default="normal",
            image=self.img_search,
            text='\n')
        self.btnBuscarProducto.place(
            anchor="nw",
            height=30,
            relx=0.94,
            rely=0.20,
            width=30,
            x=0,
            y=0)
        self.cbxFecha = DateEntry(self.productMenu, name="cbxfecha", width=12, background='darkblue', foreground='white', borderwidth=2)
        self.cbxFecha.place(
            anchor="nw",
            relx=0.82,
            rely=0.04,
            width=110,
            x=0,
            y=0)
        self.productMenu.pack_propagate(0)
        
        self.list()

        # Main widget
        self.mainwindow = self.productMenu

    def run(self):
        self.mainwindow.mainloop()
    
    def empty(self):
        self.txtCodigo.delete(0, 'end') 
        self.txtProducto.delete(0, 'end')  
        self.txtCategoria.delete(0, 'end') 
        self.txtPrecio.delete(0, 'end') 
        self.cbxFecha.set_date(self.cbxFecha['values'][0]) 

    def save(self):
        user_name=self.txtCodigoCliente.get()
        product_name=self.txtProducto.get()
        category=self.txtCategoria.get()
        price=self.txtPrecio.get()
        date=self.cbxFecha.get_date()
        if not user_name or not product_name or not category or not price or not date:
            messagebox.showerror("Error", "Llene todos los campos de texto.")
            return
        try:
            Selling.insert(user_name, product_name, category, price, date)
            messagebox.showinfo("Éxito", "Producto guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error de registro", f"Ocurrió un error: {e}")
    
    def list(self):
        products = Product.list_all() 
        self.tablaVentas.delete(*self.tablaVentas.get_children()) 
        for pro in products:
            self.tablaVentas.insert("", "end", values=(
            pro.code,       
            pro.name,    
            pro.stock,        
            pro.category,    
            pro.price      
        ))
            
    def list_by_category(self):
        category = self.cbxCategoria.get()
        products = Product.list_by_category(category)
        self.tablaVentas.delete(*self.tablaVentas.get_children()) 
        for pro in products:
            self.tablaVentas.insert("", "end", values=(
            pro.code,       
            pro.name,    
            pro.stock,        
            pro.category,    
            pro.price      
        ))
            
        
    def searchProduct(self):
        code = self.txtCodigo.get()  
        product = Product.find_by_code(code)
        if product:
            self.txtProducto.delete(0, tk.END)  
            self.txtProducto.insert(0, product.name)  

            self.txtCategoria.delete(0, tk.END) 
            self.txtCategoria.insert(0, product.category)  

            self.txtPrecio.delete(0, tk.END) 
            self.txtPrecio.insert(0, product.price)
            
            self.txtStock.delete(0, tk.END) 
            self.txtStock.insert(0, product.stock)

            self.txtDisponible.delete(0, tk.END) 
            self.txtDisponible.insert(0, "si") 
            #messagebox.showinfo("Producto encontrado", f"Nombre: {product.name}\nCategoría: {product.category}\nPrecio: {product.price}\nStock: {product.stock}")
        else:
            # Si no se encuentra el producto, muestra un mensaje de error
            messagebox.showerror("Error", "Producto no encontrado.")




if __name__ == "__main__":
    app = product_menuUI()
    app.run()
