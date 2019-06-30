import settings


# Hashing password for security
def password_hash(password_input):
    byte_password = password_input.encode()
    hashed_password = settings.hashlib.md5(byte_password).hexdigest()
    return hashed_password


def clear_window(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()
    column, row = root_frame.grid_size()

    for i in range(0, row):
        root_frame.rowconfigure(i, weight=0)

    for i in range(0, column):
        root_frame.columnconfigure(i, weight=0)


# Window for log in
def login_window(root_frame):

    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med')
    root_frame.geometry('250x130')
    root_frame.maxsize(250, 130)
    root_frame.minsize(250, 130)

    label1 = settings.tk.Label(root_frame, text='Login', font=("Arial", 30), fg='white', bg='#3c3f41')
    label1.grid(column=1, columnspan=3, sticky='W')

    label2 = settings.tk.Label(root_frame, text='Username :', font=("Arial", 10), fg='white', bg='#3c3f41')
    label2.grid(row=1, sticky='E')

    label3 = settings.tk.Label(root_frame, text='Password :', font=("Arial", 10), fg='white', bg='#3c3f41')
    label3.grid(row=2, sticky='E')

    user = settings.tk.Entry(root_frame, width=15)
    user.grid(row=1, column=1, columnspan=2, sticky='W')
    user.focus()

    password = settings.tk.Entry(root_frame, show="*", width=15)
    password.grid(row=2, column=1, columnspan=2, sticky='W')

    login_btn = settings.tk.Button(root_frame, text='Login', command=lambda: check_user(user.get(), password.get(),
                                                                                        password, root_frame))
    login_btn.grid(row=3, column=1, sticky='E')

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=3, column=2, sticky='W')


# Function to verify if user is in the database (username + password)
def check_user(username, password_input, password_label, root_frame):

    hashed_password = password_hash(password_input)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT Username, PasswordHash, GroupId FROM Users WHERE Username = %s AND PasswordHash = %s",
                   (username, hashed_password))
    records = cursor.fetchall()
    cursor.close()
    cnx.close()

    try:
        group_id = records[0][2]
    except IndexError:
        incorrect = settings.tk.Label(root_frame, image=settings.img_error, background='#3c3f41')
        incorrect.grid(row=1, column=4, sticky='W')

        password_label.delete(0, settings.tk.END)
    else:
        if group_id == 0:
            settings.admin_frame.admin(root_frame, username)
        else:
            settings.user_frame.user(root_frame, username)



