#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import product_menuui as baseui


class product_menu(baseui.product_menuUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = product_menu()
    app.run()
