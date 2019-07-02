import settings


def log(username, message):

    ts_date = str('{date:%Y-%m-%d_%H:%M:%S}'.format(date=settings.datetime.datetime.now()))
    log_string = ts_date + '\t' + username + '\t' + message
    client = settings.paramiko.SSHClient()
    client.set_missing_host_key_policy(settings.paramiko.AutoAddPolicy())
    client.connect(settings.HOST, username=settings.SSH_USER, password=settings.SSH_PWD)
    command = 'sudo echo "' + log_string + '" >> /home/ftp/log/ClicMed.log'
    stdin, stdout, stderr = client.exec_command(command)
    client.close()
