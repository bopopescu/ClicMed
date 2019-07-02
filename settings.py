# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import os
import sys
import tkinter as tk
from tkinter import ttk
from queue import Queue
import mail_bomber
import base64
import pyAesCrypt
import ftplib
import tkinter.filedialog as fdialog
import threading
import itertools
import signal
import ssl
import time
import smtplib
import string
import random
import mysql.connector as mysql
import hashlib
import logging
import shutil
import datetime
import socket
import paramiko

import log
import user_manager
import file_manager
import login
import menu
import bruteforce
import port_scanner


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

