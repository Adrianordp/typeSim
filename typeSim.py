#!/bin/python3
from time import sleep
from random import uniform
import tkinter
import tkinter.font as tkFont
import tkinter.ttk as ttk
from typing import Text

class Application:
    def __init__(self, master=None):
        root.title('TypeSim')
        self.fontParagraph = ("Arial", "12")
        self.fontTyping = ("Arial", "12")
        root.geometry("500x300")

        self.typingWindow = tkinter.Toplevel()
        self.typingWindow.geometry("500x300")
        self.typingWindow.attributes('-topmost','true')

        self.typing = tkinter.Text(self.typingWindow)
        self.typing.pack(expand=True, fill=tkinter.BOTH)
        self.typing["width"] = 30
        self.typing["font"] = self.fontTyping
        self.typing.config(state=tkinter.DISABLED)


        self.container1 = tkinter.Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = tkinter.Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container4 = tkinter.Frame(master)
        self.container4["padx"] = 20
        self.container4.pack(side=tkinter.LEFT)

        self.container3 = tkinter.Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.titulo = tkinter.Label(self.container1, text="Typing Simulator")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.paragraph = tkinter.Text(self.container2, height=12)
        self.paragraph["font"] = self.fontParagraph
        self.paragraph.pack()
        self.paragraph.bind("<Button-3>", self.do_popup)

        self.fontFamilies = sorted(tkFont.families())
        self.comboFont = ttk.Combobox(self.container4, values=self.fontFamilies, state='readonly')
        self.comboFont.pack(side=tkinter.LEFT)
        self.comboFont.current(0)

        self.fontSizeEntry = tkinter.Entry(self.container4, width=3)
        self.fontSizeEntry.insert(tkinter.END, '12')
        self.fontSizeEntry.pack(side=tkinter.LEFT)

        self.speedLabel = tkinter.Label(self.container4, text='Speed')
        self.speedLabel.pack(side=tkinter.LEFT,padx=(20,0))

        self.speedMin = tkinter.Entry(self.container4, width=5)
        self.speedMin.insert(tkinter.END, '0.001')
        self.speedMin.pack(side=tkinter.LEFT)

        self.speedMax = tkinter.Entry(self.container4, width=5)
        self.speedMax.insert(tkinter.END, '0.01')
        self.speedMax.pack(side=tkinter.LEFT)

        self.runButton = tkinter.Button(self.container3)
        self.runButton["text"] = "Run"
        self.runButton["font"] = ("Calibri", "8")
        self.runButton["width"] = 12
        self.runButton["command"] = self.do_runButton
        self.runButton.pack(side=tkinter.LEFT)

        self.menu = tkinter.Menu(self.paragraph, tearoff=0)
        self.menu.add_command(label="Paste", command=self.do_paste)
        self.menu.add_command(label="Clear", command=self.do_clear)
        self.menu.add_command(label="Clear and Paste", command=self.do_clear_and_paste)
        self.menu.bind("<FocusOut>",self.popupFocusOut)

    def popupFocusOut(self, event=None):
        self.menu.unpost()
    
    def do_popup(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def do_paste(self):
        clipboard_text  = root.clipboard_get()
        self.paragraph.insert(tkinter.CURRENT, clipboard_text)

    def do_clear(self):
        self.paragraph.delete('1.0', tkinter.END)

    def do_clear_and_paste(self):
        self.do_clear()
        self.do_paste()

    def do_runButton(self):
        self.fontFamily = self.comboFont.get()
        self.fontSize = self.fontSizeEntry.get()
        self.fontTyping = (self.fontFamily, self.fontSize)

        self.typing["font"] = self.fontTyping

        speedMin = float(self.speedMin.get())
        speedMax = float(self.speedMax.get())

        self.typing.config(state=tkinter.NORMAL)
        self.typing.delete('1.0', tkinter.END)
        self.typing.config(state=tkinter.DISABLED)

        paragraph = self.paragraph.get('1.0', tkinter.END)
        N = len(paragraph)

        for i in range(N):
                self.typing.config(state=tkinter.NORMAL)
                self.typing.insert(tkinter.END, paragraph[i])
                self.typing.config(state=tkinter.DISABLED)

                sleep(uniform(speedMin,speedMax))

                root.update()
    
root = tkinter.Tk()
Application(root)
root.mainloop()
