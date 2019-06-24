import settings


def main_frame(root_frame):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('User Management')
    root_frame.geometry('450x330')
    root_frame.maxsize(650, 330)
    root_frame.minsize(650, 330)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    nb_rows = cursor.rowcount
    cursor.close()
    cnx.close()
    idx = 0

    label0 = settings.tk.Label(root_frame, text='id user', font=("Arial", 10), fg='black', bg='white',
                               relief=settings.tk.RIDGE, width=5)
    label0.grid(row=idx, column=2, sticky='W', padx=1)
    label1 = settings.tk.Label(root_frame, text='username', font=("Arial", 10), fg='black', bg='white',
                               relief=settings.tk.RIDGE, width=10)
    label1.grid(row=idx, column=3, sticky='W', padx=1)
    label2 = settings.tk.Label(root_frame, text='Name', font=("Arial", 10), fg='black', bg='white',
                               relief=settings.tk.RIDGE, width=10)
    label2.grid(row=idx, column=4, sticky='W', padx=1)
    label3 = settings.tk.Label(root_frame, text='Surname', font=("Arial", 10), fg='black', bg='white',
                               relief=settings.tk.RIDGE, width=10)
    label3.grid(row=idx, column=5, sticky='W', padx=1)
    label3 = settings.tk.Label(root_frame, text='email address', font=("Arial", 10), fg='black', bg='white',
                               relief=settings.tk.RIDGE, width=30)
    label3.grid(row=idx, column=6, sticky='W')

    for row in records:
        idx += 1
        edit_btn = settings.tk.Button(root_frame, text='Edit', command=lambda: user_edit())
        edit_btn.grid(row=idx, column=0)
        del_btn = settings.tk.Button(root_frame, text='Delete', command=lambda: user_del())
        del_btn.grid(row=idx, column=1)
        label0 = settings.tk.Label(root_frame, text=row[0], font=("Arial", 10), fg='black', bg='white',
                                   relief=settings.tk.RIDGE, width=5)
        label0.grid(row=idx, column=2, sticky='W')
        label1 = settings.tk.Label(root_frame, text=row[1], font=("Arial", 10), fg='black', bg='white',
                                   relief=settings.tk.RIDGE, width=10)
        label1.grid(row=idx, column=3, sticky='W')
        label2 = settings.tk.Label(root_frame, text=row[2], font=("Arial", 10), fg='black', bg='white',
                                   relief=settings.tk.RIDGE, width=10)
        label2.grid(row=idx, column=4, sticky='W')
        label3 = settings.tk.Label(root_frame, text=row[3], font=("Arial", 10), fg='black', bg='white',
                                   relief=settings.tk.RIDGE, width=10)
        label3.grid(row=idx, column=5, sticky='W')
        label4 = settings.tk.Label(root_frame, text=row[4], font=("Arial", 10), fg='black', bg='white',
                                   relief=settings.tk.RIDGE, width=30, anchor='w')
        label4.grid(row=idx, column=6, sticky='W')


def user_del():
    print('test')


def user_edit():
    print('test')
