#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
x = [i for i in numbers if i <= 0]
print(x)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list = [i for row in list_of_lists for item in row for i in item]
print(list)

#3
tuple_pow = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(10)]
print(tuple_pow)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
simple_countries = [item for row in countries for i in row for item in i]
print(simple_countries)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_count = [{'countrie' : item[0] , 'city' : item[1]} for row in countries for item in row]
print(dict_count)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name  = [f'{item[0]} {item[1]}' for row in names for item in row]
print(full_name)

#7
slope = lambda y2, y1, x2, x1 : (y2 - y1) / (x2 - x1)
print(slope(5, 1, 3, 1))