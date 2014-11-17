import sql_manager
import hashlib
import getpass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            hash_object = hashlib.sha1(password.encode()).digest()
            sql_manager.register(username, str(hash_object))

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            hash_object = hashlib.sha1(password.encode()).digest()
            logged_user = sql_manager.login(username, str(hash_object))

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")
        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            hash_object = hashlib.sha1(new_pass.encode()).digest()
            sql_manager.change_pass(str(hash_object), logged_user.get_username())

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)
        elif command == 'show-message':
            print(logged_user.get_message())
        elif command == 'deposit':
            amount = input("amount>")
            sql_manager.deposit(logged_user.get_username(), amount)
        elif command == 'withdraw':
            amount = input("amount>")
            sql_manager.withdraw(logged_user.get_username(), amount)
        elif command == 'balance':
            print(sql_manager.balance(str(logged_user.get_username())))
        elif command == 'show clients':
            sql_manager.show_clients()

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("deposit - for depositting money")
            print("withdraw - for withdrowing money")
            print("balance - for showing balance")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
