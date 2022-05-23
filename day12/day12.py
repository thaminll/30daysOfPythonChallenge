from traceback import print_tb
import mymodule
from mymodule import sum_two_number
import statistics
import math
from string import *
import random

age = [12, 8, 16, 21, 54, 45]

print(mymodule.generate_fullname('samin', 'lashgari'))
print(sum_two_number(12, 30))

print(statistics.mean(age))
print(statistics.median(age))
print(statistics.mode(age))
print(statistics.stdev(age))

print(math.sqrt(81))
print(math.log(100, 10))
print(math.pow(2, 5))

print(ascii_letters)
print(digits)
print(punctuation)

print(random.random())
print(random.randint(12, 52))


#1
def random_userID():
    choicee = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    userID = ''
    for i in range(6):
        x = random.choice(choicee)
        userID += x
    print(userID)
random_userID()

#2
def user_id_gen_by_user(numofchar, numofid):
    choicees = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    for i in range(numofid):
        userID = ''
        for j in range(numofchar):
            x = random.choice(choicees)
            userID += x
        print(userID)
user_id_gen_by_user(15, 3)

#3
def rgb_color_gen():
    rgb = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
    return rgb
print(rgb_color_gen())

#level2/ 1
def list_of_hexa_colors():
    hex = '0123456789abcdef'
    list_of_hex = []
    for j in range(random.randint(0, 9)):
        hexnum = '#'
        for i in range(6):
            x = random.choice(hex)
            hexnum += x
        list_of_hex.append(hexnum)
    print(list_of_hex)
list_of_hexa_colors()

#level2/ 2
def list_of_rgb_colors():
    list_of_rgb = []
    for j in range(random.randint(0, 9)):
        num = random.randint(0, 255)
        list_of_rgb.append(num)
    print(list_of_rgb)
list_of_rgb_colors()

#level2/ 3
def generate_colors(type, number):
    list_of = []
    if type == 'rgb':
        for i in range(number):
            list_of.append(f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})')
    else:
        hex = '0123456789abcdef'
        
        for i in range(number):
            hexnum = '#'
            for i in range(6):
                x = random.choice(hex)
                hexnum += x
            list_of.append(hexnum)
    print(list_of)
generate_colors('rgb', 3)
generate_colors('hexa', 3)

#level3/ 1
def shuffle_list(list):
    shuffled_list = []
    while len(list) > 0:
        rand = list[random.randint(0, len(list) - 1)]
        shuffled_list.append(rand)
        list.remove(rand)
    print(shuffled_list)
shuffle_list(['sara', 'samin', 'hanie', 'sogand', 'tina', 'sana', 'afsane'])

#level3/ 2
def seven_random():
    list_seven = []
    while len(list_seven) != 7 :
        rand_num = random.randint(0, 9)
        if rand_num in list_seven:
            continue
        else:
            list_seven.append(rand_num)
    print(list_seven)
seven_random()
