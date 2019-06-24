import settings


# Admin panel with all the tools and full access
def admin(root_frame):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med Admin')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    login_btn = settings.tk.Button(root_frame, text='User Management', command=lambda: settings.user_mgmt.main_frame(
        root_frame))
    login_btn.grid(row=3, column=1, sticky='E')