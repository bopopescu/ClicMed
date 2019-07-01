import settings


# Admin panel with all the tools and full access
def main_frame(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')

    if group == 0:
        root_frame.title('Clic Med Admin')
        root_frame.geometry('450x330')
        root_frame.maxsize(450, 330)
        root_frame.minsize(450, 330)

        usr_btn = settings.tk.Button(root_frame, text='User Management',
                                     command=lambda: settings.user_manager.main_frame(root_frame,
                                                                                      username, 'All', group))
        usr_btn.grid(row=0, column=0, sticky='ne', pady=20, padx=20)

        file_btn = settings.tk.Button(root_frame, text='File Management',
                                      command=lambda: settings.file_manager.main_frame(root_frame, username, group))
        file_btn.grid(row=0, column=1, sticky='ne', pady=20)

        mail_btn = settings.tk.Button(root_frame, text='Mail Bomber', command=lambda: settings.mail_bomber.main_frame(
            root_frame, username, group))
        mail_btn.grid(row=1, column=1, sticky='ne', pady=20)

        brute_btn = settings.tk.Button(root_frame, text='BruteForcer', command=lambda: settings.bruteforce.main_frame(
            root_frame, username, group))
        brute_btn.grid(row=1, column=0, sticky='ne', pady=20)

        return_btn = settings.tk.Button(root_frame, text='Return',
                                        command=lambda: settings.login.login_window(root_frame))
        return_btn.grid(row=2, column=2, sticky='se')

        exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
        exit_btn.grid(row=2, column=3, sticky='sw')

    else:
        settings.file_manager.main_frame(root_frame, username, group)
