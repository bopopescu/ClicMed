import os
import sys
import tkinter as tk
import mail_bomber
import pyAesCrypt
import ftplib
import tkinter.filedialog as fdialog
import file_manager
import threading
import itertools
import signal
import ssl
import time
import smtplib
import string
import random
import login
import menu
import mysql.connector as mysql
import hashlib
import user_manager
import logging
import log
import shutil
import datetime


# Settings global variables
HOST = 'benjamin.beyerle.fr'
MYSQL_USER = 'ClicMed-user'
MYSQL_USER_PWD = 'clicmedUs3r'
MYSQL_ADMIN = 'ClicMed-admin'
MYSQL_ADMIN_PWD = 'clicmedAdm1n'
MYSQL_DB = 'ClicMed'

SSH_USER = 'ClicMed-ssh'
SSH_PWD = 'clicmedSSH'
SSH_PORT = 22

FTP_USER = 'ClicMed-user'
FTP_PWD = 'clicmedUs3r'

CRYPTO_PWD = 'clicmed'
CRYPTO_BUFFER = 64 * 1024


ICO = os.path.join(sys.path[0], "Resources/ClicMed.gif")
ICO_ERROR = os.path.join(sys.path[0], "Resources/incorrect2.png")
root = tk.Tk()
img_error = tk.PhotoImage(file=ICO_ERROR)
img_ico = tk.PhotoImage(file=ICO)
root.tk.call('wm', 'iconphoto', root._w, img_ico)

EMAIL = 'clicmed.abkp@gmail.com'
EMAIL_PWD = 'clicmedmail'

