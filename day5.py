from re import I


empty_list = []
empty_list2 = list()

list1 = [1, 2, 3, 4, 5]
print(len(list1))
first = list1[0]
mid = list1[int(len(list1)/2)]
last = list1[-1]
print(f'first item of the list {first} the mid is {mid} and the last is {last}')

mixed_data_types = ['samin', 22, 164, 'single', "tehran,takestan"]

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
first_comp = it_companies[0]
mid_comp = it_companies[int(len(it_companies)/2)]
last_comp = it_companies[-1]
print(f'first item of the list {first_comp} the mid is {mid_comp} and the last is {last_comp}')
it_companies[1] = "htc"
print(it_companies)
it_companies.append('samsung')
print(it_companies)
it_companies.insert(int(len(it_companies)/2), 'hp')
print(it_companies)
it_companies[2] = it_companies[2].upper()
print(it_companies)
print("# ".join(it_companies))
print('htc' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
it_companies.remove('Oracle')
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ["Node", 'Express', 'MongoDb']

front_end.extend(back_end)
print(front_end)
full_stack = front_end.copy()
print(full_stack)
full_stack.append('python')
full_stack.append('SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(f'{min(ages)} and {max(ages)}')
ages.append(min(ages))
ages.append(max(ages))
print(ages)
print(sum(ages)/len(ages))
print(max(ages) - min(ages))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = countries
print(china)
print(scandic)