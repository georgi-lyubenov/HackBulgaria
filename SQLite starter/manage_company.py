import sqlite3


def list_employees():
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM my_company")
    for row in result:
        print('{} - {} - {}'.format(row[0], row[1], row[-1]))


def monthly_spending():
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM my_company")
    total = 0
    for row in result:
        total += row[2]
    return total


def yearly_spending():
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM my_company")
    total = 0
    for row in result:
        total = total + row[2] * 12 + row[3]
    return total


def add_employee():
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()

    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")

    cursor.execute('''INSERT INTO my_company
        (id,name,monthly_salary,yearly_bonus,position)
        VALUES(?,?,?,?,?)''', (6, name, monthly_salary, yearly_bonus, position))
    conn.commit()


def delete_employee():
    worker_id = input("id>")
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM my_company WHERE id = ? ''', (worker_id))
    conn.commit()


def update_employee():
    worker_id = input("id>")
    conn = sqlite3.connect("my_company.db")
    cursor = conn.cursor()
    name = input("name>")
    monthly_salary = input("monthly_salary>")
    yearly_bonus = input("yearly_bonus>")
    position = input("position>")
    cursor.execute('''UPDATE my_company SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ? WHERE id = ? ''',
                    (name, monthly_salary, yearly_bonus, position, worker_id))
    conn.commit()


def main():
    while True:
        comm = input("command>")
        if comm == "list_employees":
            list_employees()
        elif comm == "monthly_spending":
            print(monthly_spending())
        elif comm == "yearly_spending":
            print(yearly_spending())
        elif comm == "add_employee":
            add_employee()
        elif comm == "delete_employee":
            delete_employee()
        elif comm == "update_employee":
            update_employee()
        else:
            "invalid input"

if __name__ == '__main__':
    main()
