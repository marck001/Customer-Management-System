#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import register_productui as baseui


class Register_product(baseui.Register_productUI):
    def __init__(self, master=None):
        super().__init__(master)

    def on_btn_register(self, widget_id):
        pass

    def on_btn_delete(self, widget_id):
        pass

    def on_btn_clear(self, widget_id):
        pass

def on_btn_search(self, widget_id):
    product_id = self.entry_product_id.get()  
    if product_id:
        print(f"Buscando producto con ID: {product_id}")
    else:
        print("Por favor, ingrese un ID de producto.")

def on_btn_modify(self, widget_id):
    product_id = self.entry_product_id.get()
    new_name = self.entry_product_name.get()
    new_price = self.entry_product_price.get()

    if product_id and new_name and new_price:
        print(f"Modificando producto {product_id} con nombre: {new_name}, precio: {new_price}")
    else:
        print("Por favor, complete todos los campos para modificar.")