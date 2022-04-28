from code import compile_command


string = 'thirty ' + 'days ' + 'of ' + 'python'
print(string)
company = 'coding for all'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
comp = company.split()
print(comp[0])
print(company.find("coding"))
print(company.index('coding'))
print(company.replace("coding", "python"))
print(company.split(" "))
names = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(names.split(", "))
print("Coding for all"[0])
print("Coding for all"[-1])
print("Coding for all"[10])
acr = company.split()
acrrr = ''
for i in acr:
    acrrr += i[0]
print(acrrr.upper())

print(company.index("c"))
print(company.rfind("i"))
strrr = "you cannot end a sentence with because because because is a conjuction"
print(strrr.index('because'))
print(strrr.rindex('because'))
print("Coding For All".startswith('Coding'))
print("Coding For All".endswith('Coding'))
print("   Coding For All   ".strip(" "))
print("30DaysOfPython".isidentifier())
list1 = ['django', 'flask', 'bottle', 'pyramid']
print(" - ".join(list1))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
area = 3.14 * radius ** 2
print(f'the area of a circle with radius {radius} is {area} meters square')
