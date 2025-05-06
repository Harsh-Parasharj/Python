


#                                        Ch 6 Dictionaries  With Harsh Parashar



# In this chapter, you'll learn how to use Python dictionaries to connect related information. You'll discover how to access and modify data within dictionaries, loop through their contents, and nest dictionaries within lists or other dictionaries. This understanding will help you model real-world objects, such as representing a person with details like name, age, and profession. You can also pair different types of information, like words and their meanings or names and favorite numbers.




#                                                  A Simple Dictionary



# In the example provided, a simple dictionary named alien_0 stores information about an alien, including its color and point value:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # Outputs: green
print(alien_0['points'])  # Outputs: 5

#  This demonstrates how dictionaries can effectively represent real-world situations, and with practice, you'll become more comfortable using them.



#                                                Working with Dictionaries


#  A dictionary in Python is a collection of key-value pairs, where each key is linked to a value. You can use keys to access their corresponding values, which can be numbers, strings, lists, or even other dictionaries.
#  Dictionaries are defined using braces {} and consist of key-value pairs separated by colons and commas. For example:

alien_0 = {'color': 'green', 'points': 5}


#  In this case, 'color' is a key associated with the value 'green'. A dictionary can have multiple key-value pairs, but it can also be as simple as having just one, like this:

alien_0 = {'color': 'green'}

#  This stores only the alien's color.



# #                                              Accessing Values in a Dictionary



# To access a value in a dictionary, use the dictionary name followed by the key in square brackets. For example:


alien_0 = {'color': 'green'}
print(alien_0['color'])  # Outputs: green

#You can have multiple key-value pairs in a dictionary. For instance:

alien_0 = {'color': 'green', 'points': 5}

# You can access the point value like this:

new_points = alien_0['points']
print(f"You just earned {new_points} points!")  # Outputs: You just earned 5 points!

# This code retrieves the point value whenever an alien is shot down, allowing you to display the points earned.




#                                                                  Adding New Key-Value Pairs



# You can easily add new key-value pairs to a dictionary in Python. For example, if you have a dictionary representing an alien, you can add its x and y coordinates like this:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # Output: {'color': 'green', 'points': 5}
alien_0['x_position'] = 0  # Adding x coordinate
alien_0['y_position'] = 25  # Adding y coordinate
print(alien_0)  # Output: {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}


# In this example, we start with a dictionary containing the alien's color and points. We then add the x and y positions, resulting in a dictionary with four key-value pairs. As of Python 3.7, dictionaries maintain the order of items as they are added.



#                                                     Starting with an Empty Dictionary



# You can start with an empty dictionary and add key-value pairs as needed. Here's how to create the alien_0 dictionary from scratch:


alien_0 = {}  # Start with an empty dictionary
alien_0['color'] = 'green'  # Add color
alien_0['points'] = 5        # Add points
print(alien_0)  # Output: {'color': 'green', 'points': 5}


# This method is useful for storing user-supplied data or when generating many key-value pairs automatically.


#Time is Passing
Cureent_used_mails = ["harshparashar639@gmail.com" , "hparashar739@gmail.com" , "anon591303@gmail.com" ]
Used_username = ["hin90@" , "kimoha@13" , "Huj092!" , "Ouuehi877" , "uhrhuuhre0988&"]
Name = input("Enter your first name :")
name = Name.title()
Age = int(input("Please Enter your Age :"))
UserProfile1 = {}
UserProfile1["Name "] = name
UserProfile1["Age"] = Age
Username = input("Please enter a username :")
while Username in Used_username:
    print("Please try a another username that is already in use")
    Username = input("Please enter a username :")
    if Username not in Used_username:
        UserProfile1["Username "] = Username
        break
mail_id = input("Please enter your mail id :")
while mail_id in Cureent_used_mails:
    print("PLease Enter a new mail id that is already in use")
    mail_id = input("Please enter your mail id :")
    if mail_id not in Cureent_used_mails:
      UserProfile1["Mail Id : "] = mail_id
    break
Country = input("Please enter your coutry :")
UserProfile1["Country "] = Country
Phone_Number = int(input("Please enter your phone number :"))
if Country == "India":
    UserProfile1["Phone_number "] = f" +91 {Phone_Number}"
print(UserProfile1)




#                                                           Modifying Values in a Dictionary

# To modify values in a dictionary in Python, you can directly assign a new value to a specific key. Here's a simplified example using an alien's attributes:
# Define the Alien: Create a dictionary to represent the alien's properties, such as its position and speed.


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#Print Original Position: Display the alien's original x position.

print(f"Original position: {alien_0['x_position']}")

#Determine Movement: Use an if-elif-else statement to decide how far the alien should move based on its speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # fast alien

# Update Position: Add the increment to the alien's current x position and update the dictionary.


alien_0['x_position'] += x_increment
#Print New Position: Show the new x position after the move.

print(f"New position: {alien_0['x_position']}")

#Change Speed: You can change the alien's speed to affect its movement in future updates.

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # fast alien
alien_0['x_position'] += x_increment
print(f"New Position : {alien_0['x_position']}")

#Print New Speed: Display the updated speed.
# Example Output:
# Original position: 0
# New position: 2 (if speed is 'medium')
# This approach allows you to easily modify the alien's behavior by changing its attributes in the dictionary.




#                                                                   Removing Key-Value Pairs


#To remove a key-value pair from a dictionary in Python, you can use the del statement. Here's a simplified example:
#Define the Dictionary: Create a dictionary with some key-value pairs.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # Output: {'color': 'green', 'points': 5}
#Delete a Key-Value Pair: Use "del" to remove a specific key and its associated value.

del alien_0['points']
#Print the Updated Dictionary: Show the dictionary after the deletion.

print(alien_0)  # Output: {'color': 'green'}

#Print the Updated Dictionary: Show the dictionary after the deletion.

#Note : The deleted key-value pair is removed permanently from the dictionary.




#                                                             A Dictionary of Similar Objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Each key represents a person's name, and each value represents their favorite programming language.
# Accessing Values:
# To find out a specific person's favorite language, you can look it up using their name as the key. For example, to get Sarah's favorite language:

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Output:
# This will display: Sarah's favorite language is C.
# Formatting Tips:
# When defining a long dictionary, you can break it into multiple lines for better readability. Indent each new line and ensure the closing brace aligns with the first key-value pair. It's also good practice to include a comma after the last pair for future additions.
# This approach allows you to easily manage and access information about multiple objects in a structured way.



profile = {"Name" : "Harsh" ,
           "Age" : 18 ,
           "Gender" : "Male",
           "Phone" : 9547784506 }
Name = profile["Name"]
Age = profile['Age']
Gender = profile['Gender']
Phone = profile['Phone']
print(f"Name of the User : {Name}")
print(f"Age of the User  : {Age}")
print(f"Gender of the User : {Gender}")
print(f"Phone of the User : {Phone}")




#                                                              Using get() to Access Values


#When retrieving values from a dictionary using keys in square brackets, you may encounter a KeyError if the key does not exist. For example:
#Example of KeyError:

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])  # This will raise a KeyError


#Output
# Traceback (most recent call last):
#   File "c:\Users\admin\.android\PYTHON\Ch 6 Dictionaries.py", line 257, in <module>
#     print(alien_0['points'])  # This will raise a KeyError
#           ~~~~~~~^^^^^^^^^^
# KeyError: 'points'

# Handling Missing Keys:
# To avoid this error, you can use the get() method, which allows you to specify a default value if the key is not found. Here's how it works:
#Note : Using get() method to avoid these Errors




#                                                             Using get() Method:



alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)  # Output: No point value assigned.


profile = {"Name" : "Harsh"}
Gf = profile.get("Gf" , "You are still single motherfucker")
print(Gf)


#If the key 'points' or value exists, get() returns its value. If it doesn't, it returns the specified default message instead of raising an error.


# Note:
# If you use get() without a second argument and the key doesn't exist, it will return None, indicating the absence of a value without causing an error.
# sing get() is a safer way to access dictionary values when you're unsure if a key exists.





#                                                                   try it yourself

#  6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
#  6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
#  6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.


#Solution
Person = {"First Name " : "Akshita" ,
           "Last Name"  : "Thakur"  ,
           "Age" : 19 ,
           "City" : "Delhi" ,}
print(f"First Name : {Person["First Name "]}")
print(f"Last Name : {Person["Last Name"]}")
print(f"Age : {Person['Age']}")
print(f"City : {Person['City']}")

#Note This Data Reffered below is Real You also can use any data you want to use.
Favourite_Number  = {"Harsh" : 2 ,
                     "Akshita" : 2,
                     "Rohan" : 83 ,
                     "Anshik" : 5 ,
                     "Jesmie" : 2}

print(f" Harsh Favourite number is {Favourite_Number["Harsh"]}")
print(f" Akshita Favourite number is {Favourite_Number['Akshita']}")
print(f" Rohan Favourite number is {Favourite_Number['Rohan']}")
print(f" Priya Favourite number is {Favourite_Number['Anshik']}")
print(f" Jesmie Favourite number is {Favourite_Number['Jesmie']}")

Glossary = {"sort" : "A fumction is uesd in List to sort the list in a specific order",
              "in" : "in function is also used in list to show whether a element exist in a list",
            "not in" : "not in function is also used in list to show whether a element not exist in a list",
            "append" : "append function is used to add a element in a list",
            "pop" : "pop function is used to remove a element from a list",
            }

print(f"sort : \n{Glossary['sort']}")
print(f"in : \n{Glossary['in']}")
print(f"not in : \n{Glossary['not in']}")
print(f"append : \n{Glossary['append']}")
print(f"pop : \n{Glossary['pop']}")






#                                                                         Looping Through a Dictionary


# In Python, you can loop through a dictionary to access its key-value pairs, keys, or values. Here’s a brief overview of how to loop through a dictionary, using an example of user information.
# Define a Dictionary: Create a dictionary to store user information.

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Loop Through Key-Value Pairs: Use a for loop with the items() method to access each key-value pair.

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


#This will output:
# Key: username
# Value: efermi
# Key: first
# Value: enrico
# Key: last
# Value: fermi



#                                                                                    Looping Through All Keys


#In Python, you can loop through the keys of a dictionary using the keys() method or simply by iterating over the dictionary itself. Here’s a concise overview of how to do this with an example using a dictionary of favorite programming languages.


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


#Loop Through Keys: You can loop through the keys using either of the following methods:
#Method 1
for name in favorite_languages.keys():
    print(name.title())

#Method 2
for name in favorite_languages:
    print(name.title())

#Both methods will output the same result:
# Jen
# Sarah
# Edward
# Phil


#                                                                                            Accessing Values with Keys



# Accessing Values with Keys
# You can also access the values associated with the keys while looping. For example, if you want to send a special message to certain friends:


#Define a List of Friends:
friends = ['phil', 'sarah']


#Loop and Check for Friends:

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


#Output
# Jen
# Sarah
#     Sarah, I see you love C!
# Edward
# Phil
#     Phil, I see you love Python!



#                                                                                          Checking for a Key

# You can also use the keys() method to check if a specific person was polled. For example, to check if 'Erin' took the poll:

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Erin, please take our poll!

# Summary
# Use keys() to loop through all keys in a dictionary.
# You can access values using the keys during the loop.
# The keys() method can also be used to check for the existence of a specific key in the dictionary.




#                                                                                    Looping Through a Dictionary’s Keys in a Particular Order



# In Python 3.7 and later, dictionaries maintain the order of items as they are inserted. However, if you want to loop through a dictionary in a different order, you can use the sorted() function to sort the keys.

# Example of Sorting Keys in a Dictionary


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Loop Through Sorted Keys: Use the sorted() function to get the keys in order before looping through them.

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# This will display the names in alphabetical order:


#OUTPUT
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.




#                                                                                    Looping Through All Values in a Dictionary


# To loop through all values in a dictionary and get a list of unique items, you can use the values() method along with a set. Here's a simplified explanation:
# Using values(): You can retrieve all values from a dictionary using the values() method. For example:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


#OUTPUT
# The following languages have been mentioned:
# Python
# C
# Ruby
# Python



# This will print all chosen languages, including duplicates.
# Using a Set for Uniqueness: To avoid duplicates, you can convert the values to a set, which only keeps unique items:


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# #Output
# The following languages have been mentioned:
# Ruby
# C
# Python


# This will print each language only once, resulting in a cleaner list.
# Creating a Set: You can also create a set directly using braces:
# This will automatically filter out duplicates.
# Note: Sets do not maintain any specific order of items.



#                                                                                Try it yourself

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 99) by replacing your series of print() 
# calls with a loop that runs through the dictionary’s keys and values. When 
# you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should 
# automatically be included in the output.
#  6-5. Rivers: Make a dictionary containing three major rivers and the country 
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#  •	Use a loop to print a sentence about each river, such as The Nile runs 
# through Egypt.
#  •	Use a loop to print the name of each river included in the dictionary.
#  •	Use a loop to print the name of each country included in the dictionary.
#  6-6. Polling: Use the code in favorite_languages.py (page 97).
#  •	Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not. 
# •	Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take 
# the poll


#Solution:     

Glassory_2 = {"remove" : "To remove element from a lsit" ,
              "del" : "To prermanently remove something from the list",
              "insert" : "This function is used to insert an element at a specified position in the list" ,
              "capitalize" : "is basically used to convert the first character of a string in uppercase and rest of the characters in lowercase" ,
              "upper" : "is used to convert all the characters of a string in uppercase" ,
               }
for name , meaning in Glassory_2.items():
    print(f"{name.title()}:   \n {meaning}")


Rivers = {"Nile" : "Egypt" ,
          "Ganga" : "India" ,
          "Volga" : "Russia" ,
          }                             
for river , country in Rivers.items():
    print(f"The {river} flows through {country}")

for river in Rivers.keys():
    print(f"{river}")

for country in Rivers.values():
    print(f"{country}")


# Existing dictionary of favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# List of people who should take the poll
people_to_poll = ['jen', 'sarah', 'mike', 'anna', 'phil', 'john']
# Loop through the list of people
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"Hi {person.title()}, please take our favorite languages poll!")


favorite_languages = {
    "Harsh" : "Python" ,
    "Anshika" : "C++" ,
    "Vedansh" : "Java" ,
    "Jesmie" : "Swift",
}

person_to_poll = ["Harsh" , "Anshika" , "Kiny" , "John" , "Vedansh" , "Dhruv" , "Jesmie"]
for person , language in favorite_languages.items():
    if person in person_to_poll:
        print(f"{person.title()} , your favorite language is {language} .")
    else:
        print(f"{person.title ()} , you are not poll for the favourite languages Please pole it First ")





#                                                                        Nesting

# Nesting in Python allows you to store complex data structures, such as lists of dictionaries or dictionaries containing lists. This is particularly useful for managing collections of related data.
# Example: List of Dictionaries
# To manage a fleet of aliens, you can create a list where each alien is represented as a dictionary. Here's a simple example:



# Create individual alien dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# Store them in a list
aliens = [alien_0, alien_1, alien_2]

# Print each alien
for alien in aliens:
    print(alien)

#Output
# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}





#                                                                  Creating Multiple Aliens

# You can also generate a larger fleet of aliens using a loop:

# Create an empty list for aliens
aliens = []

# Generate 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Show total number of aliens
print("Total number of aliens: " + str(len(aliens)))


#Output
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# Total number of aliens: 30



#                                                                        Modifying Aliens

# You can modify specific aliens based on their attributes. For example, to change the first three green aliens to yellow:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens after modification
for alien in aliens[:5]:
    print(alien)


#Output 
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
#...

#Summary
# Nesting allows you to create complex data structures, such as lists of dictionaries, which can be easily manipulated. This is useful for scenarios like managing a game with multiple entities, where each entity has various attributes.



#                                                                            A List Inside a Dictionary


# You can store multiple values for a single key in a dictionary by using a list. For example, when describing a pizza order:
# Dictionary for pizza order

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping) #/t is basically use to work like a tab



# You ordered a thick-crust pizza with the following toppings:
#     mushrooms
#     extra cheese




#                                                                     A Dictionary Inside a Dictionary



#You can also nest dictionaries within dictionaries. For example, to store user information on a website:

#Dictionary for users
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
    }


# Loop through users and print their information
for username, user_info in users.items():
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\nUsername: " + username)
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


#Output
# Username: aeinstein
#         Full name: Albert Einstein
#         Location: Princeton

# Username: mcurie
#         Full name: Marie Curie
#         Location: Paris




#                                                          try It yourself


#  6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people . Loop through your list of people . As you 
# loop through the list, print everything you know about each person .  
# Chapter 6
# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the 
# name of a pet . In each dictionary, include the kind of animal and the owner’s 
# name . Store these dictionaries in a list called pets . Next, loop through your list 
# and as you do print everything you know about each pet .
#  6-9. Favorite Places: Make a dictionary called favorite_places . Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person . To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places . Loop through the dictionary, and print 
# each person’s name and their favorite places .
#  6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so 
# each person can have more than one favorite number . Then print each person’s 
# name along with their favorite numbers .
#  6-11. Cities: Make a dictionary called cities . Use the names of three cities as 
# keys in your dictionary . Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city . The keys for each city’s dictionary should be something like 
# country, population, and fact . Print the name of each city and all of the infor
# mation you have stored about it .
#  6-12. Extensions: We’re now working with examples that are complex enough 
# that they can be extended in any number of ways . Use one of the example pro
# grams from this chapter, and extend it by adding new keys and values, chang
# ing the context of the program or improving the formatting of the output . 



#Solution1
People = []
People1 = {"Name" : "Omu","DOB" : 1937 ,"Location" : "Lagos"}
People2 = {"Name" : "kin" , "DOB" : 1964 , "Location" : "USA"}
People3 = {"Name" : "Jin" , "DOB" : 1990 , "Location" : "China"}
People.append(People1)
People.append(People2)
People.append(People3)

for person in People:
    print(f"Name : {person["Name"]}")
    print(f"DOB : {person['DOB']}")
    print(f"Location : {person['Location']}\n")


#Solution2
#Creating a empty list
pets  = []

#Making three dictioniries showing each pet information
kitty = {"animal" : "Cat" , "owner" : "Kim"}
tuffy = {"animal" : "Dog" , "owner" : "Misti"}
chetak = {"animal" : "Horse" , "owner" : "Huby"}

#Appending all pets dictionaries in list 
pets.append(kitty)
pets.append(tuffy)
pets.append(chetak)


#Applying loop in the list to represent all the information about each pet we know
for pet in pets:
    print(f"Pet Type : {pet['animal']}")
    print(f"Owner name : {pet['owner']}\n")





#Solution3
#Creating a dictionery called favourite_places to strore persons name with thier facvourite place

favorite_places = {"Ransoi" : "USA" , "Kim" : "China" , "Muig" : "Mexico"} 

#Using for loop to print each person detail with thier favourite place

for name , place in favorite_places.items():
    print(f"Name of the person : {name}")
    print(f"Favourite place of the person : {place}\n")





#Solution4
#Just create a dictionary who stores person's favourite number according to thier name
favourite_number = {"Harsh" : [2,4,7,27,12,14] , "Jesmie" : [7,9,13,87] , "Kimoha" : [1,0,6,3,2] , "Hyb" : [5,34,2,2334,45,5]}

#Applying for loop to print all the favourite number according to persons name
for key , value in favourite_number.items():
    print(f"\nPerson name : {key}")
    print(f"Its favourite number are :  ")
    for val in value:
        print(f"{val}")



#You can also try this one 
# Creating a dictionary that stores each person's favorite numbers
favorite_numbers = {
    "Harsh": [2, 4, 7, 27, 12, 14],
    "Jesmie": [7, 9, 13, 87],
    "Kimoha": [1, 0, 6, 3, 2],
    "Hyb": [5, 34, 2, 2334, 45, 5]
}

# Applying a for loop to print all the favorite numbers according to each person's name
for name, numbers in favorite_numbers.items():
    print(f"\nPerson's name: {name}")
    print("Their favorite numbers are: ", end="")
    print(", ".join(map(str, numbers)))  # Join the numbers into a single string for better formatting




#Solution5

#Creating a dictionary that contains key as the name of the city and value as the details of the city

city = {"Tokyo" : {"Country" : "Japan" , "Population" : 37.4 , "Fact" : "Tokyo is known for its unique blend of traditional culture and cutting-edge technology, featuring ancient temples alongside modern skyscrapers"} , "Delhi" : {"Country" : "India" , "Population" : 29.3,"Fact" : " Delhi has a rich history that spans over 2,000 years, making it a city filled with historical landmarks and cultural diversity."} , "Shanghai" : {"Country" : "China" , "Population" : 26.3 , "Fact" : " Once a small fishing village, Shanghai has transformed into a global financial hub and is known for its impressive skyline and vibrant economy."}}


#Using for loop to print all infomation about each city store in the dictionery
for city , information in city.items():
    print(f"\nName of the city : {city}")
    print(f"Country : {information['Country']}")
    print(f"Population of city in million's : {information['Population']}")
    print(f"Intresting fact about the city : {information['Fact']}")



#Solution6
# Let's take the previous example of the cities dictionary and extend it by adding new keys and values. We can include additional information such as the area of the city (in square kilometers) and the year it was founded. Additionally, we can improve the formatting of the output to make it more visually appealing.

# Here’s the extended version of the cities program:

# Creating a dictionary that contains key as the name of the city and value as the details of the city
cities = {
    "Tokyo": {
        "Country": "Japan",
        "Population": 37.4,
        "Area (sq km)": 2191,
        "Year Founded": 1603,
        "Fact": "Tokyo is known for its unique blend of traditional culture and cutting-edge technology, featuring ancient temples alongside modern skyscrapers."
    },
    "Delhi": {
        "Country": "India",
        "Population": 29.3,
        "Area (sq km)": 1484,
        "Year Founded": '6th century BC',
        "Fact": "Delhi has a rich history that spans over 2,000 years, making it a city filled with historical landmarks and cultural diversity"
    },
    "Shanghai": {
        "Country": "China",
        "Population": 26.3,
        "Area (sq km)": 6340,
        "Year Founded": 1291,
        "Fact": "Once a small fishing village, Shanghai has transformed into a global financial hub and is known for its impressive skyline and vibrant economy."
    }
}

# Using a for loop to print all information about each city stored in the dictionary
for city, information in cities.items():
    print(f"\n{'-' * 40}")
    print(f"Name of the city: {city}")
    print(f"Country: {information['Country']}")
    print(f"Population (in millions): {information['Population']}")
    print(f"Area (in sq km): {information['Area (sq km)']}")
    print(f"Year Founded: {information['Year Founded']}")
    print(f"Interesting fact about the city: {information['Fact']}")
    print(f"{'-' * 40}")




# This output provides a comprehensive overview of each city, including additional details that enhance the information presented


#                                                     Summary of this chapter 

# In this chapter you learned how to define a dictionary and how to work 
# with the information stored in a dictionary. You learned how to access and 
# modify individual elements in a dictionary, and how to loop through all of 
# the information in a dictionary. You learned to loop through a dictionary’s 
# key-value pairs, its keys, and its values. You also learned how to nest multiple 
# dictionaries in a list, nest lists in a dictionary, and nest a dictionary inside 
# a dictionary.
#  In the next chapter you’ll learn about while loops and how to accept 
# input from people who are using your programs. This will be an exciting 
# chapter, because you’ll learn to make all of your programs interactive: 
# they’ll be able to respond to user input

















    




























































