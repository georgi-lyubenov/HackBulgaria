from random import randrange

board = [['.' for row in range(3)] for elem in range(3)]


class Game():
    def row(self):
        if board[0][0] == board[0][1] == board[0][2] != '.'\
            or board[1][0] == board[1][1] == board[1][2] != '.'\
                or board[2][0] == board[2][1] == board[2][2] != '.':
            return True

    def col(self):
        if board[0][0] == board[1][0] == board[2][0] != '.'\
            or board[0][1] == board[1][1] == board[2][1] != '.'\
                or board[0][2] == board[1][2] == board[2][2] != '.':
            return True

    def cross(self):
        if board[0][0] == board[1][1] == board[2][2] != '.'\
                or board[0][2] == board[1][1] == board[2][0] != '.':
            return True

    def print_board(self):
        for i in board:
            print(' '.join(i))

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    return False
        return True

    def check_for_winner(self):
        if self.row() is True or self.col() is True or self.cross() is True:
            return True
        return False

    def AI_move(self):
        if self.is_full() is True:
            return
        number = randrange(1, 9)
        if number == 1:
            if board[0][0] == '.':
                board[0][0] = 'O'
            else:
                self.AI_move()
        if number == 2:
            if board[0][1] == '.':
                board[0][1] = 'O'
            else:
                self.AI_move()
        if number == 3:
            if board[0][2] == '.':
                board[0][2] = 'O'
            else:
                self.AI_move()
        if number == 4:
            if board[1][0] == '.':
                board[1][0] = 'O'
            else:
                self.AI_move()
        if number == 5:
            if board[1][1] == '.':
                board[1][1] = 'O'
            else:
                self.AI_move()
        if number == 6:
            if board[1][2] == '.':
                board[1][2] = 'O'
            else:
                self.AI_move()
        if number == 7:
            if board[2][0] == '.':
                board[2][0] = 'O'
            else:
                self.AI_move()
        if number == 8:
            if board[2][1] == '.':
                board[2][1] = 'O'
            else:
                self.AI_move()
        if number == 9:
            if board[2][2] == '.':
                board[2][2] = 'O'
            else:
                self.AI_move()


def main():
    g = Game()
    g.print_board()
    while True:
        if g.is_full() is True:
            print("Draw Game!")
        row = input("choose a row>")
        col = input("choose a col>")
        if int(row) >= 4 or int(col) >= 4:
            print("invalid move")
            continue
        else:
            if board[int(row) - 1][int(col) - 1] == '.':
                board[int(row) - 1][int(col) - 1] = "X"
                if g.check_for_winner() is True:
                    print("Player Wins!")
                    break
            else:
                print("invalid move")
        g.AI_move()
        g.print_board()
        if g.check_for_winner() is True:
            print("The AI wins")
            break
if __name__ == '__main__':
    main()
