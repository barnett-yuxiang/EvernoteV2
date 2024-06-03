import os
from os.path import abspath, dirname


current_dir = os.getcwd()
print(current_dir)

current_dir = dirname(abspath(__file__))
print(current_dir)
