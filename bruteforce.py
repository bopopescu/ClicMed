# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA - Karthike EZHILARASAN - Alexandre KOSTAS
# Classe: SRC1 - 3E
# Projet - ClicMed

import settings


def main_frame(root_frame, username, group):
    settings.login.clear_window(root_frame)
    root_frame.configure(background='#3c3f41')

    root_frame.title('Bruteforcer')
    root_frame.geometry('290x290')
    root_frame.maxsize(290, 290)
    root_frame.minsize(290, 290)

    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT DISTINCT Username FROM Users")
    username_list = list(cursor.fetchall())
    cursor.close()

    filter1_choice = settings.tk.StringVar(root_frame)
    filter1_choice.set(username)

    filter1 = settings.tk.Label(root_frame, text='Select user : ', font=("Arial", 10), fg='white', bg='#3c3f41')
    filter1.grid(row=0, column=0, pady=2, sticky="w")

    dropdown1 = settings.tk.OptionMenu(root_frame, filter1_choice, *username_list)
    dropdown1.grid(row=0, column=1, pady=2, sticky="w")
    dropdown1.config(borderwidth=0)

    filtr_btn = settings.tk.Button(root_frame, text="Apply",
                                   command=lambda: bruteforcer(filter1_choice.get()[2:-3], username, group))
    filtr_btn.grid(row=0, column=1, pady=2, sticky="w", padx=100)


def bruteforcer(username_target, username, group):

    found = False

    available_char = settings.string.ascii_letters + settings.string.digits
    cnx = settings.mysql.connect(host=settings.HOST, user=settings.MYSQL_USER, password=settings.MYSQL_USER_PWD,
                                 database=settings.MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT PasswordHash FROM Users WHERE Username = %s", (username_target, ))
    hashed_user_password = str(cursor.fetchall()[0])[2:-3]
    cursor.close()
    cnx.close()

    for length in range(8, 9):
        password_to_attempt = settings.itertools.product(available_char, repeat=length)

        for attempt in password_to_attempt:
            attempt = ''.join(attempt)
            hashed_attempt = settings.login.password_hash(attempt)
            if hashed_attempt == hashed_user_password:
                found = True
                break

        if found:
            break
