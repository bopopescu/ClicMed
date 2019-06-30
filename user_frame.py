import settings


# User panel with less tools and restricted access
def user(root_frame, username):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med Admin')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)
