# name = input("Name: ")
# age = input("Age: ")
# print(f"hello {name}, you're {age} years old")

from functions import hi


s= set()

s.add(1)
s.add(3)

print(f'the set has {len(s)} elements')

def square(num):
    return num * num 

for i in range(5):
 print(f"the square of {i} is {square(i)} ")   

name = 'Lucy'

print(hi(name))

