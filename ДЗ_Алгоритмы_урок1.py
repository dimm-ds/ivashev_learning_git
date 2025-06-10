#Задача №1

from datetime import datetime
import requests

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper

@measure_execution_time
def get_response(url: str):
    response = requests.get(url)
    return response


print(get_response('https://google.com'))
print()
#Задача №2

def requires_admin(func):
    def wrapper(*args, **kwargs):
        if args[0]['role'] != 'admin':
            raise PermissionError('У пользователя недостаточно прав')
        return func(*args, **kwargs)
    return wrapper

@requires_admin
def delete_user(user: dict, username_to_delete: str):
    return f"User {username_to_delete} has been deleted by {user['username']}."



admin_user = {'username': 'Alice', 'role': 'admin'}
regular_user = {'username': 'Bob', 'role': 'user'}


print(delete_user(admin_user, 'Charlie'))
print(delete_user(regular_user, 'Charlie'))
