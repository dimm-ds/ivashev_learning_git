import os
import shutil

os.mkdir('Управление_файлами')

os.chdir(os.path.join(os.getcwd(), 'Управление_файлами'))

with open('file1.txt', 'w', encoding='utf-8') as f1:
    f1.write('Содержимое файла 1')

with open('file2.txt', 'w', encoding='utf-8') as f2:
    f2.write('Содержимое файла 2')

with open('file1.txt', encoding='utf-8') as f1:
    data_1 = f1.readlines()

with open('file2.txt', encoding='utf-8') as f2:
    data_2 = f2.readlines()

print(data_1, data_2, sep='\n')

os.remove('file2.txt')

os.mkdir('Управление_файлами_2')

os.replace('file1.txt', 'Управление_файлами_2/file1.txt')

os.chdir('..')

shutil.rmtree('Управление_файлами')