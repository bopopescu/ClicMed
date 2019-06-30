import settings


# ---------------------------------------------------------------------------------------------------------------------
# Admin Frame
def main_frame(root_frame, username_set, region):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('User Management')
    root_frame.geometry('890x430')
    root_frame.maxsize(890, 430)
    root_frame.minsize(890, 430)

    canvas = settings.tk.Canvas(root_frame, background='#3c3f41', scrollregion=(0, 0, 500, 500))
    canvas.grid(row=1, column=0, columnspan=5, sticky="nswe")
    second_frame = settings.tk.Frame(canvas, background='#3c3f41')
    second_frame.grid(row=0, column=0, sticky="nw")
    scrollbar = settings.tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=second_frame, anchor="nw", tags="second_frame")
    scrollbar.grid(row=1, column=5, sticky="nse")

    root_frame.rowconfigure(1, weight=1)
    root_frame.columnconfigure(0, weight=1)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)

    cursor.execute("SELECT DISTINCT Region FROM Users")
    region_list = list(cursor.fetchall())
    cursor.close()
    region_list.insert(0, 'None')

    cursor = cnx.cursor(buffered=True)

    if region == 'None':
        cursor.execute("SELECT * FROM Users")
    else:
        region = region[2:-3]
        cursor.execute("SELECT * FROM Users WHERE Region = %s", (region, ))

    records = cursor.fetchall()
    cursor.close()
    cnx.close()
    idx = 1

    filter1_choice = settings.tk.StringVar(root_frame)
    filter1_choice.set(region)
    username = settings.tk.StringVar()
    name = settings.tk.StringVar()
    surname = settings.tk.StringVar()
    email = settings.tk.StringVar()
    region = settings.tk.StringVar()
    groupid = settings.tk.StringVar()


    filter1 = settings.tk.Label(root_frame, text='Filter on:', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter1.grid(row=0, column=0, sticky="w")

    dropdown1 = settings.tk.OptionMenu(root_frame, filter1_choice, *region_list)
    dropdown1.grid(row=0, column=1, sticky="w")

    filtr_btn = settings.tk.Button(root_frame, text="Apply", command=lambda: main_frame(root_frame, username_set,
                                                                                        filter1_choice.get()))
    filtr_btn.grid(row=0, column=2, sticky="w")

    label0 = settings.tk.Label(second_frame, text='Id', font=("Arial", 10), fg='black', bg='white', width=2)
    label0.grid(row=1, column=3, sticky="w", padx=1, pady=1)

    label1 = settings.tk.Label(second_frame, text='username', font=("Arial", 10), fg='black', bg='white', width=10)
    label1.grid(row=1, column=4, sticky="w", padx=1, pady=1)

    label2 = settings.tk.Label(second_frame, text='Name', font=("Arial", 10), fg='black', bg='white', width=10)
    label2.grid(row=1, column=5, sticky="w", padx=1, pady=1)

    label3 = settings.tk.Label(second_frame, text='Surname', font=("Arial", 10), fg='black', bg='white', width=10)
    label3.grid(row=1, column=6, sticky="w", padx=1, pady=1)

    label4 = settings.tk.Label(second_frame, text='Email address', font=("Arial", 10), fg='black', bg='white',
                               width=30)
    label4.grid(row=1, column=7, sticky="w", padx=1, pady=1)

    label5 = settings.tk.Label(second_frame, text='Country', font=("Arial", 10), fg='black', bg='white', width=10)
    label5.grid(row=1, column=8, sticky="w", padx=1, pady=1)

    label6 = settings.tk.Label(second_frame, text='Group', font=("Arial", 10), fg='black', bg='white', width=10)
    label6.grid(row=1, column=9, sticky="w", padx=1, pady=1)

    for row in records:
        idx += 1

        edit_btn = settings.tk.Button(second_frame, text='Edit')
        edit_btn.grid(row=idx, column=0, sticky="w", padx=1, pady=1)

        del_btn = settings.tk.Button(second_frame, text='Delete', command=lambda user_id=row[0]: user_del(user_id,
                                                                                                          root_frame,
                                                                                                          username_set))
        del_btn.grid(row=idx, column=1, sticky="w", padx=1, pady=1)

        pass_btn = settings.tk.Button(second_frame, text='New Password', command=lambda user_id=row[0],
                                      email_usser=row[4]: new_pass(user_id, email_usser))
        pass_btn.grid(row=idx, column=2, sticky="w", padx=1, pady=1)

        label0 = settings.tk.Label(second_frame, text=row[0], font=("Arial", 10), fg='black', bg='grey', width=2)
        label0.grid(row=idx, column=3, sticky="w", padx=1, pady=1)

        label1 = settings.tk.Label(second_frame, text=row[1], font=("Arial", 10), fg='black', bg='grey', width=10)
        label1.grid(row=idx, column=4, sticky="w", padx=1, pady=1)

        label2 = settings.tk.Entry(second_frame, font=("Arial", 11), fg='black', bg='white', width=10)
        label2.insert(0, row[2])
        label2.grid(row=idx, column=5, sticky="w", padx=1, pady=1)

        label3 = settings.tk.Entry(second_frame, font=("Arial", 11), fg='black', bg='white', width=10)
        label3.insert(0, row[3])
        label3.grid(row=idx, column=6, sticky="w", padx=1, pady=1)

        label4 = settings.tk.Entry(second_frame, font=("Arial", 11), fg='black', bg='white', width=30)
        label4.insert(0, row[4])
        label4.grid(row=idx, column=7, sticky="w", padx=1, pady=1)

        label5 = settings.tk.Entry(second_frame, font=("Arial", 11), fg='black', bg='white', width=10)
        label5.insert(0, row[5])
        label5.grid(row=idx, column=8, sticky="w", padx=1, pady=1)

        label6 = settings.tk.Entry(second_frame, font=("Arial", 11), fg='black', bg='white', width=10)
        label6.insert(0, row[6])
        label6.grid(row=idx, column=9, sticky="w", padx=1, pady=1)

        edit_btn['command'] = lambda user_id=row[0], lname=label2, lsurname=label3, lemail=label4, lregion=label5, \
                                     lgroup=label6: user_edit(user_id, lname, lsurname, lemail, lregion, lgroup)

    idx += 1
    add_btn = settings.tk.Button(second_frame, text='Add', command=lambda: user_add(label1, label2, label3, label4,
                                                                                    label5, label6, root_frame,
                                                                                    username_set))
    add_btn.grid(row=idx, column=1, sticky="w", padx=1, pady=1)

    clear_btn = settings.tk.Button(second_frame, text='Clear', command=lambda: clear(label1, label2, label3, label4,
                                                                                     label5, label6))
    clear_btn.grid(row=idx, column=2, sticky="w", padx=1, pady=1)

    label1 = settings.tk.Entry(second_frame, textvariable=username, font=("Arial", 11), fg='black', bg='white',
                               width=10)
    label1.grid(row=idx, column=4, sticky="w", padx=1, pady=1)

    label2 = settings.tk.Entry(second_frame, textvariable=name, font=("Arial", 11), fg='black', bg='white', width=10)
    label2.grid(row=idx, column=5, sticky="w", padx=1, pady=1)

    label3 = settings.tk.Entry(second_frame, textvariable=surname, font=("Arial", 11), fg='black', bg='white', width=10)
    label3.grid(row=idx, column=6, sticky="w", padx=1, pady=1)

    label4 = settings.tk.Entry(second_frame, textvariable=email, font=("Arial", 11), fg='black', bg='white', width=30)
    label4.grid(row=idx, column=7, sticky="w", padx=1, pady=1)

    label5 = settings.tk.Entry(second_frame, textvariable=region, font=("Arial", 11), fg='black', bg='white', width=10)
    label5.grid(row=idx, column=8, sticky="w", padx=1, pady=1)

    label6 = settings.tk.Entry(second_frame, textvariable=groupid, font=("Arial", 11), fg='black', bg='white', width=10)
    label6.grid(row=idx, column=9, sticky="w", padx=1, pady=1)

    return_btn = settings.tk.Button(root_frame, text='Return', command=lambda: settings.admin_frame.admin(root_frame,
                                                                                                          username_set))
    return_btn.grid(row=2, column=3, sticky="e")

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=2, column=4, sticky="w")


# ----------------------------------------------------------------------------------------------------------------------
# User Frame


def user_del(user_id, root_frame, username_set):

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_ADMIN, password=settings.MYSQL_ADMIN_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)

    cursor.execute("DELETE FROM Users WHERE idusers = %s", (user_id, ))
    cnx.commit()
    cnx.close()

    ftp = settings.ftplib.FTP(settings.HOST)
    ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
    ftp.cwd("ClicMed/Patients")
    ftp.set_pasv(False)
    hashed_id = settings.login.password_hash(str(user_id))
    ftp.delete(hashed_id)

    settings.user_mgmt.main_frame(root_frame, username_set, 'None')


def user_edit(user_id, label2, label3, label4,label5, label6):
    name_u = label2.get()
    surname_u = label3.get()
    email_u = label4.get()
    region_u = label5.get()
    groupid_u = label6.get()

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_ADMIN, password=settings.MYSQL_ADMIN_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)

    cursor.execute("UPDATE Users SET Name = %s, LastName = %s, Email = %s, Region = %s, GroupId = %s "
                   "WHERE idusers = %s", (name_u, surname_u, email_u, region_u, groupid_u, user_id))
    cnx.commit()
    cnx.close()

    popup = settings.tk.Toplevel()
    popup.wm_title("Success!")
    ico_popup = settings.tk.PhotoImage(file=settings.ICO)
    popup.configure(background='#3c3f41')
    popup.geometry('150x130')
    popup.maxsize(150, 70)
    popup.minsize(150, 70)
    popup.grab_set()
    popup.tk.call('wm', 'iconphoto', popup._w, ico_popup)
    label = settings.tk.Label(popup, text="Update Success !", font=("Arial", 11), fg='white', bg='#3c3f41')
    label.pack(side="top", fill="x", pady=10)
    okay_btn = settings.tk.Button(popup, text="Okay", command=popup.destroy)
    okay_btn.pack()
    popup.mainloop()


def new_pass(user_id, email_user):
    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_ADMIN, password=settings.MYSQL_ADMIN_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)

    password = random_password()
    message = f"Your ClicMed account password has just been reset. To log in use {password} as password."
    send_mail(email_user, message)

    hashed_password = settings.login.password_hash(password)

    cursor.execute("UPDATE Users SET PasswordHash = %s WHERE idusers = %s", (hashed_password, user_id))
    cnx.commit()
    cnx.close()


def user_add(label1, label2, label3, label4, label5, label6, root_frame, username_set):

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_ADMIN, password=settings.MYSQL_ADMIN_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    username_u = label1.get()
    name_u = label2.get()
    surname_u = label3.get()
    email_u = label4.get()
    region_u = label5.get()
    groupid_u = label6.get()
    password = random_password()

    message = f"Your ClicMed account has just been created. To log in use {username_u} as username and {password} " \
        f"as password."
    send_mail(email_u, message)

    hashed_password = settings.login.password_hash(password)

    cursor.execute("INSERT INTO Users (Username,Name,LastName,Email,Region,GroupId, PasswordHash)"
                   " VALUES (%s,%s,%s,%s,%s,%s,%s)", (username_u, name_u, surname_u, email_u, region_u, groupid_u,
                                                      hashed_password))
    cnx.commit()
    cursor.close()

    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT idusers FROM Users WHERE username = %s", (username_u, ))
    id_user = cursor.fetchone()
    cursor.close()
    cnx.close()

    ftp = settings.ftplib.FTP(settings.HOST)
    ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
    ftp.cwd("ClicMed/Patients")
    ftp.set_pasv(False)

    hashed_id = settings.login.password_hash(str(id_user[0]))
    header = bytes("User created : " + str(settings.datetime.datetime.now()) + "\n", "UTF-8")
    bheader = settings.io.BytesIO(header)
    ftp.storbinary('STOR %s' % hashed_id, bheader)

    settings.user_mgmt.main_frame(root_frame, username_set, 'None')


def clear(label1, label2, label3, label4, label5, label6):

    label1.delete(0, settings.tk.END)
    label2.delete(0, settings.tk.END)
    label3.delete(0, settings.tk.END)
    label4.delete(0, settings.tk.END)
    label5.delete(0, settings.tk.END)
    label6.delete(0, settings.tk.END)


def random_password():
    available_char = settings.string.ascii_letters + settings.string.digits
    passwd = ""
    for i in range(8):
        passwd += available_char[settings.random.randint(0, len(available_char) - 1)]
    return passwd


def send_mail(receiver_email, message):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = settings.EMAIL
    password = settings.EMAIL_PWD

    context = settings.ssl.create_default_context()
    with settings.smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
