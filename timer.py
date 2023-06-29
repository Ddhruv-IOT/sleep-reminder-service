from datetime import datetime
import pyttsx3 as ve
print(datetime.now())

voice_engine = ve.init()
voice_engine.setProperty("rate", 141)
voice_engine.say("Hello Sir")
voice_engine.runAndWait()

import win32api

win32api.MessageBox(0, 'hello', 'title', 0x00001000)
import pyautogui as pag
pag.confirm(text="Hello World", title="The Hello World Box")

import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Title", "Message")


from gi.repository import Gtk

dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "This is an INFO MessageDialog")
dialog.format_secondary_text(
    "And this is the secondary text that explains things.")
dialog.run()
print ("INFO dialog closed")