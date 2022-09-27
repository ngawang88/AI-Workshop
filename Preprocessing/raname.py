import os

path = os.chdir(
    '')

for file in os.listdir(path):
    new_file_name = 'Aa-{}.jpg'.format(i)
    os.rename(file, new_file_name)
    