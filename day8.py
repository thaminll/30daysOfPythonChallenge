dog = dict()
dog = {'name' : 'jesi', 'color' : 'blue', 'breed' : 'Golden', 'legs' : 4, 'age' : 2}
student = {'first_name' : 'Samin', 'last_name' : 'Lashgari', 'gender' : 'female', 'age' : 22, 'marital_status' : 'single', 'skills' : ['python', 'django', 'html'], 'country' : 'iran', 'city' : 'tehran', 'addres' : {'street' : 'takestan', 'no' : 9}}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('mysql')
student['skills'].append('linux')
print(student['skills'])
print(student.keys())
print(student.values())
student_tup = tuple(student.items())
print(student_tup)
student.pop('city')
print(student)
del dog