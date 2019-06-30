import os
import sys
import tkinter as tk
import ftplib
import tkinter.filedialog as fdialog
import ftp
import threading
import itertools
import signal
import re
import ssl
import time
import smtplib
import string
import random
import login
import admin_frame
import user_frame
import mysql.connector as mysql
import hashlib
import user_mgmt
import logging
import log
import shutil
import datetime
import paramiko


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


ICO = os.path.join(sys.path[0], "Resources/ClicMed.gif")
ICO_ERROR = os.path.join(sys.path[0], "Resources/incorrect2.png")
root = tk.Tk()
img_error = tk.PhotoImage(file=ICO_ERROR)
img_ico = tk.PhotoImage(file=ICO)
root.tk.call('wm', 'iconphoto', root._w, img_ico)

EMAIL = 'clicmed.abkp@gmail.com'
EMAIL_PWD = 'clicmedmail'

