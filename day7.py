it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
new_mem = {"Digikala", "snapp", "Tapsi"}
it_companies.update(new_mem)
print(it_companies)
it_companies.remove('Google')
print(it_companies)

'''The discard() method removes the specified item from the set.
This method is different from the remove() method, because the remove()
method will raise an error if the specified item does not exist,
and the discard() method will not.'''

c = A.union(B)
print(c)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

print(A.symmetric_difference(B))
del A
del B
del c

ages = set(age)
print(len(age))
print(len(ages))

sentences = 'I am a teacher and I love to inspire and teach people'
words = sentences.split()
print(len(set(words)))
