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

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")

#Use slicing to obtain indexes 3, 4 and 5:

print(genres_tuple[3:6])

