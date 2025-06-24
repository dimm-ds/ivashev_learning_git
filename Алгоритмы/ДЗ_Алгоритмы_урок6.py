class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return float(self.items[-1])
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)


def get_rpn(sequence):
    stack = Stack()
    for element in sequence.split():
        if stack.is_empty():
            try:
                stack.push(int(element))
                continue
            except ValueError:
                raise ValueError('Не обнаружен операнд для вычисления')
        try:
            stack.push(int(element))
        except ValueError:
            if stack.size() < 2:
                raise ValueError('Неправильная последовательность')
            a = stack.pop()
            b = stack.pop()
            if element == '+':
                stack.push(b + a)
            elif element == '-':
                stack.push(b - a)
            elif element == '*':
                stack.push(b * a)
            elif element == '/':
                if a == 0:
                    raise ValueError('Деление на 0')
                stack.push(b / a)
            else:
                raise ValueError('Несуществующий оператор')
    if stack.size() != 1:
        raise ValueError('Неправильная последовательность')
    return stack.peek()


while True:
    user_input = input('Введите последовательность для вычисления')
    try:
        print(get_rpn(user_input))
    except ValueError as e:
        print(e)

