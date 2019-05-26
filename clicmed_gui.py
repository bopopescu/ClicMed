import tkinter as tk
import mysql.connector as mysql
import hashlib
import os
import sys

# Settings variables
HOST = 'benjamin.beyerle.fr'
MYSQL_USER = 'ClicMed-user'
MYSQL_USER_PWD = 'clicmedUs3r'
MYSQL_DB = 'ClicMed'
ICO = os.path.join(sys.path[0], "Resources/ClicMed.gif")
ICO_ERROR = os.path.join(sys.path[0], "Resources/incorrect2.png")


# Hashing password for security
def password_hash(password_input):
    byte_password = password_input.encode()
    hashed_password = hashlib.md5(byte_password).hexdigest()
    return hashed_password


# Window for log in
def login_window(root_frame):

    login_f = tk.Toplevel()
    login_f.configure(background='#3c3f41')
    login_f.tk.call('wm', 'iconphoto', login_f._w, img_ico)
    login_f.title('Clic Med')
    login_f.geometry('250x130')
    login_f.maxsize(250, 130)
    login_f.minsize(250, 130)

    label1 = tk.Label(login_f, text='Login', font=("Georgia", 30), fg='white', bg='#3c3f41')
    label1.grid(column=1, columnspan=2, sticky='W')

    label2 = tk.Label(login_f, text='Username :', font=("Georgia", 10), fg='white', bg='#3c3f41')
    label2.grid(row=1, sticky='E')

    label3 = tk.Label(login_f, text='Password :', font=("Georgia", 10), fg='white', bg='#3c3f41')
    label3.grid(row=2, sticky='E')

    user = tk.Entry(login_f)
    user.grid(row=1, column=1, columnspan=2, sticky='W')
    user.focus()

    password = tk.Entry(login_f, show="*")
    password.grid(row=2, column=1, columnspan=2, sticky='W')

    login_btn = tk.Button(login_f, text='Login', command=lambda: check_user(user.get(), password.get(), login_f,
                                                                            password, root_frame))
    login_btn.grid(row=3, column=1, sticky='E')

    exit_btn = tk.Button(login_f, text='Exit', command=root_frame.destroy)
    exit_btn.grid(row=3, column=2, sticky='W')


# Function to verify if user is in the database (username + password)
def check_user(username, password_input, login_frame, password_label, root_frame):

    hashed_password = password_hash(password_input)

    cnx = mysql.connect(host=HOST, user=MYSQL_USER, password=MYSQL_USER_PWD, database=MYSQL_DB)
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT Username, PasswordHash, GroupId FROM Users WHERE Username = \'%s\' AND PasswordHash = \'%s\'" %
             (username, hashed_password))
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    cnx.close()

    try:
        group_id = records[0][2]
    except IndexError:
        incorrect = tk.Label(login_frame, image=img_error, background='#3c3f41')
        incorrect.grid(row=1, column=4, sticky='W')

        password_label.delete(0, tk.END)
    else:
        root_frame.deiconify()
        fail_img = tk.Label(root_frame, image=tk.PhotoImage(ICO))
        fail_img.grid()
        login_frame.destroy()
        return group_id


# Main execution of program
root = tk.Tk()
img_ico = tk.PhotoImage(file=ICO)
img_error = tk.PhotoImage(file=ICO_ERROR)
root.withdraw()
if login_window(root) == 1:
    print('admin')
else:
    print('user')
root.mainloop()
