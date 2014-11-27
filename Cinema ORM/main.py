from cinema import *

engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)

session.add_all([
    Movie(name="Her", rating=8.3),
    Movie(name="Wreck It Ralph", rating=7.8),
    Movie(name="The Hunger Games:Catching Fire", rating=7.9),
    Projection(movie_id=1, type="3D", date="2014-04-01", time="19:10"),
    Projection(movie_id=1, type="2D", date="2014-04-01", time="19:00"),
    Projection(movie_id=1, type="4DX", date="2014-04-02", time="21:00"),
    Projection(movie_id=3, type="2D", date="2014-04-05", time="20:20"),
    Projection(movie_id=2, type="3D", date="2014-04-02", time="22:00"),
    Projection(movie_id=2, type="2D", date="2014-04-02", time="19:30"),
    Reservation(username="Rado", projection_id=1, row=2, col=1),
    Reservation(username="Rado", projection_id=1, row=3, col=5),
    Reservation(username="Rado", projection_id=1, row=7, col=8),
    Reservation(username="Ivo", projection_id=3, row=1, col=1),
    Reservation(username="Ivo", projection_id=3, row=1, col=2),
    Reservation(username="Someone", projection_id=5, row=2, col=3),
    Reservation(username="Someone", projection_id=5, row=2, col=4)])
session.commit()

seats = [['.' for row in range(10)] for elem in range(10)]


class Cinema():
    def show_movies(self):
        result = session.query(Movie.id, Movie.name, Movie.rating)
        for row in result:
            print('{} - {} - {}'.format(row[0], row[1], row[2]))

    def show_movie_projections(self, needed_id):
        result = session.query(Projection.id, Projection.movie_id, Projection.type, Projection.date, Projection.time)\
            .filter(Movie.id == Projection.movie_id, Movie.id == needed_id)
        for row in result:
            print('{} - {} - {} - {}'.format(row[0], row[2], row[3], row[4]))

    def print_seats(self):
        for i in seats:
            print(' '.join(i))

    def make_reservation(self):
        name = input("name>")
        number_of_tickets = input("number_of_tickets>")
        self.show_movies()
        movie = input("choose a movie>")
        self.show_movie_projections(movie)
        projection = input("choose a projection>")
        self.print_seats()
        for index in range(int(number_of_tickets)):
            row = input("choose a row>")
            col = input("choose a col>")
            seat = (row, col)
            if seats[int(row)][int(col)] != "x":
                seats[int(row)][int(col)] = "x"
                reserv = Reservation(username=name, projection_id=projection, row=seat[0], col=seat[1])
                session.add(reserv)
                session.commit()
            else:
                print("The seat is taken")


def main():
    my_cinema = Cinema()
    while True:
        comm = input("command>")
        if comm == "show movies":
            my_cinema.show_movies()
        elif comm == "show_movie_projections":
            needed_movie_id = input("choose movie id>")
            my_cinema.show_movie_projections(needed_movie_id)
        elif comm == "make reservation":
            my_cinema.make_reservation()
        else:
            "invalid input"

if __name__ == '__main__':
    main()
