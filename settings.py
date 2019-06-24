import os
import sys
import tkinter as tk
import login
import admin_frame
import user_frame
import mysql.connector as mysql
import hashlib


# Settings global variables
HOST = 'benjamin.beyerle.fr'
MYSQL_USER = 'ClicMed-user'
MYSQL_USER_PWD = 'clicmedUs3r'
MYSQL_DB = 'ClicMed'
ICO = os.path.join(sys.path[0], "Resources/ClicMed.gif")
ICO_ERROR = os.path.join(sys.path[0], "Resources/incorrect2.png")
root = tk.Tk()
img_error = tk.PhotoImage(file=ICO_ERROR)
img_ico = tk.PhotoImage(file=ICO)
root.tk.call('wm', 'iconphoto', root._w, img_ico)

