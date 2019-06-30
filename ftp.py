import settings


def main_frame(root_frame, username):

    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med Admin')
    root_frame.geometry('450x330')
    root_frame.maxsize(650, 330)
    root_frame.minsize(650, 330)

    canvas = settings.tk.Canvas(root_frame, background='#3c3f41', scrollregion=(0, 0, 250, 250))
    canvas.grid(row=1, column=3, rowspan=7, sticky="nw")
    second_frame = settings.tk.Frame(canvas, background='#3c3f41')
    second_frame.grid(row=0, column=0, sticky="nw")
    scrollbar = settings.tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=second_frame, anchor="nw", tags="second_frame")
    scrollbar.grid(row=1, column=4, rowspan=7, sticky="nse")

    # root_frame.rowconfigure(1, weight=1)
    root_frame.columnconfigure(3, weight=1)

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

    filter1_choice = settings.tk.StringVar(root_frame)
    filter1_choice.set(username)

    filter1 = settings.tk.Label(root_frame, text='Filter on:', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter1.grid(row=0, column=0, pady=2, sticky="w")

    dropdown1 = settings.tk.OptionMenu(root_frame, filter1_choice, *username_list)
    dropdown1.grid(row=0, column=1, pady=2, sticky="w")
    dropdown1.config(borderwidth=0)

    filtr_btn = settings.tk.Button(root_frame, text="Apply", command=lambda: main_frame(root_frame,
                                                                                        filter1_choice.get()[2:-3]))
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

    upload_btn = settings.tk.Button(root_frame, width=2, text='Upload', command=lambda: upload_file())
    upload_btn.grid(row=8, column=3, pady=2, sticky='we')

    return_btn = settings.tk.Button(root_frame, text='Return', command=lambda: settings.login.login_window(root_frame))
    return_btn.grid(row=8, column=3, pady=2, sticky='se')

    exit_btn = settings.tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=8, column=4, pady=2, sticky='sw')

    def upload_file():
        raw_filename = settings.fdialog.askopenfilename(initialdir="/", title="Select file")
        ftp = settings.ftplib.FTP(settings.HOST)
        ftp.login(user=settings.FTP_USER, passwd=settings.FTP_PWD)
        ftp.cwd("ClicMed/Files")
        ftp.set_pasv(False)
        print(ftp.pwd())
        file_name = raw_filename
        file = open(file_name, 'rb')
        ftp.storbinary('STOR ' + file_name, file)
        file.quit()

    # def upload_file_to_FTP():
    #     ##    first thing we do is connect to the ftp host
    #
    #     command = 'echo'
    #
    #     client = settings.paramiko.SSHClient()
    #     client.load_system_host_keys()
    #     client.set_missing_host_key_policy(settings.paramiko.WarningPolicy)
    #
    #     client.connect(settings.HOST, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)
    #
    #     stdin, stdout, stderr = client.exec_command(command)
    #     ftp = FTP('')
    #     ftp.login(user='', passwd='')
    #     ftp.cwd("")
    #     ftp.set_pasv(False)
    #     file_name = self.raw_filename
    #     file = open(file_name, 'rb')
    #     ftp.storbinary('STOR ' + file_name, file)