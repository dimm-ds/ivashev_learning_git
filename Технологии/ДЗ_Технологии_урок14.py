str_list = ["apple", "kiwi", "banana", "fig"]
print(list(filter(lambda x: len(x) > 4, str_list)))

dict_list = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
print(sorted(dict_list, key=lambda x: x['grade'], reverse=True)[0]['name'])

tuple_list =  [(1, 5), (3, 2), (2, 8), (4, 3)]
print(list(sorted(tuple_list, key=lambda x: sum(x))))

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, numbers_list)))

class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name - {self.name}, age - {self.age}.'


p1 = Person('Dima', 20)
p2 = Person('Andrey', 30)
p3 = Person('Aleksey', 25)
p4 = Person('Pavel', 36)
p5 = Person('Oleg', 22)

persons_list = [p1, p2, p3, p4, p5]
for person in sorted(persons_list, key=lambda x: x.age):
    print(person)