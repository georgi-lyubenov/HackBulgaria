import sqlite3
conn = sqlite3.connect("tables.db")
cursor = conn.cursor()

seats = [['.' for row in range(10)] for elem in range(10)]


def show_movies():
    conn = sqlite3.connect("tables.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT * FROM movies ORDER BY rating")
    for row in result:
        print('{} - {} - {}'.format(row[0], row[1], row[-1]))


def show_movie_projections(movie_id_param):
    conn = sqlite3.connect("tables.db")
    cursor = conn.cursor()
    result = cursor.execute('''SELECT * FROM projections INNER JOIN movies
                            ON movies.id = projections.movie_id WHERE movies.id = ?''', (movie_id_param,))
    for row in result:
        print('{} - {} - {} - {}'.format(row[0], row[2], row[3], row[4]))


def print_seats():
    for i in seats:
        print(' '.join(i))


def make_reservation():
    name = input("name>")
    number_of_tickets = input("number_of_tickets>")
    show_movies()
    movie = input("choose a movie>")
    show_movie_projections(movie)
    projection = input("choose a projection>")
    print_seats()
    for index in range(int(number_of_tickets)):
        row = input("choose a row>")
        col = input("choose a col>")
        seat = (row, col)
        if seats[int(row)][int(col)] != "x":
            seats[int(row)][int(col)] = "x"
            cursor.execute('''INSERT INTO reservations (username, projection_id, row, col)
                         VALUES (?, ?, ?, ?)''', (name, projection, seat[0], seat[1],))
            conn.commit()
        else:
            print("The seat is taken")


def main():
    print_seats()
    while True:
        comm = input("command>")
        if comm == "show movies":
            show_movies()
        elif comm == "show_movie_projections":
            needed_movie_id = input("choose movie id>")
            show_movie_projections(needed_movie_id)
        elif comm == "make reservation":
            make_reservation()
        else:
            "invalid input"

if __name__ == '__main__':
    main()
