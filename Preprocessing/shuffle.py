import random
import os

path = os.chdir(
    r'./images')
file_list = os.listdir(path)
random.shuffle(file_list)


i = 0
for file in file_list:
    Newfile_name = '{}.jpg'.format(i)
    os.rename(file, Newfile_name)
    i = i + 1


# k = 1
# for file in os.listdir(path):
#     Newfile_name = 'Nine{}.jpg'.format(k)
#     os.rename(file, Newfile_name)
#     k = k + 1