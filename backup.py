import settings

settings.log.init_log('backup')

# Repertoire de destination
root_dest = settings.os.path.join('/home/ftp/ClicMed/User/User1/backup')
# Repertoire racine du user
root_directory = settings.os.path.join('/home/ftp/ClicMed/User/User1/')
print(root_directory)

# On recupere la date dans une variable
date = settings.datetime.datetime.now().strftime('%Y-%m-%d')

print("\n-----------------------------------------------------------\n")
print("Backup of " + root_directory + "docs" + "\n")
print("-----------------------------------------------------------\n")

# Creation de l'archive backup_XX-XX-XX.tar.gz contenant le repertoire "docs" dans le repertoire de destination
try:
    settings.shutil.make_archive(
        root_dest + '/' + 'backup_' + date, 'gztar',
        root_directory,
        'docs',
        )
except:
       print ("File or directory doesn't exist !!!")
