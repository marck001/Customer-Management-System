#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import product_sellingui as baseui


class Product_selling(baseui.Product_sellingUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = Product_selling()
    app.run()
