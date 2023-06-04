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

#Find the first index of "disco":
print(genres_tuple.index("disco"))

#Generate a sorted List from the Tuple 
C_tuple=(-5, 1, -3)
C_list = sorted(C_tuple)
C_list


#dictionaries
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}

#In the dictionary soundtrack_dic what are the keys ?
soundtrack_dic.keys()
#In the dictionary soundtrack_dic what are the values ?
soundtrack_dic.values()

album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}

#Use the dictionary to find the total sales of Thriller:
album_sales_dict["Thriller"]

inventory ={}

#Task-2 Store the first product details in variable
ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

#Add the details in inventory
inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear

#Delete release year from the inventory

del(inventory["ProductNo1_releaseYear"])

print(inventory)

