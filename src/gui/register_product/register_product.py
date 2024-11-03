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


if __name__ == "__main__":
    app = Register_product()
    app.run()
