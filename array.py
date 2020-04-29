x='     Well hello   '
y=x.strip().lower()[:7]
print(y)
print(x.strip()[:-4].upper())
print(x.replace('Well','Oh'))
print(x.split(" "))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

print('12\t34\b\n')
print('\x23\n\n\n')

a=3
b=2
print("a") if a > b else print("b")

if a > b: print("a")


import platform

x = platform.system()
print(x)

username = input("Enter username:")
print("Username is: " + username)