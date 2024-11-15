#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import sign_upui as baseui


class sign_up(baseui.sign_upUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = sign_up()
    app.run()
