name = 'samin'
age = 20
height = 9.6
mylist = [1, 2, 'salam']
mydict = {'name':'samin', 'age1': 222}
mytuple = ('samin', 1, 3)
myset = {'salam' , 5}
floatnom = 2.6

'''base = int(input("enter the base:"))

height = int(input("enter the height:"))

area = base * height
#print("the area is " ,area)'''

print(len("python") > len("dragon"))
print('on' in 'python' and 'on' in 'dragon')
print('on' not in 'python' and 'on'  not in 'dragon')
print(len('python'))
print(float(len('python')))
print(str(len('python')))
print(7//2 == int(2.7))
print(type(10) == type('10'))

list1 = [1, 1, 1, 1, 1]
list2 = [2, 1, 2, 4, 8]
list3 = [3, 1, 3, 9, 27]
list4 = [4, 1, 4, 16, 64]
list5 = [5, 1, 5, 25, 125]

print(*list1)
print(*list2)
print(*list3)
print(*list4)
print(*list5)