# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

# Ce fichier recense toutes les lib necessaire et déclare les variables globales, on as juste à importe settings
# dans les autres fichier pour utiliser les fonctions voulues
import sys
import string
import random
import hashlib
import authenticate
import menu
import add
import delete
import list
import update
import string
import random
import smtplib
import time
import itertools
import signal
import threading


# Information de connection pour la base de donnée
def init():
    global DB_IP, DB_PORT, DB_USER, DB_PASSWORD
    DB_IP = 'benjamin.beyerle.fr'
    DB_PORT = 3006
    DB_USER = 'clicmed_user'
    DB_PASSWORD = 'Cl1cM3dUs3r'
