from gameparts import Board

from gameparts.exceptions import InvalidMoveError, CellOccupiedError


def save_result(str_result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(str_result + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:
        print(f'Текущий игрок: {current_player}')

        while True:

            try:

                row = int(input('Введите номер строки: '))

                if row < 0 or row >= game.field_size:
                    raise InvalidMoveError

                column = int(input('Введите номер столбца: '))

                if column < 0 or column >= game.field_size:
                    raise InvalidMoveError

                if game.board[row][column] != ' ':
                    raise CellOccupiedError

            except InvalidMoveError:
                print('Значения должны быть не отрицательными и меньше'
                      f'{game.field_size}!'
                      )
                print('Введите знаечния для строки и столбца заново.')
            except ValueError:
                print('Буквы вводить нельзя!')
                print('Введите значения для строки и столбца заново.')
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break

        game.make_move(row, column, current_player)
        game.display()

        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            save_result(f'Победили {current_player}!')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            save_result('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
