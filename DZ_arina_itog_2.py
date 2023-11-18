# Задание №4: Крестики нолики

class Cell:
    def __init__(self, numer):
        self.numer = numer
        self.val = ' '

    def val_value(self, val):
     if self.val == ' ':
         self.val = val
         return True
     else:
         return False


class Board:
    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append(Cell(i + 1))

    def place(self):
        print('  1  |  2  |  3  ')
        print('-----------------')
        print('  4  |  5  |  6  ')
        print('-----------------')
        print('  7  |  8  |  9  ')

    def new_board(self):
        print(f'  {self.cells[0].val}  |  {self.cells[1].val}  |  {self.cells[2].val}  ')
        print('---------------')
        print(f'  {self.cells[3].val}  |  {self.cells[4].val}  |  {self.cells[5].val}  ')
        print('---------------')
        print(f'  {self.cells[6].val}  |  {self.cells[7].val}  |  {self.cells[8].val}  ')

class Player:

    def __init__(self, name, klet):
        self.name = name
        self.klet = klet

    def play(self, board):
        while True:
            try:
                hod = int(input(f'{self.name}, введите номер клетки (1-9): '))
                if 1 <= hod <= 9:
                    break
                elif hod == 0 or hod > 10:
                    print('Вы ввели неверное значение! Введите число от 1 до 9')
                else:
                    print('Ячейка уже занята! Попробуйте еще раз')
            except:
                print('Вы ввели неверное значение! Введите число от 1 до 9')


board = Board()
board.place()

try:
    player1 = Player(input("Введите имя первого игрока: "), str(input("Выберите крестик или нолик: ")))
    while True:
        if player1.klet not in ['X', '0']:
            setattr(player1, 'klet', str(input("Вы ввели неверный символ. Выберите крестик или нолик: ")))
        else:
            player2 = Player(input("Введите имя второго игрока: "), "0" if player1.klet == "X" else "X")
            print(f'{player2.name}, вы ходите {player2.klet}')
            break
except:
    print("Что-то пошло не так...")

current_player = player1

while True:
    current_player.play(board)
    board.new_board()
    if ((board.cells[0].val == board.cells[1].val == board.cells[2].val != ' ') or
            (board.cells[3].val == board.cells[4].val == board.cells[5].val != ' ') or
            (board.cells[6].val == board.cells[7].val == board.cells[8].val != ' ') or
            (board.cells[0].val == board.cells[3].val == board.cells[6].val != ' ') or
            (board.cells[1].val == board.cells[4].val == board.cells[7].val != ' ') or
            (board.cells[2].val == board.cells[5].val == board.cells[8].val != ' ') or
            (board.cells[0].val == board.cells[4].val == board.cells[8].val != ' ') or
            (board.cells[2].val == board.cells[4].val == board.cells[6].val != ' ')):
        print(f'Победил игрок {current_player.name}!')
        break
    elif all(cell.val != ' ' for cell in board.cells):
        print('Ничья!')
        break
    current_player = player1 if current_player == player2 else player2



