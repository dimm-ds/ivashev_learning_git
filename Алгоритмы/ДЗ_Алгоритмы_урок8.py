class TaskQueue:
    def __init__(self):
        self.items = []

    def add_task(self, task):
        self.items.append(task)

    def get_next_task(self):
        try:
            return self.items.pop(0)
        except IndexError:
            return

    def is_empty(self):
        return len(self.items) == 0

class Task:
    def __init__(self, name):
        self.name = name

queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Ожидаемый результат: "Задача 1"

queue.get_next_task()  # Извлечь следующую задачу

print(f"Очередь пуста: {queue.is_empty()}")  # Ожидаемый результат: False
