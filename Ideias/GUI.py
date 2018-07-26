#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter

top = tkinter.Tk()

menubar = tkinter.Menu()

menu1 = tkinter.Menu(menubar, tearoff = 0)
menu1.add_command(label="New", command = print)

top.config(menu = menubar)
top.mainloop()