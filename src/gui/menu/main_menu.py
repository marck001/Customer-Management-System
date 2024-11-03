#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import main_menuui as baseui


class menu(baseui.menuUI):
    def __init__(self, master=None):
        super().__init__(master)

    def on_window_products(self):
        pass

    def callback(self, event=None):
        pass

    def on_window_selling(self):
        pass

    def on_window_sell_products(self):
        pass

    def on_window_logout(self):
        pass


if __name__ == "__main__":
    app = menu()
    app.run()
