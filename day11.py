from itertools import count
from operator import truediv
import statistics
import math
from re import I

def sum(num1, num2):
    sum_total = num1 + num2
    return sum_total

print(sum(3, 81))

def area_of_circle(r):
    area = 3.14 * r * r
    return area

print(area_of_circle(10))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            total += num 
        else:
            print("not a number")    # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5, 'a', 4))

def convert_C_to_F(c):
    F = (c * 9.5) + 32
    return F
print(convert_C_to_F(100))

def check_season(month):
    if month in ['december', 'january', 'february']:
        season = 'winter'
    elif month in ['march', 'april', 'may']:
        season = 'spring'
    elif month in ['june', 'july', 'august']:
        season = 'summer'
    else:
        season = 'fall'
    return season

print(check_season('june'))


def solve_quadratic_eqn(a, b, c):
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 
  
print(solve_quadratic_eqn(5, 6, 1))

def slope(x1, y1, x2, y2):
    return (float)(y2-y1)/(x2-x1)




def print_list(my_list):
    for item in my_list:
        print(item)

print(print_list(['hello', 'salam', 'thammmmm']))

def reversed_list(list):
    list.reverse()
    return list
print(reversed_list(['hello', 'salam', 'thammmmm']))

def capitalize_list_items(list):
    capital = []
    for item in list:
        capital.append(item.capitalize())
    return capital

print(capitalize_list_items(['hello', 'samin', 'boom']))

def add_item(list, item):
    list.append(item)
    return list
print(add_item(['sam', 'darara', 'bab'], 'hell'))

def remove_item(list, item):
    list.remove(item)
    return list
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))

def sum_of_numbers(number):
    sum = 0
    for i in range(number):
        sum += i
    return sum
print(sum_of_numbers(5))

def  sum_of_odds(number):
    sum = 0
    for i in range(number):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odds(5))

def sum_of_even(number):
    sum = 0
    for i in range(number):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(5))

def evens_and_odds(num):
    even = 0
    odd = 0
    for i in range(num):
        if i % 2 == 0:
            even += 1
        else:
            odd +=1
    print(f'number of even numbers: {even}, and the number of odds: {odd}')
evens_and_odds(100)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))



def is_empty(param):
    if len(param) == 0:
        return True
    else:
        return False
print(is_empty([]))





def calculate_mean(list):
    sum = 0
    for item in list:
        sum += item
    return sum / len(list)
print(calculate_mean([1, 2, 3, 4, 5, 6, 7]))

def calculate_median(list):
    return statistics.median(list)
print(calculate_median([1, 2, 3, 4, 5]))

def calculate_mode(list):
    return statistics.mode(list)
print(calculate_mode([2, 3, 2, 3, 2, 5]))

def is_prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
is_prime(11)

def uniqe(list):
    if len(list) == len(set(list)):
        return True
    else: 
        return False
print(uniqe([1, 2, 5, 1]))

def same_type(list):
    res = all(isinstance(sub, type(list[0])) for sub in list[1:])
    if res == True:
        print('all the same')
    else:
        print('all are not the same')
same_type([5, 3, 6, 'd'])

def valid_var(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(valid_var('tam'))


def most_spoken(countries_info):
    lang_counter ={}
    for item in countries_info:
        for lang in item["languages"]:
            if lang in lang_counter:
                lang_counter[lang] += 1
            else:
                lang_counter[lang] = 1

    pop = sorted(lang_counter, key=lang_counter.get, reverse=True)
    top_20 = pop[:20]
    print(top_20)

def most_populated(countries_info):
    populated = []
    for item in countries_info:
        populated.append(item['population'])
    
    pop = sorted(populated, reverse=True)

    most_20 = []
    for i in populated:
        for item in countries_info:
            if i == item['population']:
                most_20.append(item['name'])

    print(most_20[:20])
