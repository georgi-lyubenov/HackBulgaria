from create_db import *
from random import randrange
from sqlalchemy import update

engine = create_engine("sqlite:///expressions_game.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
session.add_all([
    Operation(name="mult", sign='x'),
    Operation(name="pow", sign='^'),
    Operation(name="add", sign='+'),
    Operation(name="subtract", sign='-'),
    Operation(name="div", sign=':')])
session.commit()


class Expression():
    def __init__(self, val1, oper, val2):
        self.value1 = val1
        self.oper = oper
        self.value2 = val2
        session.query(Operation).filter(Operation.sign == self.oper).update({'value1': self.value1})
        session.query(Operation).filter(Operation.sign == self.oper).update({'value2': self.value2})
        session.commit()

    def solve(self):
        obj = session.query(Operation).filter(Operation.sign == self.oper).one()
        if obj.sign == 'x':
            session.query(Operation).filter(Operation.sign == self.oper).update({'result': obj.value1 * obj.value2})
        elif obj.sign == '^':
            session.query(Operation).filter(Operation.sign == self.oper).update({'result': obj.value1 ** obj.value2})
        elif obj.sign == '+':
            session.query(Operation).filter(Operation.sign == self.oper).update({'result': obj.value1 + obj.value2})
        elif obj.sign == '-':
            session.query(Operation).filter(Operation.sign == self.oper).update({'result': obj.value1 - obj.value2})
        elif obj.sign == ':':
            session.query(Operation).filter(Operation.sign == self.oper).update({'result': obj.value1 // obj.value2})
        number = obj.result
        session.commit()
        return number


def main():
    i = 1
    print("\nWelcome to the Do you even math? game!\n")
    print("Here are your options:")
    while True:
        print("- start")
        print("- highscores")
        option = input("?>")
        if option == "start":
            player = input("Enter your playername>")
            obj = Highscore(name=player)
            session.add(obj)
            session.commit()
            print("Welcome {}! Let the game begin!".format(player))
            while True:
                print("Question #{}:".format(i))
                value1 = randrange(1, 10)
                value2 = randrange(1, 10)
                oper = randrange(1, 5)
                if oper == 1:
                    operation = 'x'
                elif oper == 2:
                    operation = '^'
                elif oper == 3:
                    operation = '+'
                elif oper == 4:
                    operation = '-'
                elif oper == 5:
                    operation = ':'
                print("What is the answer to {} {} {}?".format(value1, operation, value2))
                expr = Expression(value1, operation, value2)
                res = expr.solve()
                answer = input("?>")
                if answer == str(res):
                    print("Correct")
                    i += 1
                else:
                    score = obj.calc_score(i)
                    print("Incorrect! Ending game. You score is: {}".format(score))
                    session.query(Highscore).filter(Highscore.name == player).update({'score': score})
                    break
        elif option == "highscores":
            print("This is the current top10:")
            result = session.query(Highscore.id, Highscore.name, Highscore.score)
            for row in result:
                print("{} with {} points".format(row[1], row[2]))
        else:
            print("invalid input")

if __name__ == '__main__':
    main()
