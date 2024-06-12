# LOOPS
# for loop
# for iterator_variable in iterable:
#   do something
# while loop
# while condition to run:
#   do something

# for loops
# for loop will iterate until the end of the iterable inless told otherwise
flavors = ["vanilla", "chocolate", "chocolate chip", "mango", "pistaccio", "strawberry"]
# for iterator_variable in iterable:
#   do something
for flavor in flavors:
    print(flavor)
print(flavors)

# a conditional in a loop
for flavor in flavors:
    if flavor == "chocolate chip":
        print(flavor, "Thats my favorite flavor")
    else:
        print(flavor, "Thats an ok flavor, i guess")

# Looping by index
# using range() and len()
# range(start, stop, step)
# range(stop)
#              0          1              2               3          4           5
flavors = ["vanilla", "chocolate", "chocolate chip", "mango", "pistaccio", "strawberry"]
for num in range(6):
    print(num)
print()
length = len(flavors)
print(length, "length of flavors list")

# looping by index
# i as an iterator can be anythign i want
# conventionally we use i to stand for the index when we're looping by index
for i in range(len(flavors)):
    print(i, flavors[i])

# using a loop to replace an element
for i in range(len(flavors)):
    if flavors[i] == "chocolate":
        flavors[i] = "moose tracks"
print(flavors)

# looping with enumerate
#              0          1              2               3          4           5
flavors = ["vanilla", "chocolate", "chocolate chip", "mango", "pistaccio", "strawberry"]
flavor_enum = enumerate(flavors)
print(flavor_enum)
print(list(flavor_enum)) #converts an enumerate object into a list
for i, element in enumerate(flavors):
    print(i, element)

for group in enumerate(flavors):
    print(group)
    

# very similar to setting two variables on a single line
x, y = 0, "vanilla" 

for i, element in enumerate(flavors):
    if i % 2 == 0:
        print(element)

# unpacking list
names = ["Blake", "Skylar", "Jeremiah"]
blake, skylar, jeremiah = names

print(blake)
print(skylar)
print(jeremiah)

flavor_enum = [0, "vanilla"]
i, element = flavor_enum
print(i)
print(element)

for elephant, potato in enumerate(flavors):
    if potato == "pistaccio":
        flavors[elephant] = "moose tracks"
print(flavors)

# Double For loops - nested for loops

flavors = ["vanilla", "chocolate", "chocolate chip", "mango", "pistaccio", "strawberry"]  
toppings = ["sprinkles", "syrup", "mochi", "hot fudge", "heath", "crushed nuts", "choco chips"]

for flavor in flavors:
    print(flavor)
    for topping in toppings:
        print(topping)

for flavor in flavors:
    if flavors.index(flavor) == 2:
        break
    print(flavor)
    for topping in toppings:
        print(topping)
print()
# Loop Keywords
# break - stops the loop wherever its at
toppings = ["sprinkles", "syrup", "mochi", "hot fudge", "heath", "crushed nuts", "choco chips"]
for topping in toppings:
    if topping == "mochi":
        break
    else:
        print(topping)
# for topping in toppings:
#     break
#     print(topping) # unreachable code

# continue - skip over an iteration
for topping in toppings:
    if topping == "hot fudge":
        continue
    print(topping)

# pass - lets us leave blocks of code blank
# we can come back later and add some functionality
for topping in toppings:
    pass # come back to this later and figure out what i want to do with my toppings

# loop by index to access multiple items from evenly lengthed lists
#                0         1        2
booth_types = ["Food", "Games", "Music"]
schedule_times = ["10:00 am", "1:00 pm", "3:00 pm"]
items_needed = ["Grill", "Tickets", "Bass Guitar"]

# iterating through all three lists at the same, using the indexes from one list
for i in range(len(booth_types)):
    print(i)
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"{booth} Booth - Scheduled: {time}, Needs item: {item}")

# calulating the total of a list of prices
prices = [2.99, 5.49, 3.25, 13.99, 4.75]
print(sum(prices))
# adding a total with a for loop
total = 0
for price in prices:
    total += price #total = total + price
print("Total cost:", total)

# while loop
# while condition to run:
#   do something
while True:
    break
    #do something
    


# looping with a counter
# as long as the counter is greater or less than a certain
# the while loop will keep going
marshmallows = 0
while marshmallows < 35: #this while loop runs as long as marshmallows is less than 35
    print("throwing marshmallow")
    marshmallows += 1
    print(f"I currently have {marshmallows} marshmallows in my mouth")

temperature = 100
# setting a condition that is never
while temperature < 0:
    # this block of code never executes because 
    # temperature is start at 100 
    temperature -= 1

# creating a loop that never breaks
# marshmallows = 0
# while marshmallows < 35:
#     marshmallows -= 10000000000000000000000000
#     print(marshmallows)


# TAKING a user input with a while loop and break when the user says to quit
# video_games = []
# while True:
#     user_input = input("Enter a game to add to your collection or say quit to quit")
#     if user_input == "quit":
#         print(video_games)
#         break
#     else:
#         video_games.append(user_input)

# Write a program with a while loop, asking the user to add something to a list
# and breaking the loop if they say quit
# EXTRA SAUCE
# add options to remove an item from the list
# display each item individually in the list
# any other sauce you wanna throw on
# vacation_list = []
# while True:
#     user_input = input("Enter destination to add to your list of vacation spots or Say quit or remove to remove")
#     if user_input == "quit":
#         print(vacation_list)
#         break
#     elif user_input == "remove":
#         removed_destination = input("Which destination would you like to remove")
#         if removed_destination in vacation_list:
#             vacation_list.remove(removed_destination)
#         else:
#             print("That destination is not in your list")
        
#     else:
#         vacation_list.append(user_input)

# random module
import random #pull in all functionality from the random module in python
# random.randint(a, b) <-- a random number between a and b
print(random.randint(1,20))

for num in range(10):
    print(random.randint(1, 20))

# random.shuffle() to shuffle the order of a list
playlist = ["Whats Up", "Talking to My Scale", "Ice Ice Baby", "Are You Happy Now", "Heather", "Faded"]
random.shuffle(playlist)
print(playlist)

# random.choice - randomly pick an element from a list
my_games = ["Paper Mario", "Fire Emblem", "COD", "Baldurs Gate 3", "Marvel vs Capcom", "Tomb Raider"]
random_game = random.choice(my_games)
print(random_game)

# choices = ["rock", "paper", "scissors"]

# while True:
#     user_choice = input("Please enter rock paper or scissors")
#     computer_choice = random.choice(choices)