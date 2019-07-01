import settings


def main_frame(root_frame, username, group):

    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('File Manager')
    root_frame.geometry('450x330')
    root_frame.maxsize(650, 330)
    root_frame.minsize(650, 330)

    root_frame.columnconfigure(3, weight=1)

    canvas = settings.tk.Canvas(root_frame, background='white', )
    canvas.grid(row=1, column=3, rowspan=7, sticky="nw")
    second_frame = settings.tk.Frame(canvas, background='white')
    second_frame.grid(row=0, column=0, sticky='nw')
    scrollbar = settings.tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=second_frame, anchor="nw", tags="second_frame")
    file_listbox = settings.tk.Listbox(second_frame, bd=0, selectmode='SINGLE',
                                       font=("Arial", 10), fg='white', bg='#3c3f41', height=640, width=330)
    file_listbox.grid(sticky='nw')
    scrollbar.grid(row=1, column=4, rowspan=7, sticky="nse")
    second_frame.columnconfigure(0, weight=1)
    second_frame.rowconfigure(0, weight=1)
    canvas.columnconfigure(0, weight=1)
    canvas.rowconfigure(0, weight=1)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT DISTINCT Username FROM Users")
    username_list = list(cursor.fetchall())
    cursor.close()

    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM Users WHERE Username = %s", (username,))
    infos = cursor.fetchall()
    cursor.close()

    cnx.close()

    if group == 0:
        filter1_choice = settings.tk.StringVar(root_frame)
        filter1_choice.set(username)

        filter1 = settings.tk.Label(root_frame, text='Select user:', font=("Arial", 10), fg='white', bg='#3c3f41')
        filter1.grid(row=0, column=0, pady=2, sticky="w")

        dropdown1 = settings.tk.OptionMenu(root_frame, filter1_choice, *username_list)
        dropdown1.grid(row=0, column=1, pady=2, sticky="w")
        dropdown1.config(borderwidth=0)

        filtr_btn = settings.tk.Button(root_frame, text="Apply",
                                       command=lambda: main_frame(root_frame, filter1_choice.get()[2:-3], group))
        filtr_btn.grid(row=0, column=1, pady=2, sticky="w", padx=100)

    labelFile = settings.tk.Label(root_frame, text='File :', font=("Arial", 10), fg='white', bg='#3c3f41')
    labelFile.grid(row=0, column=3, pady=2, sticky="w")

    label00 = settings.tk.Label(root_frame, text='Id :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label00.grid(row=1, column=0, sticky="w", padx=1, pady=1)
    label01 = settings.tk.Label(root_frame, text=infos[0][0], font=("Arial", 10), fg='black', bg='white', width=10)
    label01.grid(row=1, column=1, sticky="w", padx=1, pady=1)

    label10 = settings.tk.Label(root_frame, text='Username :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label10.grid(row=2, column=0, sticky="w", padx=1, pady=1)
    label11 = settings.tk.Label(root_frame, text=infos[0][1], font=("Arial", 10), fg='black', bg='white', width=10)
    label11.grid(row=2, column=1, sticky="w", padx=1, pady=1)

    label20 = settings.tk.Label(root_frame, text='Fist Name :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label20.grid(row=3, column=0, sticky="w", padx=1, pady=1)
    label21 = settings.tk.Label(root_frame, text=infos[0][2], font=("Arial", 10), fg='black', bg='white', width=10)
    label21.grid(row=3, column=1, sticky="w", padx=1, pady=1)

    label30 = settings.tk.Label(root_frame, text='Last Name :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label30.grid(row=4, column=0, sticky="w", padx=1, pady=1)
    label31 = settings.tk.Label(root_frame, text=infos[0][3], font=("Arial", 10), fg='black', bg='white', width=10)
    label31.grid(row=4, column=1, sticky="w", padx=1, pady=1)

    label40 = settings.tk.Label(root_frame, text='Email :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label40.grid(row=5, column=0, sticky="w", padx=1, pady=1)
    label41 = settings.tk.Label(root_frame, text=infos[0][4], font=("Arial", 10), fg='black', bg='white', width=30)
    label41.grid(row=5, column=1, sticky="w", padx=1, pady=1)

    label50 = settings.tk.Label(root_frame, text='Country :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label50.grid(row=6, column=0, sticky="w", padx=1, pady=1)
    label51 = settings.tk.Label(root_frame, text=infos[0][5], font=("Arial", 10), fg='black', bg='white', width=10)
    label51.grid(row=6, column=1, sticky="w", padx=1, pady=1)

    label60 = settings.tk.Label(root_frame, text='Group :', font=("Arial", 10), fg='white', bg='#3c3f41', width=10)
    label60.grid(row=7, column=0, sticky="w", padx=1, pady=1)
    label61 = settings.tk.Label(root_frame, text=infos[0][6], font=("Arial", 10), fg='black', bg='white', width=10)
    label61.grid(row=7, column=1, sticky="w", padx=1, pady=1)

    upload_btn = settings.tk.Button(root_frame, text='Upload', command=lambda: upload_file(infos, root_frame, username))
    upload_btn.grid(row=8, column=3, pady=2, sticky='w')

    upload_btn = settings.tk.Button(root_frame, text='Download',
                                    command=lambda: download_file(file_listbox.get(file_listbox.curselection())))
    upload_btn.grid(row=8, column=3, pady=2, padx=60, sticky='w')

    if group == 0:
        return_btn = settings.tk.Button(root_frame, text='Return',
                                        command=lambda: settings.menu.main_frame(root_frame, username, group))
        return_btn.grid(row=8, column=3, pady=2, sticky='se')
    else:
        return_btn = settings.tk.Button(root_frame, text='Return',
                                        command=lambda: settings.login.login_window(root_frame))
        return_btn.grid(row=8, column=3, pady=2, sticky='se')

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=8, column=4, pady=2, sticky='sw')

    ftp = settings.ftplib.FTP(settings.HOST)
    ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
    ftp.cwd("ClicMed/Patients")
    ftp.set_pasv(True)
    hashed_id = settings.login.password_hash(str(infos[0][0]))
    ftp.retrbinary('RETR %s' % hashed_id, open("tmp.txt", 'wb').write)
    settings.login.decrypt("tmp.txt")
    f = open("tmp.txt", 'r')
    file_list = f.readlines()[1:]
    f.close()
    settings.os.remove("tmp.txt")
    idx = 0

    for file_name in file_list:
        clear_name = settings.login.decode(settings.CRYPTO_PWD, file_name)
        file_listbox.insert(idx, clear_name)
        idx += 1


def upload_file(infos, root_frame, username):
    raw_filename = settings.fdialog.askopenfilename(initialdir="~/Pictures", title="Select file")
    filename = settings.os.path.basename(raw_filename)
    ts_date = str('{date:%Y-%m-%d_%H-%M-%S}'.format(date=settings.datetime.datetime.now() ))
    filename = ts_date + '_' + filename
    hashed_filename = settings.login.encode(settings.CRYPTO_PWD, filename)
    hashed_id = settings.login.password_hash(str(infos[0][0]))
    settings.shutil.copyfile(raw_filename, hashed_filename)

    ftp = settings.ftplib.FTP(settings.HOST)
    ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
    ftp.cwd("ClicMed/Files")
    ftp.set_pasv(True)

    file = open(hashed_filename, 'rb')
    ftp.storbinary('STOR %s' % hashed_filename, file)
    file.close()
    settings.os.remove(hashed_filename)

    ftp.cwd("../Patients")
    ftp.retrbinary("RETR %s" % hashed_id, open("tmp.txt", 'wb').write)
    settings.login.decrypt("tmp.txt")
    tmp = open("tmp.txt", "a+")
    tmp.write(str(hashed_filename) + "\n")
    tmp.close()
    settings.login.crypt("tmp.txt")
    file = open("tmp.txt", 'rb')
    ftp.storbinary('STOR %s' % hashed_id, file)
    file.close()
    settings.os.remove("tmp.txt")
    ftp.close()
    main_frame(root_frame, username, group)


def download_file(file_selected):
    destination = settings.fdialog.asksaveasfilename(title='Save as', initialfile=file_selected)
    ftp = settings.ftplib.FTP(settings.HOST)
    ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
    ftp.cwd("ClicMed/Files")
    ftp.set_pasv(False)
    hashed_filename = settings.login.encode(settings.CRYPTO_PWD, file_selected)
    ftp.retrbinary("RETR %s" % hashed_filename, open(destination, 'wb').write)
