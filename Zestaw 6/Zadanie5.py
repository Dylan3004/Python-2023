import math
import os
import random
import re
import sys
import functools
from itertools import product

first_input = input().split()

number_of_lists = int(first_input[0])
lista = []
curr = 0
number_of_modulo = int(first_input[1])
for n in range(number_of_lists):
    lista.append(list(map(int, input().split()[1:])))

for i in product(*lista):
    temp = sum(map(lambda x: x * x, i)) % number_of_modulo
    if temp > curr:
        curr = temp

print(curr)