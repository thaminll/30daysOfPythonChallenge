
tpl1 = tuple()
sisters = ('samin', 'sana')
brothers = ('amirhosein',)
siblings = sisters + brothers
print(len(siblings))

family_members = list(siblings)
family_members.append("zahra")
family_members.append("mohammadreza")
print(family_members)
siblings1 = family_members[0:3]
parents = family_members[3:]
print(siblings1)
print(parents)

fruits = ('banana', 'apple', 'watermelon')
vegetables = ('carrot', 'lettuce')
animal_products = ('milk', 'butter')
food_stuff = fruits + vegetables + animal_products
food_stuff_lst = list(food_stuff)
print(food_stuff_lst)
print(food_stuff_lst[2:5])
print(food_stuff_lst[0:3])
print(food_stuff_lst[-3:])
del food_stuff

nordic_countries = ("china", 'usa', 'iran', 'france', 'iceland')
print('estonia' in nordic_countries)
print('iceland' in nordic_countries)

