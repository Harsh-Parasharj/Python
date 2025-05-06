








#                                               Ch 7  Functions with Harsh parashar





# In this chapter, you'll learn how to write functions, which are named blocks of code designed to perform specific tasks. Instead of rewriting code for the same task multiple times, you can simply call the function, making your programs easier to write, read, test, and fix.
# You'll also discover how to pass information to functions and differentiate between functions that display information and those that process data and return values. Finally, you'll learn how to store functions in separate files called modules to better organize your main program files.
#Functions are also called as subroutines and procedures
#There are two type of functions 
#1 User defined Functions 
#2 Library Functions 


#                                               Defining a Function




# # # Here's a simple function called greet_user() that prints a greeting:

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()


# # # Function Definition: The line def greet_user(): defines the function. The parentheses are required, even if they are empty.
# # # Docstring: The line with triple quotes describes what the function does.
# # # Function Body: The indented line print("Hello!") is the code that runs when the function is called.
# # # When you call the function with greet_user(), it executes the code inside and prints "Hello!".

# # #Output
# # # Hello!




# # #                                                             Passing Information to a Function


# # # You can modify the function to greet users by name:


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


# Parameter: The function now takes a parameter username, allowing you to pass a name when calling the function.
# Function Call: When you call greet_user('jesse'), it prints "Hello, Jesse!".
# You can call greet_user() multiple times with different names, like greet_user('sarah'), which will print "Hello, Sarah!".
# This way, the function can provide personalized greetings based on the input name




# In the greet_user() function, the variable username is a parameter, which is the information the function needs to perform its task. When you call the function with a specific value, like greet_user('jesse'), the value 'jesse' is called an argument.

# To summarize:

# Parameter: A variable in the function definition that specifies what information the function needs (e.g., username).
# Argument: The actual value passed to the function when it is called (e.g., 'jesse').
# It's important to note that people sometimes use the terms "arguments" and "parameters" interchangeably, so you may encounter this variation in terminology.




#                                                                             Try It yourself

#  8-1. Message: Write a function called display_message() that prints one sen
# tence telling everyone what you are learning about in this chapter . Call the 
# function, and make sure the message displays correctly .
#  8-2. Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title . The function should print a message, such as One of my 
# favorite books is Alice in Wonderland . Call the function, making sure to 
# include a book title as an argument in the function call





#Solution1 

# # """Very firstly  we def a function """
def display_message():
    """Give function some task"""
    print("We lean in this chapter how we can make a function \nhow we can pass parameter\nand how we cam call a function" )

display_message()


# # #Solution2
# # """"First we define a function and name it favorite_book then we pass a parameter that ask user for the title of the back and after it return a message to the user when user pass the title of the book"""
def favorite_book(title):
    print(f"\nOne of my favourite book is {title}")

favorite_book("The Midnight Library by Matt Haig")






#                                                           Passing Arguements        


    
# When calling a function with multiple parameters, you can pass arguments in several ways:
# Positional Arguments: Arguments must be in the same order as the parameters in the function definition.
# Keyword Arguments: Each argument is specified by a parameter name, allowing you to pass them in any order.
# Lists and Dictionaries: You can also pass collections of values, such as lists or dictionaries, to the function.
# These methods provide flexibility in how you provide data to your functions.







#                                                            Positional Arguments




# When calling a function in Python, positional arguments must match the order of parameters in the function definition.
# For example, consider the function describe_pet:


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# When you call it like this:

describe_pet('hamster', 'harry')


# The argument 'hamster' is assigned to animal_type.
# The argument 'harry' is assigned to pet_name.
# The output will be:


# I have a hamster.
# My hamster's name is Harry.
# This demonstrates how positional arguments work by matching the order of the provided values to the function's parameters.





#                                                                           Multiple Function Calls



# Calling Functions Multiple Times
# You can call a function as many times as needed with different arguments. For example, using the describe_pet function:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# You can describe multiple pets like this:
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#Output:
# I have a hamster.
# My hamster's name is Harry.
# I have a dog.
# My dog's name is Willie.


# This shows that you can efficiently describe different pets by calling the function multiple times. The function's code is written once, and you can reuse it with new information, regardless of how long the function is. You can use as many positional arguments as needed, and Python will match them to the corresponding parameters in the function definition.



#                                                                      Order Matters in Positional arguments


# Order of Positional Arguments
# When using positional arguments, the order in which you pass them matters. If you mix up the order, you can get unexpected results.
# For example, consider the function:



def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")



#  If you call it like this:

describe_pet('harry', 'hamster')

# OUTPUT
# I have a harry.
# My harry's name is Hamster.


# Here, 'harry' is incorrectly assigned to animal_type, and 'hamster' to pet_name. To avoid such issues, always ensure that the order of arguments in your function call matches the order of parameters in the function definition.







#                                                                      Keyword Arguments


# A keyword argument is a name-value pair passed to a function, allowing you to specify which parameter each value corresponds to. This eliminates confusion about the order of arguments and clarifies their roles.

# For example, using the describe_pet function:

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")




# #You can call it with keyword arguments like this:

describe_pet(animal_type='hamster', pet_name='harry')

# #This ensures that 'hamster' is assigned to animal_type and 'harry' to pet_name, producing the correct output:
# # I have a hamster.
# # My hamster's name is Harry.


# The order of keyword arguments does not matter, so you can also call it like this:
describe_pet(pet_name='harry', animal_type='hamster')

#Just remember to use the exact parameter names from the function definition when using keyword argument





 #                                                   Default Values




# Default Values in Function Parameters
# When defining a function, you can set default values for parameters. If an argument is provided in the function call, Python uses that value; if not, it uses the default. This can simplify function calls and clarify typical usage.

# For example, you can modify the describe_pet function to have a default value for animal_type:

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# # # Now, you can call it with just the pet's name:
describe_pet(pet_name='willie')


#Output:
# I have a dog.
# My dog's name is Willie.

#If you want to describe a different animal, you can still provide an explicit argument:

describe_pet(pet_name='harry', animal_type='hamster')

# Note: When using default values, parameters with default values must be listed after those without default values to ensure correct interpretation of positional arguments.





#                                                                 Equivalent Function Calls


#Combining Positional Arguments, Keyword Arguments, and Default Values


# You can use positional arguments, keyword arguments, and default values together when calling a function, allowing for multiple equivalent ways to call it.
# For example, with the function defined as:



def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")



# You must always provide an argument for pet_name, which can be done using either positional or keyword format. If the animal is not a dog, you can specify animal_type in either format as well.

# Here are several valid calls to the function:

# For a dog named Willie:

describe_pet('willie')
describe_pet(pet_name='willie')

#For a hamster named Harry:

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# All of these calls will produce the same output.
# Note: Choose the calling style that you find easiest to understand; the output will remain the same regardless of the style used.





#                                                                      Avoiding Argument Errors


# Handling Unmatched Arguments in Functions
# When using functions, you may encounter errors related to unmatched arguments, which occur when you provide too few or too many arguments.

# For example, if you call the describe_pet function without any arguments:

describe_pet("animal","nui","kino")


# Python will raise an error indicating that required arguments are missing:

# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
# TypeError: describe_pet() takes from 1 to 2 positional arguments but 3 were given



# The error message includes a traceback that shows where the problem occurred, helping you identify the missing arguments. This feature allows you to correct the function call without needing to open the function's code.

# Providing descriptive names for your variables and functions can make these error messages more informative and helpful for you and others using your code.

# If you provide too many arguments, you'll receive a similar error message, guiding you to match your function call with its definition correctly.





#                                                                 Try It yourself


#  8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt . The function should print 
# a sentence summarizing the size of the shirt and the message printed on it .
#  Call the function once using positional arguments to make a shirt . Call the 
# function a second time using keyword arguments .
#  8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python . Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message .
#  8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country . The function should print a simple sentence, such as 
# Reykjavik is in Iceland . Give the parameter for the country a default value . 
# Call your function for three different cities, at least one of which is not in the 
# default country


#Solution1
def make_shirt(size , message):
    """Print a sentence about the size and message on the shirt"""
    print(f"\nThe size of the shirt is {size} and message printed on the shirt is {message}")


make_shirt("L" , "Code to Survive")
make_shirt(message="I love python" , size="M")



#Solution2
def make_shirt(size = "L" , message = "I love Python"):
    """Print a sentence about the size and message on the shirt"""
    print(f"\nThe size of the shirt is {size} and message printed on the shirt is {message}")

make_shirt()
make_shirt("M")
make_shirt(message = "Hack the Cox")



# Solution3
def describe_city(City_name , Country = "America"):
    """Printing a simple message that describe city name with its country """
    print(f"{City_name} is in {Country}")

describe_city("New York")
describe_city("Chicago")
describe_city(Country="India" , City_name="Delhi")





#                                                                       Return Values

# Return Values in Functions
# A function can process data and return a value instead of displaying it directly. The value returned by the function is called a return value. The return statement sends a value back to the point where the function was called.
# Using return values allows you to delegate complex tasks to functions, simplifying the main body of your program.





#                                                                     Returning a Simple Value



# Formatting Names with a Function


#The get_formatted_name() function takes a first and last name as parameters and returns a neatly formatted full name. Here's how it works:




#                                                                  Formatting Names with a Function


#   The get_formatted_name() function takes a first and last name as parameters and returns a neatly formatted full name. Here's how it works:


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# The function combines the first and last names, adds a space, and converts the result to title case.
# The returned value is stored in the variable musician, which outputs "Jimi Hendrix".
# While it may seem simpler to just print "Jimi Hendrix", using a function is beneficial in larger programs where you need to handle many names separately. You can store first and last names and call the function whenever you need to display the full name.




#                                                                         Making an Argument Optional



# Making Function Arguments Optional with Default Values
# You can make function arguments optional by using default values. For example, to expand the get_formatted_name() function to handle middle names, you can set the middle_name argument to an empty string by default:



def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()



# Example Usage:
# For a name with no middle name:


musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Output: Jimi Hendrix


# For a name with a middle name:

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)  # Output: John Lee Hooker


# Explanation:
# The middle_name parameter is optional and is placed last in the function definition.
# The function checks if a middle name is provided. If it is, it combines the first, middle, and last names; if not, it combines just the first and last names.
# This approach allows the function to handle names with or without middle names while keeping function calls simple and flexible.





#                                                   Returning a Dictionary


# Returning Complex Data Structures from Functions
# A function can return various types of values, including complex data structures like dictionaries. For example, the build_person() function creates a dictionary representing a person:


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix'}



# Explanation:
# The function takes a first and last name, stores them in a dictionary with keys 'first' and 'last', and returns the dictionary.
# This allows you to work with the information in a structured way, rather than just printing it.



# Extending the Function:
# You can easily modify the function to include additional information, such as age:



def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # Output: {'first': 'jimi', 'last': 'hendrix', 'age': 27}



# Summary:
# The modified function now accepts an optional age parameter. If provided, it adds the age to the dictionary.
# This approach allows you to store and manage various pieces of information about a person in a meaningful way





#                                                           Using a Function with a while Loop


# Using Functions with Loops for User Input
# You can combine functions with loops to create interactive programs. For example, the get_formatted_name() function can be used in a loop to greet users by their names:


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
        
    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")



# Explanation:
# The program prompts the user for their first and last names in a loop.
# A message is displayed to inform the user how to quit the program by entering 'q'.
# If the user enters 'q' at either prompt, the loop breaks, and the program ends.
# This allows the program to greet users continuously until they choose to exit.



# Example Output:
# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: eric
# Last name: matthes
# Hello, Eric Matthes!
# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: q

# This structure makes the program user-friendly and easy to exit.



#                                                                          Try it yourself 


#  8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country . The function should return a string formatted like this:
#  "Santiago, Chile"
#  Call your function with at least three city-country pairs, and print the value 
# that’s returned .
#  8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album . The function should take in an artist name and an 
# album title, and it should return a dictionary containing these two pieces of 
# information . Use the function to make three dictionaries representing different 
# albums . Print each return value to show that the dictionaries are storing the 
# album information correctly .
#  Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album . If the calling line includes a value for the num
# ber of tracks, add that value to the album’s dictionary . Make at least one new 
# function call that includes the number of tracks on an album .
#  8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
# loop that allows users to enter an album’s artist and title . Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created . Be sure to include a quit value in the while loop


# Solution1
def city_Country(cityname , country):
    format = cityname + "," + " " + country
    return format
result = (city_Country("Delhi" , "India"))
print(result)
result = (city_Country("Mumbai" , "India"))
print(result)
result = (city_Country("Pune" , "India"))
print(result)
# Solution2
def make_album(artist_name , title ,numberoftracks=''):
    music_album = {"artist_name" : artist_name ,
                   "album_title" : title ,
                   }
    if numberoftracks:
        music_album["number_of_tracks"] = numberoftracks
        return music_album
    else:
        return music_album
album1 = make_album("Damien Hirst" , " Im With You : by Red Hot Chili Peppers")
print(album1)
album2 = make_album("Keith Haring" , "Duck Rock by Malcolm McLaren" , 23)
print(album2)
album3 = make_album("Bad Company" , "Bad Company")
print(album3)
#Solution3
def make_album(artist_name , title ,numberoftracks=''):
    music_album = {"artist_name" : artist_name ,
                   "album_title" : title ,
                   }
    if numberoftracks:
        music_album["number_of_tracks"] = numberoftracks
        return music_album
    else:
        return music_album
while True:
    print("\nPlease enter artist name :")
    print("Enter 'q' to quit")
    
    artistname  = input("Please enter your artist name :")
    if artistname.lower() == 'q':
        break
    title = input("Please enter album name :")
    if title.lower() == 'q':
        break
    print(f"The Artist name is {artistname} and its album title  is {title}")




#                                                Passing a list



#Here's a simplified explanation of how to pass a list to a function in Python to greet users:

#Code Example

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Explanation
# Function Definition: The greet_users() function takes a list of names as an argument.
# Looping Through the List: Inside the function, it loops through each name in the list and prints a personalized greeting.
# List of Usernames: A list called usernames is created with three names.
# Function Call: The list is passed to the greet_users() function, which outputs:

# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!

# Summary
# This approach allows you to easily greet multiple users by passing their names in a list to a function, making the code efficient and reusable.


#Simple a example to remind yourself

def sample(list):
    """Simply print a message to all people that are in list"""
    for name in list:
        print(f" Hi {name.title()} I know you love python")
names = ["Harsh" , "Prince" , "Jesmie"]
sample(names)





#                                                          Modifying a List in a Function




# When you pass a list to a function, the function can modify the list. This allows for efficient work with large amounts of data.
# Example: 3D Printed Models


# Define functions
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Main program
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



# Benefits:
# More organized code
# Easier to understand and maintain
# Functions can be reused
# Changes can be made in one place, affecting all calls to the function

# Output:
# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case

# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case



#                                         Preventing a Function from Modifying a List



# When you want to prevent a function from modifying the original list, you can pass a copy of the list instead. This is useful when you need to keep the original data intact after performing operations.


# How to Pass a Copy of a List
# You can create a copy of a list using slice notation [:]. For example:

print_models(unprinted_designs[:], completed_models)

# In this case, print_models() receives a copy of unprinted_designs, allowing it to modify the copy without affecting the original list.
# Benefits of Passing a Copy
# Preserves Original Data: The original list remains unchanged, which is useful for record-keeping.
# Function Flexibility: The function can still perform its tasks without losing access to the original data.
# Efficiency Consideration
# While passing a copy can be helpful, it's generally more efficient to pass the original list unless you specifically need to preserve the original data. Making a copy uses additional time and memory, especially with large lists.

# Summary
# Use [:] to pass a copy of a list to a function.
# Preserve the original list when necessary.
# Prefer passing the original list for efficiency unless a copy is needed.



#                                                         Try It yourself


#  8-9. Magicians: Make a list of magician’s names . Pass the list to a function 
# called show_magicians(), which prints the name of each magician in the list .
#  8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 . 
# Write a function called make_great() that modifies the list of magicians by add
# ing the phrase the Great to each magician’s name . Call show_magicians() to 
# see that the list has actually been modified .
#  8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the 
# function make_great() with a copy of the list of magicians’ names . Because the 
# original list will be unchanged, return the new list and store it in a separate list . 
# Call show_magicians() with each list to show that you have one list of the origi
# nal names and one list with the Great added to each magician’s name 



#Solution1 
magicianname = ["Harry Houdini",
"David Copperfield",
"Penn & Teller",
"Derren Brown",
"David Blaine",
"Dynamo",
"Jean-Eugène Robert-Houdin",
"Paul Daniels"
"Tommy Cooper"
"The Great Soprendo"
"Justin Willman"
"Gloria Dea"]

def magician_name(name_list):
    for name in name_list:
        print("\n" , name)



#Solution2
def magician_name(name_list):
    print("\nOriginal List : \n")
    for name in name_list:
        print(name)
def modify_names(name_list):
    print("\nModified List :\n")
    for i in (name_list):
        print(f"{i} the great")

    
magician_name(magicianname)
modify_names(magicianname)


#Solution3
# Function to display the names of magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function to modify the list of magicians by adding "the Great"
def make_great(magicians):
    # Create a new list to store modified names
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " the Great")
    return great_magicians

# List of magicians
magicians = ['Harry Houdini', 'David Copperfield', 'Penn & Teller', 
             'Derren Brown', 'David Blaine', 'Dynamo']

# Show original list of magicians
print("Original list of magicians:")
show_magicians(magicians)

# Create a new list with "the Great" added to each magician's name
great_magicians = make_great(magicians)

# Show modified list of magicians
print("\nModified list of magicians:")
show_magicians(great_magicians)



#                                            Passing an arbitrary number of arguments



# In Python, you can create a function that accepts an arbitrary number of arguments using the asterisk (*) syntax. This allows you to collect multiple values into a tuple.
# For example, consider a function that builds a pizza with various toppings:


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# In this code:

# The *toppings parameter collects all the arguments passed to the function into a tuple named toppings.
# The function then prints each topping, regardless of whether one or multiple toppings are provided.




# Making a pizza with the following toppings:
# - pepperoni

# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese




#                                                Mixing Positional and Arbitrary Arguments




# In Python, when defining a function that accepts different types of arguments, the parameter for arbitrary arguments (using *) must be placed last. This allows the function to first match positional and keyword arguments before collecting any remaining arguments.

# For example, if you want to create a pizza function that takes a size and an arbitrary number of toppings, you would define it like this:

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# In this code:
# The size parameter captures the first argument (the pizza size).
# The *toppings parameter collects any additional arguments (the toppings) into a tuple.



# Output:
# Making a 16-inch pizza with the following toppings:
# - pepperoni
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# This structure ensures that the size is printed first, followed by the toppings.




#                                               Using Arbitrary Keyword Arguments


# In Python, you can create functions that accept an arbitrary number of keyword arguments using the double asterisk (**) syntax. This is useful for situations where you want to gather various pieces of information without knowing in advance what they will be.

# Example: Building User Profiles
# Here's a function that builds user profiles:

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)



# Key Points:
# The function build_profile() takes a first name and a last name as required parameters, and it accepts any number of additional keyword arguments through **user_info.
# Inside the function, an empty dictionary profile is created to store the user's information.
# The first and last names are added to this dictionary, and a loop adds any additional key-value pairs from user_info.
# The function returns the complete profile as a dictionary.

{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}

# This approach allows the function to handle any number of additional attributes, making it flexible for various user profiles. You can mix positional, keyword, and arbitrary arguments in your functions, which is a common practice in Python programming.



#                                                          Try It yourself


#  8-12. Sandwiches: Write a function that accepts a list of items a person wants 
# on a sandwich . The function should have one parameter that collects as many 
# items as the function call provides, and it should print a summary of the sand
# wich that is being ordered . Call the function three times, using a different num
# ber of arguments each time .
#  8-13. User Profile: Start with a copy of user_profile.py from page 153 . Build 
# a profile of yourself by calling build_profile(), using your first and last names 
# and three other key-value pairs that describe you .
#  8-14. Cars: Write a function that stores information about a car in a diction
# ary . The function should always receive a manufacturer and a model name . It 
# should then accept an arbitrary number of keyword arguments . Call the func
# tion with the required information and two other name-value pairs, such as a 
# color or an optional feature . Your function should work for a call like this one:
#  car = make_car('subaru', 'outback', color='blue', tow_package=True)
#  Print the dictionary that’s returned to make sure all the information was 
# stored correctly

#Solution1 
def sandwich(items):
    print("\nMaking your sandwich with following toopings :")
    for item in items:
        print("-" , item)
sandwich_toppings = [
    "Lettuce",
    "Tomato",
    "Onion",
    "Cheese",
    "Turkey",
    "Ham",
    "Bacon",
    "Avocado",
    "Cucumber",
    "Pickles",
    "Mustard",
    "Mayonnaise",
    "Hummus",
    "Roasted Red Peppers",
    "Spinach",
    "Jalapeños"
]
sandwich(sandwich_toppings)


# #Solution2
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Create a profile for yourself
my_profile = build_profile(
    'YourFirstName',  # Replace with your first name
    'YourLastName',   # Replace with your last name
    location='YourCity',  # Replace with your city
    hobby='YourHobby',     # Replace with your hobby
    profession='YourProfession'  # Replace with your profession
)

# Print the profile
print(my_profile)

# Solution3
def car_info(manufacturer , model_name , **other_information):
    car_information = {}
    car_information["manufacturer"] = manufacturer
    car_information["model_name"] = model_name
    for key,value in other_information.items():
        car_information[key] = value
    return car_information
    
carz = car_info('subaru', 'outback', color='blue', feature='full_open_sunroof' ,engine='1892hp')
print(carz)


        
#                                                      Storing your functions in modules


# Functions help organize code and make programs easier to read by using descriptive names. You can enhance this organization by storing functions in a separate file, called a module, and importing it into your main program. This approach hides implementation details, focuses on higher-level logic, and allows for code reuse across different programs. It also enables sharing functions with others without sharing the entire program. Additionally, knowing how to import modules lets you use libraries created by other programmers. There are various methods to import a module, which will be explained shortly.





#                                                       Importing an Entire Module


# To import functions in Python, you first create a module, which is a .py file containing the desired code. Here's how to do it with an example:


# Create a module (pizza.py):




#Create a separate file to use the module (making_pizzas.py):


# making_pizzas.py
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# How it works:

# The line import pizza allows you to use any function defined in pizza.py.
# You call the function using the syntax module_name.function_name(), like pizza.make_pizza().


#Output:
# Making a 16-inch pizza with the following toppings:
# - pepperoni

# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese






#                                                         Importing Specific Functions



#You can import specific functions from a module using the following syntax:

# from module_name import function_name

#You can import multiple functions by separating their names with commas:


#You can import multiple functions by separating their names with commas:
    

#from module_name import function_0, function_1, function_2


# #For example, in making_pizzas.py, if you only want to import the make_pizza function from the pizza module, you would write:


#Here module is the file_name and 
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# With this method, you can call the function directly by its name without using dot notation, since you've explicitly imported it.




#                                                  Using as to Give a Function an Alias


# If you want to avoid name conflicts or simplify long function names when importing, you can create an alias for a function using the as keyword. This allows you to give the function a shorter, unique name.

#For example, to import the make_pizza() function from the pizza module and give it the alias mp, you would write:


from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


#If you want to avoid name conflicts or simplify long function names when importing, you can create an alias for a function using the as keyword. This allows you to give the function a shorter, unique name.

#For example, to import the make_pizza() function from the pizza module and give it the alias mp, you would write:

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# In this case, make_pizza() is renamed to mp() in your program. You can now call the function using mp() instead, avoiding confusion with any other make_pizza() functions you may have defined.
# The general syntax for creating an alias is:

#from module_name import function_name as fn




#                                                     Importing All Functions in a Module



#You can import all functions from a module using the asterisk (*) operator:

from pizza import *


#This imports every function from the pizza module, allowing you to call them directly by name without dot notation. For example:


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# However, using this method is not recommended for larger modules, as it can lead to name conflicts if the module contains functions with the same names as those in your project. This could result in unexpected behavior, as existing functions may be overwritten.
# A better practice is to import only the specific functions you need or to import the entire module and use dot notation. This approach keeps your code clear and easy to understand. You may encounter the following import statement in other people's code:


#from module_name import *




#                                                    Styling functions


# When styling functions in Python, keep the following guidelines in mind:

# Descriptive Names: Use lowercase letters and underscores for function and module names to clearly convey their purpose.

# Docstrings: Every function should include a concise comment (docstring) immediately after the definition, explaining what the function does. This helps others understand how to use it.

# Default Parameter Values: When specifying default values for parameters, do not include spaces around the equal sign:


#def function_name(parameter_0, parameter_1='default value'):


#Keyword Arguments: Use the same convention for keyword arguments in function calls:

#function_name(value_0, parameter_1='value')


#Line Length: Limit lines of code to 79 characters for better readability. If a function's parameters exceed this length, break the line after the opening parenthesis and indent subsequent lines:


# def function_name(
#     parameter_0, parameter_1, parameter_2,
#     parameter_3, parameter_4, parameter_5):
#   function body...



# Separation of Functions: Use two blank lines to separate multiple functions for clarity.

# Import Statements: Place all import statements at the beginning of the file, unless you have comments describing the program.

# Following these conventions helps create clear, maintainable, and readable code.




#                                                         Try It yourself


# 8-15. Printing Models: Put the functions for the example print_models.py in a 
# separate file called printing_functions.py . Write an import statement at the top 
# of print_models.py, and modify the file to use the imported functions .
#  8-16. Imports: Using a program you wrote that has one function in it, store that 
# function in a separate file . Import the function into your main program file, and 
# call the function using each of these approaches:
#  import module_name
#  from module_name import function_name
#  from module_name import function_name as fn
#  import module_name as mn
#  from module_name import *
#  8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
# and make sure they follow the styling guidelines described in this section 




#Solution1 

from print_mode import print_models , completed_models
unprint_model = ["Tesla1" , "Tesla2" , "Tesla0-" , "teslamk"]
completed_model = []
print_models(unprint_model , completed_model)
completed_models(completed_model)


# In your main script (e.g., print_models.py)

from print_mode import print_models, completed_models  # Correct module name and function name
unprinted_models = ["Tesla1", "Tesla2", "Tesla0-", "teslamk"]  # Use consistent naming
completed_model = []
print_models(unprinted_models, completed_model)  # Call the function with the correct variable
completed_models(completed_model)  # Call the function with the correct name


# Solution2


# greetings.py
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")


# Step 2: Create the Main Program File
# Next, create a main program file named main.py where you will import the function using different methods.
# main.py
# Method 1: Import the entire module
# import greetings
# greetings.greet("Alice")  # Call the function using the module name

# Method 2: Import a specific function
# from greetings import greet

# greet("Bob")  # Call the function directly

# Method 3: Import a function with an alias
#from greetings import greet as greet_user
greet_user("Charlie")  # Call the function using the alias
# Method 4: Import the entire module with an alias
#import greetings as g

#greet("Diana")  # Call the function using the alias

# Method 5: Import all functions from the module
#from greetings import *
greet("Eve")  # Call the function directly
# Run the Main Program
# Now, you can run the main.py file. It will import the greet function from the greetings.py module using different import methods and call the function with different names.
# Expected Output
# When you run main.py, you should see the following output:

# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
# Hello, Diana!
# Hello, Eve!



# Solution3
# To demonstrate how to apply the styling guidelines to three different programs, I will provide examples based on common tasks that might have been covered in this chapter. Each example will follow the recommended styling conventions, including descriptive function names, proper indentation, docstrings, and consistent naming.
# Example 1: Printing Models
# printing_functions.py:

def print_models(unprinted_models, completed_models):
    """Prints the models being printed and adds them to completed models."""
    print("Printing Models:")
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"- {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Displays the completed models."""
    print("The following are the completed models:")
    for model in completed_models:
        print(f"- {model}")
# main.py:

from printing_functions import print_models, show_completed_models

unprinted_models = ["Tesla1", "Tesla2", "Tesla0-", "teslamk"]
completed_models = []

print_models(unprinted_models, completed_models)
# show_completed_models(completed_models)
# Example 2: Simple Calculator
# calculator.py:

# python

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# main_calculator.py:

# python

# from calculator import add, subtract, multiply, divide

num1 = 10
num2 = 5
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

# Example 3: Greeting Users
# greetings.py:
# python

def greet(name):
    """Print a greeting message for the given name."""
    print(f"Hello, {name}!")

def farewell(name):
    """Print a farewell message for the given name."""
    print(f"Goodbye, {name}!")

# main_greetings.py:
# python

#from greetings import greet, farewell
user_name = "Alice"
greet(user_name)
farewell(user_name)
# Summary of Styling Guidelines Applied:
# Descriptive Function Names: Each function name clearly indicates its purpose.
# Docstrings: Each function includes a docstring that describes what it does.
# Consistent Naming: Variable and parameter names are consistent and descriptive.
# Proper Indentation: Code is properly indented for readability.
# Separation of Concerns: Each program is organized into separate files for clarity and maintainability.
# By following these guidelines, the code becomes more readable, maintainable, and easier for others (or yourself in the future) to understand.




#                                                                Summary

# In this chapter, you learned how to write functions and pass arguments, enabling your functions to access the necessary information to perform their tasks. You explored positional and keyword arguments, as well as how to accept an arbitrary number of arguments. You also learned about functions that display output and those that return values, and how to use functions with lists, dictionaries, if statements, and while loops.
# Additionally, you discovered how to store functions in separate files (modules) to simplify your program files and enhance readability. You also learned to style your functions for better structure and clarity.
# Functions help you write simple, reusable code. Once a function is verified to work correctly, you can trust it to perform its task whenever called, allowing you to focus on other coding tasks. Modifying a function's behavior requires changing only one block of code, which updates all calls to that function.
# Using functions improves code readability, as good function names summarize their purpose, making it easier to understand the overall program flow compared to reading long code blocks.
# Functions simplify testing and debugging by breaking your program into smaller, manageable pieces, each with a specific task. This modular approach allows you to create separate test programs to verify that each function works correctly in various scenarios, giving you confidence in their reliability.
# In Chapter 9, you'll learn about classes, which combine functions and data into a cohesive unit, enabling flexible and efficient programming.



