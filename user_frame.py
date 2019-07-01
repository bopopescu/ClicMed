import settings


# User panel with less tools and restricted access
def menu(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med Admin')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    login_btn = settings.tk.Button(root_frame, text='File Management', command=lambda: settings.ftp.main_frame(
        root_frame, username))
    login_btn.grid(row=0, column=1, sticky='ne', pady=20)

    return_btn = settings.tk.Button(root_frame, text='Return', command=lambda: settings.login.login_window(root_frame))
    return_btn.grid(row=2, column=3, sticky='se')

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=2, column=4, sticky='sw')

