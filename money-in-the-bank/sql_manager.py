import requests
import sqlite3
import hashlib
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

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
    cursor.execute("INSERT INTO clients (username, password) values (?, ?)", (username, password))
    conn.commit()


def login(username, password):
    cursor.execute('''SELECT id, username, balance, message FROM
                clients WHERE username = (?) AND password = (?) LIMIT 1''', (username, password))

    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
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
