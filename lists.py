# A list is a data structure that is mutable(changeable), ordered sequence of elements
# create lists with [] - elements in the list are separated by commas
# every element has a position, those postions are called indexes
# indexes in lists start at 0 - first position will always be index 0

# declaring an empty list
empty_list = []

# list with stuff
# indexes    0             1             2
potions = ["Healing", "Invisiblity", "Strength"]
print(potions)

# accessing elements in a list by their index
# my_list[0] - access the first position in a list
# my_list[<number to indicate a position>]

#accessing our healing potion at index 0
print(potions[0]) #"Healing"

# accessing the invisibility potion at index 1
print(potions[1]) # "Invisibility"

# accessing the strength potion at index 2 - which is also the last index in this list
print(potions[2]) # "Strength"

# accessing the last position in a list will always be [-1]
# my_list[-1] <- last item in the list
print(potions[-1]) #Strength

# Python lists are very flexible
# many types can exist as elements in a list
#             0      1        2                3
cool_list = [42, "unicorn", 3.14, ["apple", "banana", "cherry"]]
#                                     0         1         2
print(cool_list)
# accesses the list at the last position or index 3 and then indexes into the list to get banana
print(cool_list[-1][1])
print(cool_list[3][1])

# LIST METHODS - appending, removing, popping, etc..
# my_list.append(<thing we're appending>)
# append will add to the back of the list

#           0           1           2        
names = ["Skylar", "Jeremiah", "Stephen"]
print(names)
names.append("Anthony")
print(names)
names.append("Anthony")
print(names)
names.append("Sydney")
print(names)
    # 0           1         2          3           4         5
# ['Skylar', 'Jeremiah', 'Stephen', 'Anthony', 'Anthony', 'Sydney']
# appending a new list with different data types to our list of strings
numbers = [1, 2, 3, 4, 5]
names.append(numbers) # names.append([1, 2, 3, 4, 5])
print(names)

# REMOVING elements from a list
# my_list.remove(<thing we're removing>)
names.remove("Sydney")
print(names)
names.remove("Anthony")
print(names)

# removing from a list within our list
# names[-1].remove(3)
# print(names)
# names.remove(numbers)
# print(names)

# POPPING an element from the list
# my_list.pop() <-- without an argument pop will remove the last element from the list
# my_list.pop(index) <-- a position to remove
# pop also returns the element that we're removing
popped_item = names.pop() #no argument so we pop the last index by default
print(popped_item)
print(names)
popped_item.append(6)
print(popped_item)

# popping with an argument
print(names.pop(1))
print(names)

# deleting by index
# del my_list[<index to delete>]
del names[1]
print(names)

# del with a variable
name = "Ryan"
print(name)
# del name[0]
# del name
# print(name)

# counting the number of occurences of an element in a list
# .count() 
# my_list.count(<the thing we're getting a count of>)
flowers = ["lily", "rose", "tulip", "lily", "daisy", "lily", "rose"]
print(flowers.count("lily"))
# setting a variable to a count
rose_number = flowers.count("rose")
print(rose_number)

# inserting items into our list
# my_list.insert(position, element)
hobbies = ["Kayaking", "Reading", "Working Out"]
print(hobbies)
hobbies.insert(1, "Video Games")
print(hobbies)
hobbies.insert(2, "Movies")
print(hobbies)
hobbies.insert(3, "Sketching")
print(hobbies)
# hobbies.insert("Running") TypeError - insert needs 2 arguments
hobbies.insert(9, "Basketball") #so if the position is greater than the length, it will placed at the end of the list
print(hobbies)
hobbies.append("Pokemon Cards")
print(hobbies)
# index error
# print(hobbies[7]) IndexError - list index out of range
# when we try to grab a position that doesnt exist in the list

# Preventing duplicate elements from being added to the list
# hobby = input("Enter a hobby to add to your list")
# # membership check in a list, checks to see if the element exists in the list
# # if <thing we're looking for> in list
# if hobby in hobbies:
#     print("that hobby already exists, we dont want any duplicates")
# else:
#     hobbies.append(hobby)

# print(hobbies)

# changing values at a specific index
#             0              1           2          3           4             5             6              7              8
hobbies = ['Kayaking', 'Video Games', 'Movies', 'Sketching', 'Reading', 'Working Out', 'Basketball', 'Pokemon Cards', 'Anime']
# accessing an element by index
print(hobbies[5])
hobbies[5] = "Hiking"
print(hobbies[5])
print(hobbies)

# Finding the index of an element in a list
# my_list.index(<element>)
position = hobbies.index("Movies")
print(position)
print(hobbies.index("Basketball"))

# clearing the elements of a list
# my_list.clear()
hobbies.clear()
print(hobbies)

# In-class exercise
# Create a list of stuff, it can be movies, video games, foods
# start with 3 items
# append one new thing to your list
# insert one thing to your list at position
# change the value of one thing in your list using the index
# remove one thing from your list, either with remove or pop

# movies = []
# print(movies[2])
# movies[2] = "Missing"
# print(movies)
# movies.remove("Missing")
# print(movies)

#           0          1         2
# foods = ["Sushi", "Tamales", "Pupusas"]
# food_to_eat = foods.pop(1)
# print(food_to_eat)
# print(foods)

# Sorting lists
# .sort()
# my_list.sort()
# .sort() alters the original list
nums = [2, 1, 5, 4, 6, 7, 10, 3, 2]
print(nums)
nums.sort()
print(nums)
# sorted()
# sorted(my_list)
# sorted() creates a sorted copy of the list
nums = [2, 1, 5, 4, 6, 7, 10, 3, 2]
sorted_nums = sorted(nums)
print(sorted_nums)
print(sorted(nums))

# sorting with a key using lamba
# EXTRA SECRET SAUCE
# nums.sort(key=lambda x: x%2)
# print(nums)
# names_list = [("Ryan", "Rhoades"), ("Vanady", "Beard"), ("Blake", "McGuire"), ("Sydney", "Stiward")]
# names_list.sort(key=lambda x: x[1])
# print(names_list)

# Reverse Lists
# my_list.reverse()
numbers = [1, 4, 3, 2, 5]
numbers.reverse()
print(numbers)


# getting the length of a list
# len()
# len(my_list)
#              0            1            2          3             4           5             6              7              8
hobbies = ['Kayaking', 'Video Games', 'Movies', 'Sketching', 'Reading', 'Working Out', 'Basketball', 'Pokemon Cards', 'Anime']
list_length = len(hobbies) #saving the lenght of our list to a variable
print(list_length)
print(len(hobbies))

# Identity operator
# is does not equal ==
guest_numbers = [1, 2, 3]
guest_numbers2 = guest_numbers #guest_numbers2 is pointing to the same location as guest_numbers
guest_numbers3 = [1, 2, 3]

print(guest_numbers is guest_numbers) # True because guest_number2 points to the variable of guest_numbers, giving them the same location
print(guest_numbers is guest_numbers3) #False because the variables live at different locations in our pc's memory
print(guest_numbers == guest_numbers3) #True because the list contents are the same
print(guest_numbers == guest_numbers2) # True because the contents of the list is the same for both variables

# empty lists evaluate to False
empty_list = []
if not empty_list:
    print("That list is empty")
else:
    print("Theres stuff in there")

# More membership checks
guest_list = ["Alice", "Bob", "Charlie"]
# in for membership check
print("Alice" in guest_list) #True
print("Denise" in guest_list) # False
# not in will evaluate to True if something is not in the list
print("Denise" not in guest_list) #True

if "Alice" in guest_list:
    print("Alice was invited to the party")
else:
    print("Alice was not invited")

if "Denise" not in guest_list:
    print("Denise was not invited to the party")
else:
    print("Denise was invited to the party")

# Finding the middle index of a list
# using the floor operator with the len()
#              0            1            2             3          4         5              6                7            8
hobbies = ['Kayaking', 'Video Games', 'Movies', 'Sketching', 'Reading', 'Working Out', 'Basketball', 'Pokemon Cards', 'Anime']
middle_index = len(hobbies) // 2
print(middle_index)
# using the middle index variable to access the element
print(hobbies[middle_index])

# Combining, Copying, and Joining Lists
# List concatenation - combines two lists
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "peas"]
weird_salad = fruits + vegetables
print(weird_salad)

# Copy a list
# my_list.copy()
cloned_fruits = fruits.copy()
print(cloned_fruits) # ['apple', 'banana', 'cherry']

# Joining lists together with .extend()
# my_list.extend(<iterable>)
fruits.extend(vegetables)
print(fruits)
foods = ("Hot Dogs", "Tamales", "Mac n Cheese")
fruits.extend(foods)
print(fruits)

# LIST SLICING
# Slicing - taking segments or slices from a iterable - today its lists
# my_list[start:stop:step]
# start is inclusive
# stop is not inclusive - we stop right before the specified stop index
# if not start is specified it defualts to index 0 - the beginning of the list
# if no stop is specified it defaults to the end of the list
# if no step is specified it defaults to stepping by 1

#              0            1            2             3          4         5              6                7            8
hobbies = ['Kayaking', 'Video Games', 'Movies', 'Sketching', 'Reading', 'Working Out', 'Basketball', 'Pokemon Cards', 'Anime']

# creates a new smaller list starting with index 1 - Video Games and stops before index 4 - Reading is not included
print(hobbies[1:4])
small_hobbies = hobbies[1:4]
print(small_hobbies[1])
# slicing every other element in the hobbies list - stepping by 2
print(hobbies[::2])
# starting at index 1 stopping at index 7 and stepping by 2
print(hobbies[1:7:2])
# start at the beginning and stop at index 5
print(hobbies[:5])
# start at index 3 and go to the end of the list
print(hobbies[3:])
# reverse the list with slice by stepping backwards with -1
print(hobbies[::-1])
# step backwards by -2 
print(hobbies[::-2])
