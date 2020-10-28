# s = pyshorteners.Shortener()
# short_link = s.qpsru.short('https://aparat.com')
# print(short_link)

import pyshorteners
from tkinter import *
from tkinter import messagebox
import webbrowser
# Define window
root = Tk()
root.geometry('400x150')
root.config(bg='#121212')
root.resizable(0,0)

# Functions
def shorter():
    global short_link
    if 'http' in url_entry.get() or 'htpps' in url_entry.get():
        s = pyshorteners.Shortener()
        short_link = s.qpsru.short(url_entry.get())
        result_entry = Entry(root, width=len(short_link)+10)
        result_entry.insert(0,short_link )
        result_entry.place(relx=0.5, rely=0.7, anchor='c')   
        show_in_browser_btn.config(state=NORMAL)
        url_entry.delete(0, END)
    else:
        messagebox.showerror('Error','Enter A Valid Url')
        url_entry.delete(0, END)

def open():
    webbrowser.open(short_link)


# Making the widget

url_entry = Entry(root, width=30)
confirm_btn = Button(root, text='Short URL', bg='#121212', fg='white', borderwidth=3, command=shorter)
show_in_browser_btn = Button(root, text='Open', bg='#121212', fg='white', borderwidth=3,command=open, state=DISABLED )
# Griding widgets on screen
url_entry.place(relx=0.5, rely=0.2, anchor='c')
confirm_btn.place(relx=0.5, rely=0.5, anchor='c')
show_in_browser_btn.place(relx=0.85, rely=0.7, anchor='c')
# Calling tha main window's mainloop
root.mainloop()