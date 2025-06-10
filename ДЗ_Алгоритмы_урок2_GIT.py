from abc import ABC, abstractmethod


class ChessBoard:
    """
        Класс, представляющий шахматную доску.
        """

    """
            Создание и подготовка к работе объекта класса ChessBoard (Шахматная доска)

            :param shapes_location: dict[str, list[tuple[int, int] | None]] Словарь состояний поля
                                                                            ключ - буквенно-цифровое обозначение клетки (a1, b5, f3 ...)
                                                                            значение - список из 2х элементовЖ+:
                                                                            1й - None|экземпляр класса фигуры
                                                                            2й - кортеж из 2х цифровых координат клетки (используется для рассчета хода)
            :position_interpreter: dict[tuple[int, int], str]:              Словарь для обрабного преобразования
                                                                            ключ - кортеж из 2х цифровых координат клетки
                                                                            значение - буквенно-цифровое обозначение клетки (a1, b5, f3 ...)
            """
    shapes_location: dict[str, list[tuple[int, int] | None]] = {}
    position_interpreter: dict[tuple[int, int], str] = {}

    for n, i in enumerate('abcdefgh'):
        for j in range(1, 9):
            shapes_location[f'{i}{j}'] = [None, (n + 1, j)]

    for n, i in enumerate('abcdefgh'):
        for j in range(1, 9):
            position_interpreter[(n + 1, j)] = f'{i}{j}'

    def move(self, location: str, new_location: str) -> None:
        """
               Изменяет метоположение фигур, если это возможно

               :param location: str: Клетка из которой планируется передвижение фигуры
                :param new_location: str: Клетка в которую планируется передвижение фигуры
               """
        if not all([i in self.shapes_location.keys() for i in (location, new_location)]):
            """
                Проверка соответствия введеных координат списку ключей, 
                в случае отсутсвие выдаст сообщение о некорректности введеных координат
                """
            print('Неверные координаты')
        else:
            if self.shapes_location[location][0] == None:
                """Проверка состояния первой координаты, в случает отсутствия экземпляра 
                    фигуры выдаст соответствующее сообщение
                    """
                print('Неправильный ход, нет фигуры в указанной клетке')
            elif new_location in self.shapes_location[location][0].get_possible_moves_and_attacks(self)[0] \
                    or new_location in self.shapes_location[location][0].get_possible_moves_and_attacks(self)[1]:
                """Проверка возможности передвижения на конечную точку
                    запрос в метод экземпляра фигуры возможных ходов, при наличии в списках движений и атаки"""
                self.shapes_location[new_location][0] = self.shapes_location[location][0]
                """Меняет состояние в атрибуте экземпляра доски переписывая значения словаря по новой координате
                    """
                self.shapes_location[new_location][0].location = get_number(new_location, self)
                """Меняет запись в атрибуте экземпляра фигуры  на новую координату
                    """
                self.shapes_location[location][0] = None
                """Меняет состояние в атрибуте экземпляра доски, затирая значения словаря по старой координате
                    """
            else:
                """При отсутствии в списках движений и атаки новой координаты выдаст сообщение об ошибке
                    """
                print('Неправильный ход')


class ChessPiece(ABC):
    """
                   Абстрактный класс представляющий фигуры на доске
                   """
    def __init__(self, color: str, location: tuple[int, int], board: ChessBoard):
        """Создание фигуры
        :param color: str: цвет фигуры
        :param location: tuple[int, int] цифровое значение координаты фигуры
        board: ChessBoard экземпляр класса доски, в параметр которого будет записан экзепляр класса фигуры
        """
        if all([i in range(1, 9) for i in location]):#Проверка корректности введеных координат
            self.color = color
            self.location = location
            board.shapes_location[board.position_interpreter[self.location]][0] = self #Сохранение экземпляра класса фигуры в соответствующей строке словаря атрибута доски
        else:
            print('Неверно указаны координаты')

    def rock_and_bishop_traverse_directions(self, board: ChessBoard) -> tuple:
        """возвращает в виде кортежа из 2х списков возможные варианты ходов и атак фигур ладья и слон, можно использовать для любых фигур кроме пешки
            :return tuple:
            """
        possible_moves = []
        possible_attacks = []
        for direction in self.options_moves:
            for move in direction:
                new_location = tuple(map(sum, zip(self.location, move)))
                if not all([i in range(1, 9) for i in new_location]):
                    break
                if board.shapes_location[get_str(new_location, board)][0] == None:
                    possible_moves.append(get_str(new_location, board))
                else:
                    if board.shapes_location[get_str(new_location, board)][0].color != self.color:
                        possible_attacks.append(get_str(new_location, board))
                        break
                    break
        print(f'Возможные варианты ходов: {possible_moves},\n'
              f'возможные варианты атаки: {possible_attacks}')
        return possible_moves, possible_attacks


    @abstractmethod
    def get_possible_moves_and_attacks(self, board: ChessBoard) -> tuple:
        pass


class Pawn(ChessPiece):
    """
        Создание класса Pawn(пешка)
        :param options_moves: list: - вектора движения и значения, на которые возмжоно изменить координаты при расчете ходов
        :param options_attacks: list: - вектора движения и значения, на которые возмжоно изменить координаты при расчете атак
        """
    options_moves: list = (0, 1)
    options_attacks: list = [[(1, 1)], [(1, -1)]]

    def get_possible_moves_and_attacks(self, board: ChessBoard) -> tuple:
        """возвращает в виде кортежа из 2х списков возможные варианты ходов и атак  пешки
            :return tuple:
            """
        possible_moves = []
        possible_attacks = []
        new_location: tuple = tuple(map(sum, zip(self.location, self.options_moves)))
        if all([i in range(1, 9) for i in new_location]) and board.shapes_location[get_str(new_location, board)][0] == None:
            possible_moves.append(get_str(new_location, board))

        for direction in self.options_attacks:
            for move in direction:
                new_location = tuple(map(sum, zip(self.location, move)))
                if not all([i in range(1, 9) for i in new_location]):
                    break
                if board.shapes_location[get_str(new_location, board)][0] != None and board.shapes_location[get_str(new_location, board)][0].color != self.color:
                    possible_attacks.append(get_str(new_location, board))
        print(f'Возможные варианты ходов: {possible_moves},\n'
              f'возможные варианты атаки: {possible_attacks}')
        return possible_moves, possible_attacks


class Rook(ChessPiece):
    """
        Создание класса Rook(ладья)
        :param options_moves: list: - вектора движения и значения, на которые возмжоно изменить координаты при расчете ходов и атак
        """
    options_moves = [[(0, i) for i in range(1, 8)],
                     [(0, -i) for i in range(1, 8)],
                     [(i, 0) for i in range(1, 8)],
                     [(-i, 0) for i in range(1, 8)]]

    def get_possible_moves_and_attacks(self, board: ChessBoard) -> tuple:
        return self.rock_and_bishop_traverse_directions(board)


class Bishop(ChessPiece):
    """
        Создание класса Bishop(слон)
        :param options_moves: list: - вектора движения и значения, на которые возмжоно изменить координаты при расчете ходов и атак
        """
    options_moves = [[(i, i) for i in range(1, 8)],
                     [(i, -i) for i in range(1, 8)],
                     [(-i, i) for i in range(1, 8)],
                     [(-i, -i) for i in range(1, 8)]]

    def get_possible_moves_and_attacks(self, board: ChessBoard) -> tuple:
        return self.rock_and_bishop_traverse_directions(board)


def get_number(date: str, board: ChessBoard) -> tuple:
    """
        Функция работы со словарем в атрибуте экземпляра класса ChessBoard
        принимает буквенно-цифровое обозначение клетки и
        возвращает кортеж с цифровым обозначением координат этой клетки
        """
    return board.shapes_location[date][1]

def get_str(date: tuple, board: ChessBoard) -> str:
    """
        Функция работы со словарем в атрибуте экземпляра класса ChessBoard
        принимает кортеж с цифровым обозначением клетки и
        возвращает буквенно-цифровое обозначение  этой клетки
        """
    return board.position_interpreter[date]


# Создаем объекты 3х классов
board1 = ChessBoard()

print()
# Создаем объекты 3х классов
print('Попытка создать фигуру с несуществующими на доске координатами')
b0 = Bishop('white', (9, 0), board1)
b1 = Bishop('white', (3, 3), board1)
p1 = Pawn('black', (4, 3), board1)
r1 = Rook('black', (6, 5), board1)
r2 = Rook('black', (6, 6), board1)

# Проверяем возможные варианты ходов и атак
print()
print('Проверяем возможные варианты ходов и атак')
print('Слон')
b1.get_possible_moves_and_attacks(board1)
print('Ладья')
r1.get_possible_moves_and_attacks(board1)
print('Пешка')
p1.get_possible_moves_and_attacks(board1)

# Пешка ходит d3 на d6
print()
print('Пешка ходит d3 на d6')
board1.move('d3', 'd6')

# Пешка ходит d3 на d4
print()
print('Пешка ходит d3 на d4')
board1.move('d3', 'd4')

# Проверка изменения состояний доски и атрибута location у перемещенной фигуры и предыдущей клетки
print()
print('Проверка изменения состояний доски и атрибута location у перемещенной фигуры и предыдущей клетки')
print(f'Координаты пешки - {p1.location}')
print(f'Значение клетки d3 - {board1.shapes_location["d3"]}')
print(f'Значение клетки d4 - {board1.shapes_location["d4"]}')

# Белый слон c3 рубит черную пешку на d4
print()
print('Белый слон c3 рубит черную пешку на d4')
board1.move('c3', 'd4')

# Проверка изменения состояний доски и атрибута location у перемещенной фигуры и предыдущей клетки
print()
print('Проверка изменения состояний доски и атрибута location у перемещенной фигуры и предыдущей клетки')
print(f'Координаты слона - {b1.location}')
print(f'Значение клетки c3 - {board1.shapes_location["c3"]}')
print(f'Значение клетки d4 - {board1.shapes_location["d4"]}')

# Попытка сходить из пустой клетки
print()
print('Попытка сходить из пустой клетки')
board1.move('c3', 'd4')

# Попытка срубить фигуру своего цета
print()
print('Попытка срубить черного слона на f6 черным слоном с f5 ')
board1.move('f5', 'f6')

# Попытка сходить по несуществующим координатам
print('Попытка сходить по несуществующим координатам')
board1.move('ва', 'ва')
print()