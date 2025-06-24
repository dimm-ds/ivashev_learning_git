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
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)


dct = {'[': ']',
       ']': '[',
       ')': '(',
       '(': ')',
       '{': '}',
       '}': '{'}

def stack_is_empty(sequence):
    stack1 = Stack()
    for element in list(sequence):
        if stack1.is_empty():
            stack1.push(element)
        else:
            if dct[element] == stack1.peek():
                stack1.pop()
            else:
                stack1.push(element)
    return stack1.is_empty()

user_input = input('Введите скобочную последовательность')
imput_valid = stack_is_empty(user_input)
print('Правильная последовательность' if imput_valid else 'Неправильная последовательность')