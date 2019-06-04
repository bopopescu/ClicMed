#!/usr/bin/env python
import shutil
import datetime
import os

root_dest = os.path.join('/home/ftp/ClicMed/User/User1/backup') #Repetoire de destination
root_directory = os.path.join('/home/ftp/ClicMed/User/User1/') #Repertoire racine du user
print(root_directory)

date = datetime.datetime.now().strftime('%Y-%m-%d') #on recupere la date dans une variable

print("\n-----------------------------------------------------------\n")
print("Sauvegarde de " + root_directory + "docs" + "\n")
print("-----------------------------------------------------------\n")

#creation de l'archive backup_XX-XX-XX.tar.gz contenant le repertoire "docs" dans le repertoire de destination
shutil.make_archive(
    root_dest + '/' + 'backup_' + date, 'gztar', 
    root_directory,
    'docs',

)

