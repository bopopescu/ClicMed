import hashlib
import os
import sys
import tkinter as tk
import mysql.connector as mysql

# Settings variables
HOST = 'benjamin.beyerle.fr'
MYSQL_USER = 'ClicMed-user'
MYSQL_USER_PWD = 'clicmedUs3r'
MYSQL_DB = 'ClicMed'
ICO = os.path.join(sys.path[0], "Resources/ClicMed.gif")
ICO_ERROR = os.path.join(sys.path[0], "Resources/incorrect2.png")
FONT = os.path.join(sys.path[0], "Resources/georgia.ttf")


# Hashing password for security
def password_hash(password_input):
    byte_password = password_input.encode()
    hashed_password = hashlib.md5(byte_password).hexdigest()
    return hashed_password


def clear_window(root_frame):
    for widget in root_frame.winfo_children():
        widget.destroy()


# Window for log in
def login_window(root_frame):

    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med')
    root_frame.geometry('250x130')
    root_frame.maxsize(250, 130)
    root_frame.minsize(250, 130)

    label1 = tk.Label(root_frame, text='Login', font=("Arial", 30), fg='white', bg='#3c3f41')
    label1.grid(column=1, columnspan=3, sticky='W')

    label2 = tk.Label(root_frame, text='Username :', font=("Arial", 10), fg='white', bg='#3c3f41')
    label2.grid(row=1, sticky='E')

    label3 = tk.Label(root_frame, text='Password :', font=("Arial", 10), fg='white', bg='#3c3f41')
    label3.grid(row=2, sticky='E')

    user = tk.Entry(root_frame, width=15)
    user.grid(row=1, column=1, columnspan=2, sticky='W')
    user.focus()

    password = tk.Entry(root_frame, show="*", width=15)
    password.grid(row=2, column=1, columnspan=2, sticky='W')

    login_btn = tk.Button(root_frame, text='Login', command=lambda: check_user(user.get(), password.get(),
                                                                               password, root_frame))
    login_btn.grid(row=3, column=1, sticky='E')

    exit_btn = tk.Button(root_frame, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=3, column=2, sticky='W')


# Function to verify if user is in the database (username + password)
def check_user(username, password_input, password_label, root_frame):

    hashed_password = password_hash(password_input)

    cnx = mysql.connect(host=HOST, user=MYSQL_USER, password=MYSQL_USER_PWD, database=MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT Username, PasswordHash, GroupId FROM Users WHERE Username = %s AND PasswordHash = %s",
                   (username, hashed_password))
    records = cursor.fetchall()
    cursor.close()
    cnx.close()

    try:
        group_id = records[0][2]
    except IndexError:
        incorrect = tk.Label(root_frame, image=img_error, background='#3c3f41')
        incorrect.grid(row=0, column=0, sticky='W')

        password_label.delete(0, tk.END)
    else:
        if group_id == 0:
            admin(root_frame)
        else:
            user(root_frame)


# Admin panel with all the tools and full access
def admin(root_frame):
    clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med Admin')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    login_btn = tk.Button(root_frame, text='User Management', command=lambda: user_mgmt(root_frame))
    login_btn.grid(row=3, column=1, sticky='E')


# User panel with less tools and restricted access
def user(root_frame):
    clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('Clic Med User')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)


def user_mgmt(root_frame):
    clear_window(root_frame)
    root_frame.configure(background='#3c3f41')
    root_frame.title('User Management')
    root_frame.geometry('450x330')
    root_frame.maxsize(450, 330)
    root_frame.minsize(450, 330)

    cnx = mysql.connect(host=HOST, user=MYSQL_USER, password=MYSQL_USER_PWD, database=MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    nb_rows = cursor.rowcount
    cursor.close()
    cnx.close()

    for i in range(0, nb_rows):
        edit_btn = tk.Button(root_frame, text='Edit', command=lambda: user_edit())
        edit_btn.grid(row=1+i, column=0, sticky='E')
        del_btn = tk.Button(root_frame, text='Delete', command=lambda: user_del())
        del_btn.grid(row=1+i, column=1, sticky='E')


def user_del():
    print('test')


def user_edit():
    print('test')

# ---------------------------------------------------------------------------------------------------------------------
# Main execution of program
root = tk.Tk()
img_ico = tk.PhotoImage(file=ICO)
img_error = tk.PhotoImage(file=ICO_ERROR)
root.tk.call('wm', 'iconphoto', root._w, img_ico)
login_window(root)
root.mainloop()
