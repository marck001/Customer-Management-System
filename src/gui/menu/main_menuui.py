#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

class MenuUI:  
    
    def __init__(self,user_name):
        # build ui
        self.menu = tk.Tk()
        self.current_window = None 
        self.menu.configure(
            background="#ffffff",
            height=900,
            relief="flat",
            takefocus=True,
            width=1200
        )
        self.menu.overrideredirect(False)
        self.menu.resizable(True, False)
        self.menu.title("Menu")
        self.user_name = user_name

        self.canva1 = tk.Canvas(self.menu, name="canva1")
        self.canva1.configure(
            background="#45fcf8",
            confine=False,
            cursor="arrow",
            relief="flat",
            state="normal",
            takefocus=False,
            width=300
        )
        self.canva1.pack(anchor="sw", expand=True, fill="y", side="right")

        # Create buttons for the menu
        self.btn_menu2 = self.create_button("Registrar Producto", self.on_window_products, 0.37)
        self.btn_menu3 = self.create_button("Hacer compra", self.on_window_selling, 0.44)
        self.btn_menu4 = self.create_button("Ver productos Comprados", self.on_window_sell_products, 0.51)
        self.btn_menu5 = self.create_button("Log out", self.on_window_logout, 0.58)
        self.btn_dispose = self.create_button("Salir", self.on_window_dispose, 0.65)

        
        # User label
        self.create_user_label(username=user_name)
        user_lbl=ttk.Label(self.menu, text=f'Bienvenido! {user_name}', font="{times new roman} 20 {}", background="#ffffff")
        user_lbl.place(relx=0.7, rely=0.03)

        # Additional components
        self.create_additional_components()

        self.mainwindow = self.menu
        

    def create_button(self, text, command, rel_y):
        btn = ttk.Button(self.menu, text=text, cursor="hand2")
        btn.place(anchor="nw", height=50, relx=0.0, rely=rel_y, width=300, x=0, y=0)
        btn.configure(command=command)
        return btn

    def create_user_label(self, username):
        label2 = ttk.Label(self.menu)
        self.img_user_colored = tk.PhotoImage(file="src/img/user_colored.png")
        label2.configure(
            compound="center",
            image=self.img_user_colored,
            justify="left",
            text= username,
        )
        label2.place(x=59, y=40)

    def create_additional_components(self):
        frame1 = tk.Frame(self.menu, background="#f8f8f8", height=200, width=200)
        self.add_images_to_frame(frame1)
        frame1.place(anchor="nw", height=500, relx=0.32, rely=0.14, width=750, x=0, y=0)

        self.menu.pack_propagate(0)

    def add_images_to_frame(self, frame):
        # Add images to the frame
        self.create_image_label(frame, "src/img/dress_3.png", 'Ropa', 0.05, 0.12)
        self.create_image_label(frame, "src/img/groceries.png", 'Comida', 0.42, 0.12)
        self.create_image_label(frame, "src/img/support.png", 'Herramientas', 0.79, 0.12)
        self.create_image_label(frame, "src/img/sell.png", 'Comida', 0.3, 0.61)

    def create_image_label(self, frame, img_path, text, rel_x, rel_y):
        img = tk.PhotoImage(file=img_path)
        label = tk.Label(frame, image=img, text=text)
        label.image = img  
        label.place(anchor="nw", relx=rel_x, rely=rel_y, x=0, y=0)

    def run(self):
        self.mainwindow.mainloop()
        
    def on_window_products(self):
        from gui.register_product.register_productui import RegisterProductUI
        RegisterProductUI(self.mainwindow )

    def on_window_selling(self):       
        from gui.product_menu.product_menuui import product_menuUI
        product_menuUI(self.user_name,self.mainwindow )

    def on_window_sell_products(self):
        from gui.product_selling.product_sellingui import ProductSellingUI
        ProductSellingUI(self.user_name,self.mainwindow )

    def on_window_logout(self):
        from gui.login.loginui import loginUI
        self.menu.destroy()
        loginUI()
        

    def on_window_dispose(self):
        self.menu.destroy()
        
    def open_window(self, window_class):
        self.close_current_window()
        self.current_window = window_class(self.menu)

    def close_current_window(self):   
        if self.current_window is not None:
            self.current_window.destroy() 
            self.current_window = None

if __name__ == "__main__":
    app = MenuUI()
    app.run()
