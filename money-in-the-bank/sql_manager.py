import requests
import sqlite3
import hashlib
from Client import Client
import smtplib
from email.mime.text import MIMEText
import random
import getpass

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    cursor.execute("UPDATE clients SET message = ? WHERE id = ?", (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if (any(x.isupper() for x in new_pass) and any(x.islower() for x in new_pass)
            and any(x.isdigit() for x in new_pass) and len(new_pass) >= 7)\
            and str(logged_user) not in new_pass\
            and any((c in '!@#$%^&*+-') for c in new_pass):
        cursor.execute("UPDATE clients SET password = ? WHERE id = ?", (new_pass, logged_user.get_id()))
        conn.commit()
    else:
        print("your pass is not strong enough")


def register(username, password):
    email = input("email> ")
    cursor.execute("INSERT INTO clients (username, password, email) values (?, ?, ?)", (username, password, email,))
    conn.commit()


def send_email(to_username):
    cursor.execute('''SELECT email FROM
            clients WHERE username = (?)''', (to_username,))
    receiver = cursor.fetchone()
    #textfile = "test_message.txt"
    #fp = open(textfile, 'r+')
    #msg = MIMEText(fp.read())
    #fp.close()
    #msg['Subject'] = 'The contents of %s' % textfile
    msg = MIMEText(str(random.randint(1, 100)))
    hash_object = hashlib.sha1(msg.encode()).digest()
    cursor.execute("UPDATE clients SET password = ? WHERE username = ?", (str(hash_object), to_username,))
    conn.commit()
    msg['Subject'] = "test"
    msg['From'] = 'georgi_lyubenov@mail.bg'
    msg['To'] = [str(receiver[0])]

    s = smtplib.SMTP('smtp.mail.bg:465')
    s.sendmail(msg['From'], msg['To'], hash_object.as_string())
    s.quit()
    code = input("enter the code you have received> ")
    if hash_object == code:
        print("You have permission the change your password")
        new_pass = getpass.getpass("Enter your new password: ")
        hash_object2 = hashlib.sha1(new_pass.encode()).digest()
        cursor.execute("UPDATE clients SET password = ? WHERE username = ?", (str(hash_object2), to_username,))
        conn.commit()
    print("you can login with your neww password")


def login(username, password):
    cursor.execute('''SELECT id, username, balance, message, email FROM
                clients WHERE username = (?) AND password = (?) LIMIT 1''', (username, password))

    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False


def deposit(username, amount):
    cursor.execute('''UPDATE clients SET balance = balance + ?
                    WHERE username = ?''', (amount, username,))
    conn.commit()


def withdraw(username, amount):
    current_value = cursor.execute("SELECT balance FROM clients WHERE username = ?", (username,))
    for row in current_value:
        if float(row[0]) > float(amount):
            cursor.execute('''UPDATE clients SET balance = balance - ?
                        WHERE username = ?''', (amount, username,))
            conn.commit()
        else:
            print("not enough money")


def balance(username):
    result = cursor.execute("SELECT balance FROM clients WHERE username = ?", (username, ))
    for row in result:
        return ('your balance is {}'.format(row[0]))


def show_clients():
    result = cursor.execute("SELECT * FROM clients")
    for row in result:
        print('{} - {} - {} - {}'.format(row[0], row[1], row[3], row[4]))
