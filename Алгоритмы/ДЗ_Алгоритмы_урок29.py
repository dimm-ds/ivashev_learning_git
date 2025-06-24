class MyDict:
    def __init__(self):
        self._dataset = []

    def __getitem__(self, key):
        try:
            key_index = self.keys().index(key)
            return self._dataset[key_index][1]
        except ValueError:
            return

    def __setitem__(self, key, value):
        if key not in self.keys():
            self._dataset.append((key, value))
        else:
            key_index = self.keys().index(key)
            self._dataset[key_index] = (key, value)

    def __delitem__(self, key):
        try:
            key_index = self.keys().index(key)
            self._dataset.pop(key_index)
        except ValueError:
            pass

    def keys(self):
        keys = []
        if len(self._dataset) == 0:
            return keys
        for item in self._dataset:
            keys.append(item[0])
        return keys

    def __eq__(self, other):
        pass

    def values(self):
        values = []
        if len(self._dataset) == 0:
            return values
        for item in self._dataset:
            values.append(item[1])
        return values

    def items(self):
        items = []
        if len(self._dataset) == 0:
            return items
        for item in self._dataset:
            items.append(item)
        return items

    def __contains__(self, item):
        return item in self.keys()

    def __str__(self):
        return f'{self._dataset}'




my_dict = MyDict()




my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['a'])
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']