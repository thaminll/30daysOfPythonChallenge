age = int(input('enter your age: '))
if age > 18:
    print('you are old enough to learn to drive')
else:
    print(f'you need {18 - age} more years to learn to drive')

my_age = 22
your_age = int(input('enter your age: '))

if your_age > my_age:
    if (your_age - my_age) == 1:
        print(f'you are {your_age - my_age} year older than me.')
    elif (your_age - my_age) > 1:
        print(f'you are {your_age - my_age} years older than me.')

a = int(input('enter number1: '))
b = int(input('enter number2: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

score = int(input('enter your score: '))
if score > 80 and score < 100:
    grade = 'A'
elif score > 70 and score < 89:
    grade = 'B'
elif score > 60 and score < 69:
    grade = 'C'
elif score > 50 and score < 59:
    grade = 'D'
else:
    grade = 'F'

print(grade)

month = input("enter the month: ").capitalize()

if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
else:
    season = 'Summer'

print(season)

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('enter the name of your fruit: ')
if fruit in fruits:
    print('that fruit already exist in the list.')
else:
    fruits.append(fruit)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person.keys():
    print(person['skills'][int(len('skills') / 2)-1])

if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print("True")
    else:
        print("false")

if ('JavaScript' and 'React') in person['skills'] and len(person['skills']) == 2:
        print('He is a front end developer')
elif ('Node' and 'MongoDB' and 'Python') in person['skills'] and len(person['skills']) == 3:
        print('He is a back end developer')
elif ('Node' and 'MongoDB' and 'React') in person['skills'] and len(person['skills']) == 3:
        print('He is a full stack developer')
else:
    print('unknown title')

if person['is_marred'] and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')