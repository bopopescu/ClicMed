import settings


def main_frame(root_frame):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('User Management')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    nb_rows = cursor.rowcount
    cursor.close()
    cnx.close()

    for i in range(0, nb_rows):
        edit_btn = settings.tk.Button(root_frame, text='Edit', command=lambda: user_edit())
        edit_btn.grid(row=1+i, column=0, sticky='E')
        del_btn = settings.tk.Button(root_frame, text='Delete', command=lambda: user_del())
        del_btn.grid(row=1+i, column=1, sticky='E')


def user_del():
    print('test')


def user_edit():
    print('test')
