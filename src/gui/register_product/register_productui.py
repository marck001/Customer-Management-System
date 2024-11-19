import tkinter as tk
from tkinter import ttk, messagebox
from models.Product import Product

class RegisterProductUI:
    def __init__(self, master=None):
        # Set up the main window
        toplevel1 = tk.Toplevel(master) if master else tk.Tk()
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
            highlightthickness=0
        )
        canvas3.place(height=500, width=500, x=100, y=100)

        # Entries
        self.txt_code = tk.Entry(toplevel1, bg="#e3f2fd", fg="#000", highlightbackground="#64b5f6", relief="solid")
        self.txt_code.place(anchor="nw", height=30, width=150, x=350, y=200)

        self.txt_name = tk.Entry(toplevel1, bg="#e3f2fd", fg="#000", highlightbackground="#64b5f6", relief="solid")
        self.txt_name.place(anchor="nw", height=30, width=150, x=350, y=250)

        self.spn_stock = tk.Spinbox(toplevel1, from_=0, to=1000, increment=1, bg="#e3f2fd", fg="#000", relief="solid")
        self.spn_stock.place(anchor="nw", height=30, width=150, x=350, y=350)

        self.txt_price = tk.Entry(toplevel1, bg="#e3f2fd", fg="#000", highlightbackground="#64b5f6", relief="solid")
        self.txt_price.place(anchor="nw", height=30, width=150, x=350, y=400)

        self.cbx_category = ttk.Combobox(toplevel1, values=["Ropa", "Comida", "Muebles", "Herramientas"])
        self.cbx_category.place(anchor="nw", height=30, width=150, x=350, y=300)

        # Labels
        self.lbl_code = tk.Label(toplevel1, text="Código:", background="#f9f9f9", fg="#000")
        self.lbl_code.place(anchor="nw", x=200, y=200)

        self.lbl_name = tk.Label(toplevel1, text="Nombre:", background="#f9f9f9", fg="#000")
        self.lbl_name.place(anchor="nw", x=200, y=250)

        self.lbl_category = tk.Label(toplevel1, text="Categoría:", background="#f9f9f9", fg="#000")
        self.lbl_category.place(anchor="nw", x=200, y=300)

        self.lbl_stock = tk.Label(toplevel1, text="Stock:", background="#f9f9f9", fg="#000")
        self.lbl_stock.place(anchor="nw", x=200, y=350)

        self.lbl_price = tk.Label(toplevel1, text="Precio:", background="#f9f9f9", fg="#000")
        self.lbl_price.place(anchor="nw", x=200, y=400)

        label8 = tk.Label(
            toplevel1,
            text="Registro de Producto",
            background="#ffffff",
            font=("Helvetica", 16, "bold"),
            fg="#000"
        )
        label8.place(anchor="nw", x=300, y=40)

        # Buttons
        self.btn_register = tk.Button(toplevel1, text="Registrar", bg="#007bff", fg="#fff", relief="raised", command=self.on_btn_register, width=10, height=1)
        self.btn_register.place(anchor="e", x=400, y=500)

        self.btn_delete = tk.Button(toplevel1, text="Eliminar", bg="#dc3545", fg="#fff", relief="raised", command=self.on_btn_delete, width=10, height=1)
        self.btn_delete.place(anchor="e", x=500, y=500)

        self.btn_clear = tk.Button(toplevel1, text="Limpiar", bg="#6c757d", fg="#fff", relief="raised", command=self.on_btn_clear, width=10, height=1)
        self.btn_clear.place(anchor="e", x=300, y=500)
        
        self.btn_search= tk.Button(toplevel1, text="Buscar", bg="#007bff", fg="#fff", relief="raised", command=self.on_btn_search, width=10, height=1)
        self.btn_search.place(anchor="e", x=400, y=550)

        self.btn_close = tk.Button(toplevel1, text="Salir", bg="#dc3545", fg="#fff", relief="raised", command=self.on_btn_close, width=10, height=1)
        self.btn_close.place(anchor="e", x=500, y=550)

        self.btn_modify = tk.Button(toplevel1, text="Modificar", bg="#6c757d", fg="#fff", relief="raised", command=self.on_btn_modify, width=10, height=1)
        self.btn_modify.place(anchor="e", x=300, y=550)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def on_btn_register(self):
        code = self.txt_code.get()
        name = self.txt_name.get()
        category = self.cbx_category.get()
        try:
            price = float(self.txt_price.get())
            stock = int(self.spn_stock.get())

            if not code or not name or not category or not price or not stock:
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos antes de registrar.",parent=self.mainwindow)
                return

        except ValueError:
            messagebox.showerror("Error", "Precio y Stock deben ser números",parent=self.mainwindow)
            return

        if Product.find_by_code(code):
            messagebox.showinfo("Error", "El producto ya existe",parent=self.mainwindow)
        else:
            Product.insert(code, name, category, price, stock)
            messagebox.showinfo("Éxito", "Producto registrado",parent=self.mainwindow)

    def on_btn_delete(self):
        code = self.txt_code.get()
        product = Product.find_by_code(code)
        if product:
            product.delete()
            messagebox.showinfo("Éxito", "Producto eliminado",parent=self.mainwindow)
            self.on_btn_clear()
        else:
            messagebox.showerror("Error", "Producto no encontrado",parent=self.mainwindow)

    def on_btn_clear(self):
        self.txt_code.delete(0, tk.END)
        self.txt_name.delete(0, tk.END)
        self.cbx_category.set("")
        self.spn_stock.delete(0, tk.END)
        self.txt_price.delete(0, tk.END)
        

    
    def on_btn_close(self):
       self.mainwindow.destroy()

    def on_btn_search(self, widget_id):
        product_id = self.txt_code.get()
        #name = self.txt_name.get()
        #category = self.cbx_category.get()
        #price = float(self.txt_price.get())
        #stock = int(self.spn_stock.get())
        
        product = Product.find_by_code(product_id) 
            
        if  product:
            self.txt_name.delete(0, tk.END)  
            self.txt_name.insert(0, product.name)  

            self.cbx_category.delete(0, tk.END) 
            self.cbx_category.insert(0, product.category)  

            self.txt_price.delete(0, tk.END) 
            self.txt_price.insert(0, product.price)
            
            self.spn_stock.delete(0, tk.END) 
            self.spn_stock.insert(0, product.stock)
                     
        else:
           messagebox.showerror("Error", "Producto no encontrado",parent=self.mainwindow)

    def on_btn_modify(self):
         # aqui no puede ir parametro porque es evento, solo llamalo de ahi por buscar
        product_id = self.txt_code.get()
        new_name = self.txt_name.get()
        new_price =  float(self.txt_price.get())
        new_category = self.cbx_category.get()
        new_stock = int(self.spn_stock.get())

        #obtener los valores y ponerlos en la funcion para modificar
        if product_id and new_name and new_price:
            Product.update()
            print(f"Modificando producto {product_id} con nombre: {new_name}, precio: {new_price}")
        else:
            print("Por favor, complete todos los campos para modificar.")   
    



