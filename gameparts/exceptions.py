class InvalidMoveError(IndexError):
    """Введённые значение хода недопустимы."""

    def __str__(self):
        return 'Введённые значения хода недопустимы.'


class CellOccupiedError(Exception):
    def __str__(self):
        return 'Попытка изменить занятую ячейку.'
