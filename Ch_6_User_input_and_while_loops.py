



#                                       Chapter 7 User Input and while loops with Harsh Parashar

# In this chapter, you'll learn how to accept user input in your programs using the input() function. For example, if you want to check if someone is old enough to vote, you'll ask for their age and compare it to the voting age. You'll also discover how to keep your programs running as long as users want, using a while loop, allowing them to enter as much information as needed. This will enable you to create fully interactive programs.



#                                                    How the input() function works

#The input() function in Python pauses the program to wait for user input, which is then stored in a variable for further use. Here’s a simple example:

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


#In this example, the user is prompted to enter a message, which is then printed back to them.




#                                                     Writing Clear Prompts


#When using input(), always provide a clear prompt. For example:

# greeter.py
name = input("Please enter your name: ")
print("Hello, " + name + "!")


#Adding a space after the prompt helps separate it from the user's response:

#Output
# Please enter your name: Eric
# Hello, Eric!



#                                                        Multi-line Prompts


#If you need a longer prompt, you can store it in a variable:

# greeter.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")


#This allows for a more detailed prompt that spans multiple lines:

#Output
# If you tell us who you are, we can personalize the messages you see.
# What is your first name? Eric
# Hello, Eric!




#                                                    Using int() to Accept Numerical Input


#When using the input() function in Python, all user input is treated as a string. For example, if a user enters their age:

age = input("How old are you? ")


#If the user inputs 21, the value of age will be the string '21'. This can cause issues when trying to perform numerical comparisons, as shown below:

print(age >= 18)  # This will raise a TypeError


#Outtput
# Traceback (most recent call last):
#   File "c:\Users\HARSH\Documents\Python\Ch 7 user_input and while loops.py", line 83, in <module>
#     print(age >= 18)  # This will raise a TypeError
#           ^^^^^^^^^
# TypeError: '>=' not supported between instances of 'str' and 'int'




#To resolve this, you can use the int() function to convert the string input into an integer:

age = int(age)
print(age >= 18)

#Output
#True




#                                                      Example Program


#Here’s an example program that checks if a person is tall enough to ride a roller coaster:


#rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)  # Convert input to an integer
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# #In this program, the user's height is converted to an integer before comparing it to 36, allowing for accurate comparisons. For example:

#Output
# How tall are you, in inches? 71
# You're tall enough to ride!



#Note : Always remember to convert user input to a numerical type before performing calculations or comparisons.



#                                                     The Modulo Operator


#The modulo operator (%) is used to find the remainder of a division between two numbers. For example:



# we use float here to handle the decimal values
print(float(4 % 3)) # returns 1
print(float(5 % 3)) # returns 2
print(float(6 % 3))  # returns 0
print(float(7 % 3)) # returns 1



#If one number is divisible by another, the remainder will be 0. This property can be used to determine if a number is even or odd.


#Example Program
#Here’s a simple program that checks if a number is even or odd:

# even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)  # Convert input to an integer
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


#In this program, if the user enters 42, the output will be:

#The number 42 is even.


#Note : This works because even numbers have a remainder of 0 when divided by 2 (number % 2 == 0). If the remainder is not 0, the number is odd.




# In Python 2.7, use the raw_input() function to accept user input, as it treats all input as a string, similar to input() in Python 3. The input() function in Python 2.7 evaluates the input as Python code, which can lead to errors or unintended code execution. Therefore, always use raw_input() for safe user input in Python 2.7.



#                                                          try It yourself
#  7-1. Rental Car: Write a program that asks the user what kind of rental car they 
# would like . Print a message about that car, such as “Let me see if I can find you 
# a Subaru .”
#  7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group . If the answer is more than eight, print a message say
# ing they’ll have to wait for a table . Otherwise, report that their table is ready .
#  7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not.



#Solution1

#Firstly Storing input prompt into a variable 

# prompt = "What kind of rental car you like  : "

# #Then wait for user input what kind of car he/she need
user_input = input(prompt)

# #Now print the details 
print(f"Let me see if I can found a {user_input}")



#Solution2

#Firstly Storing input prompt into a variable 

prompt = "Please tell me how many people are in your dinner group : "


# #Asking from the user for the number of 

user_input = input(prompt)

# #Converting user input into integer
user_input = int(user_input)

# #Comparing user input with condition and giving output on the basis of the user_input
if user_input > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready")



#Solution3

#Storing prompt into a variable 
prompt = "Give me a number and i tell you whether the number is a multiple of 10 or not :"
user_input = input(prompt)
user_input = int(user_input)
if user_input % 10 == 0:
    print(f"{user_input} is a multiple of 10")
else:
    print(f"{user_input} is not a multiple of 10")







#                                                  Introduction to While Loops




# A while loop in programming repeatedly executes a block of code as long as a specified condition is true, unlike a for loop, which iterates over a collection of items.



# Example of a While Loop
# Here's a simple example that counts from 1 to 5:


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# Explanation:

# We start with current_number set to 1.
# The loop continues as long as current_number is less than or equal to 5.
# Inside the loop, it prints the current number and then increments it by 1.
# This repeats until current_number exceeds 5, at which point the loop stops.
# Output:
# 1
# 2
# 3
# 4
# 5


# Real-World Use
# While loops are commonly used in applications like games, where they keep running until the user decides to quit. They ensure that programs operate as intended, either continuing until a specific condition is met or stopping when requested



#                                                           Letting the User Choose When to Quit



# Parrot Program with While Loop

# The parrot.py program uses a while loop to keep running until the user decides to quit by entering a specific value ('quit'). Here's a simplified breakdown:

# Prompt Definition:
# A prompt is created to inform the user that they can enter a message or type 'quit' to exit.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# Initial Setup:
# A variable message is initialized as an empty string to allow the loop to start.
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)  # This will print 'quit' if entered


# Improvement:
# To prevent printing 'quit', an if statement checks the value of message before printing.


if message != 'quit':
    print(message)


#Final Code Example:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#Output Example:
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit



# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit


# This program effectively allows users to input messages repeatedly until they choose to exit by typing 'quit', without displaying 'quit' as a message.





#                                                         Using a Flag in Programs

# In more complex programs, like games, multiple events can cause the program to stop running. Instead of checking all conditions in a single while statement, we can use a flag—a variable that indicates whether the program should continue running.


# Example: Parrot Program with a Flag
# Define the Flag:
# We create a variable called active and set it to True to indicate that the program is currently running.


active = True

#While Loop:
# The loop continues as long as active is True.

while active:


# User Input and Condition Check:
# Inside the loop, we check the user's input. If they enter 'quit', we set active to False, which stops the loop. If they enter anything else, we print their message.

   message = input(prompt)
   if message == 'quit':
      active = False
   else:
      print(message)



#Final Code Example:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


#Benefits of Using a Flag:
 
# Simplifies the While Statement: The loop only checks one condition (the flag).
# Easily Extendable: Additional conditions can be added to set the flag to False for other events, making it suitable for complex programs like games.
# This approach allows for better organization and management of multiple exit conditions in a program




#                                                           Using break to Exit a Loop

# The break statement allows you to exit a loop immediately, regardless of any remaining code or conditions. This is useful for controlling the flow of your program.

# Example: City Input Program
# In this example, the program asks the user to enter names of cities they have visited and exits the loop when the user types 'quit':

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:  # This loop will run indefinitely
    city = input(prompt)
    if city == 'quit':
        break  # Exit the loop if the user types 'quit'
    else:
        print("I'd love to go to " + city.title() + "!")

# How It Works:
# The loop starts with while True, meaning it will run forever until a break statement is encountered.
# When the user enters 'quit', the break statement is executed, and the loop stops.
# If the user enters a city name, the program responds with a message.


#Output Example:
# Please enter the name of a city you have visited: 
# (Enter 'quit' when you are finished.) New York 
# I'd love to go to New York! 
# Please enter the name of a city you have visited: 
# (Enter 'quit' when you are finished.) quit


# Note:
# The break statement can be used in any loop in Python, including for loops, to exit the loop early.



#                                                       Using continue in a Loop

# Using continue in Loops
# The continue statement allows you to skip the rest of the code in the current iteration of a loop and return to the beginning. This is useful when you want to ignore certain conditions.

# Example: Printing Odd Numbers
# Here's a loop that counts from 1 to 10 but only prints odd numbers:

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Skip even numbers
    print(current_number)


#Output:
# 1
# 3
# 5
# 7
# 9



#                                                     Avoiding Infinite Loops

# Every while loop needs a way to stop running. For example, this loop counts from 1 to 5:

x = 1
while x <= 5:
    print(x)
    x += 1

#If you forget to increment x, like this:

x = 1
while x <= 5:
    print(x)  # This will run forever



# The loop will run indefinitely, printing 1 repeatedly.

# Tips to Avoid Infinite Loops:
# Test Your Loops: Ensure that the loop has a condition that will eventually become False.
# Check Exit Conditions: Make sure there’s a way for the loop to exit, either by changing a variable or using a break statement.
# Stopping an Infinite Loop: If you find yourself in an infinite loop, you can stop it by pressing Ctrl+C or closing the terminal window.


# Note:
# Some text editors with embedded output windows may make it difficult to stop an infinite loop, and you might need to close the editor to end the loop.


#                                                         try It yourself

#  7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value . As they enter each topping, 
# print a message saying you’ll add that topping to their pizza .
#  7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age . If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15 . Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket .
#  User Input and while Loops   
# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:
#  •	Use a conditional test in the while statement to stop the loop .
#  •	Use an active variable to control how long the loop runs .
#  •	Use a break statement to exit the loop when the user enters a 'quit' value .
#  7-7. Infinity: Write a loop that never ends, and run it . (To end the loop, press 
# ctrl-C or close the window displaying the output .)


#Solution1
prompt1 = "Enter a series of pizza toopings & "
prompt1 += "Enter 'quit' to end the program : "
user_input = ""
while user_input != 'quit':
    user_input = input(prompt1)
    if user_input != 'quit':
      print("you will add that tooping to thier pizza")


prompt = "Please enter your age :"
user_input = input(prompt)   
user_input = int(user_input)
while True:
   if user_input < 3:
      print("Your ticket is free :") 
      break 
   elif user_input >= 3 and user_input <= 12:
      print("Your ticket prize is $10")
      break
   elif user_input > 12:
      print("Your ticket prize is $15")
      break



#Better alternative than this 
while True:
    prompt = "Please enter your age (or type 'exit' to quit): "
    user_input = input(prompt)

    # Allow the user to exit the loop
    if user_input.lower() == 'exit':
        print("Thank you for using the ticket calculator. Goodbye!")
        break

    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid age.")
        continue

    if user_input < 3:
        print("Your ticket is free.")
    elif user_input >= 3 and user_input <= 12:
        print("Your ticket price is $10.")
    elif user_input > 12:
        print("Your ticket price is $15.")


#Solution
#Creating an infinite running loop
x = 1
while x > 0:
    print("HACK The Hox")
    



#                                                                       Using a while loop with lists and dictionaries




# List of unconfirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
# Empty list for confirmed users
confirmed_users = []

# Verify users until there are no unconfirmed users left
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # Remove the last user from the unconfirmed list
    print("Verifying user: " + current_user.title())  # Simulate verification
    confirmed_users.append(current_user)  # Add the verified user to the confirmed list

# Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#     Explanation:
# Initialization: Start with a list of unconfirmed users and an empty list for confirmed users.
# While Loop: Continue verifying users until the unconfirmed list is empty.
# Use pop() to remove the last user from the unconfirmed list.
# Print a verification message.
# Append the verified user to the confirmed list.
# Display: After all users are verified, print the list of confirmed users.
# Output:
# The output will show the verification process and the final list of confirmed users.





 #                                                               Removing All Instances of Specific Values from a List
                


#Here's a simplified version of the code that removes all instances of a specific value ('cat') from a list of pets using a while loop:


#List of pets with multiple instances of 'cat'
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("Original list:", pets)

# Remove all instances of 'cat'
while 'cat' in pets:
    pets.remove('cat')

# Print the updated list
print("Updated list:", pets)




# Explanation:
# Initialization: Start with a list of pets that includes multiple 'cat' entries.
# While Loop: Continue removing 'cat' from the list as long as it exists in the list.
# Output: Print the original list and the updated list after all instances of 'cat' have been removed.


# Output
# Original list: ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# Updated list: ['dog', 'dog', 'goldfish', 'rabbit']


 



 #                                                                      Filling a Dictionary with User Input



#  Can empty dictionary to store responses
responses = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and their mountain choice
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary

    responses[name] = response
    print(responses)
    
    # Ask if another person wants to respond
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Display the poll results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")




# Explanation:
# Initialization: An empty dictionary (responses) is created to store user responses, and a flag (polling_active) is set to keep the loop running.
# While Loop: The loop continues to prompt users for their name and mountain choice until they choose to stop.
# User input is stored in the responses dictionary.
# After each entry, the user is asked if they want to allow another response.
# Output: Once polling is complete, the program prints the results, showing each participant's name and their chosen mountain.



# What is your name? Eric
# Which mountain would you like to climb someday? Denali
# Would you like to let another person respond? (yes/ no) yes
# What is your name? Lynn
# Which mountain would you like to climb someday? Devil's Thumb
# Would you like to let another person respond? (yes/ no) no

# --- Poll Results ---
# Eric would like to climb Denali.
# Lynn would like to climb Devil's Thumb.





#                                                                             Try it Yourself



#  7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari
# ous sandwiches . Then make an empty list called finished_sandwiches . Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches . After all the sandwiches have been made, print a 
# message listing each sandwich that was made .
#  in finished_sandwiches .
#  7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times . Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up 
# 7-10. Dream Vacation: Write a program that polls users about their dream 
# vacation . Write a prompt similar to If you could visit one place in the world, 
# where would you go? Include a block of code that prints the results of the poll 



# Solutin1
sandwiches = [
    "Turkey and Swiss",
    "Ham and Cheese",
    "pastrami ",
    "Veggie Delight",
    "BLT (Bacon, Lettuce, Tomato)",
    "Club Sandwich",
    "Grilled Cheese",
    "Peanut Butter and Jelly",
    "pastrami ",
    "Roast Beef and Cheddar",
    "Caprese Sandwich",
    "pastrami",
    "Egg Salad Sandwich",
]

finished_sandwiches  = []

while sandwiches:
    print("\nFinishing Sandwiches ............ ")
    sandwich = sandwiches.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nYour all these sandwiches are finished :")
for finish_sandwich in finished_sandwiches:
    print(finish_sandwich)



#Solution2
sandwiches = [
    "Turkey and Swiss",
    "Ham and Cheese",
    "pastrami",
    "Veggie Delight",
    "BLT (Bacon, Lettuce, Tomato)",
    "Club Sandwich",
    "Grilled Cheese",
    "Peanut Butter and Jelly",
    "pastrami",
    "Roast Beef and Cheddar",
    "Caprese Sandwich",
    "pastrami",
    "Egg Salad Sandwich",
]
print("\nOriginal List :")
for i in sandwiches:
    print(i)
print("Deli was out of pastrami")
while "pastrami" in sandwiches:
    sandwiches.remove("pastrami")
print("\nUpdated_list :")
for i in sandwiches:
    print(i)



# Solution3

user_data = {}
polling_status = True

while polling_status:
    Name = input("Please enter your name :")
    Favourite_place = input("What's your dream location you want to visit :")
    user_data[Name] = Favourite_place
    user_input = input("Would you like to let another person respond (yes/no) :")
    user_input.lower()
    if user_input == "no":
        polling_status = False
    print("\n___________Polling Result ___________")
    print(f"\nHi {Name} your dream place is {Favourite_place} where you want to go one timme in your life\n")



#  Summary

# In this chapter, you learned how to use the input() function to gather user information in your programs, handling both text and numerical input. You explored how to use while loops to keep your programs running based on user input, and you learned various ways to control loop flow using active flags, the break statement, and the continue statement. Additionally, you discovered how to move items between lists, remove all instances of a value from a list, and utilize while loops with dictionaries.
# In the next chapter, you'll learn about functions, which allow you to break your programs into smaller, manageable parts that perform specific tasks. Functions can be reused and stored in separate files, leading to more efficient, maintainable, and troubleshootable code.

































