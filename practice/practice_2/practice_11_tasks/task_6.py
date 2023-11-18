class Cell:
    def __init__(self, number):
        self.is_occupied = False
        self.number = number
        self.symbol = None


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(9)]

    def change_cell_state(self, cell_number, symbol):
        if not self.cells[cell_number].is_occupied:
            self.cells[cell_number].is_occupied = True
            self.cells[cell_number].symbol = symbol
            return True
        return False

    def check_end_of_game(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combination in winning_combinations:
            if self.cells[combination[0]].symbol\
                    == self.cells[combination[1]].symbol\
                    == self.cells[combination[2]].symbol\
                    != None:
                return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            cell_number = int(input(f"{self.name}, введите номер клетки: "))
            if cell_number in range(9):
                return cell_number
            print("Неверный номер клетки. Попробуйте еще раз.")


class Game:
    def __init__(self, player1, player2):
        self.state = "running"
        self.players = [player1, player2]
        self.board = Board()

    def run_turn(self, player):
        cell_number = player.make_move()
        if self.board.change_cell_state(cell_number, player.symbol):
            if self.board.check_end_of_game():
                player.wins += 1
                return True
        return False

    def run_game(self):
        self.board = Board()
        for i in range(9):
            if self.run_turn(self.players[i % 2]):
                print(f"{self.players[i % 2].name} выиграл!")
                return True
        print("Ничья!")
        return False

    def run_games(self):
        while True:
            self.run_game()
            print(
                f"Счет: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            play_again = input("Хотите сыграть еще раз? (да/нет) ")
            if play_again.lower() != "да":
                break


player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")

game = Game(player1, player2)
game.run_games()
