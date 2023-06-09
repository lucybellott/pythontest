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

#SETS

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", 1982, "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Find the intersections
intersection = album_set1 & album_set2
intersection

# Find the difference in set1 but not set2
album_set1.difference(album_set2)  

# Find the union of two sets
album_set1.union(album_set2)

# Check if superset
set(album_set1).issuperset(album_set2)   

# Check if subset
set(album_set2).issubset(album_set1)     

#LOOPS

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

 # Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])   

 # Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")   

#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)
    

#.sort vs sorted(iterable)
#sorted creates a new array, .sort changes the original array




#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")





# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

#The Frequency of words is: {'Mary': 6, 'had': 2, 'a': 2, 'little': 3, 'lamb': 3, 'Little': 1, 'lamb,': 1, 'lamb.Its': 1, 'fleece': 1, 'was': 2, 'white': 1, 'as': 1, 'snow': 1, 'And': 1, 'everywhere': 1, 'that': 2, 'went': 3, 'went,': 1, 'Everywhere': 1, 'The': 1, 'sure': 1, 'to': 1, 'go': 1}
