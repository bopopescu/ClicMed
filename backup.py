import datetime
import os


def log(username, message):

    ts_date = str('{date:%Y-%m-%d_%H:%M:%S}'.format(date=datetime.datetime.now()))
    log_string = ts_date + '\t' + username + '\t' + message
    command = 'sudo echo "' + log_string + '" >> /home/ftp/log/ClicMed.log'
    os.system(command)


for i in range(5, 0, -1):
    current = '/home/ftp/Backup/Backup.' + str(i) + '.tar.gz'
    future = '/home/ftp/Backup/Backup.' + str(i+1) + '.tar.gz'
    print(current, future)
    if os.path.isfile(current):
        os.rename(current, future)
os.rename('/home/ftp/Backup/Backup.tar.gz', '/home/ftp/Backup/Backup.1.tar.gz')
os.system('tar -C /home/ftp/ -cvf /home/ftp/Backup/Backup.tar.gz ClicMed')
log('System', ' did a backup')
