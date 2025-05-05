

#                                                Chapter 5  If Statements With Harsh Parashar                                                   Conditional Statements in Python


# In Python, conditional statements allow you to execute different actions based on certain conditions. The if statement is a fundamental way to implement this logic.


# Example: Customizing Car Names
# Suppose you have a list of car names, and you want to print each name in a specific format: most names should be in title case, but the name 'bmw' should be printed in uppercase.

# Here's a simple example:
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())  # Print 'bmw' in uppercase
    else:
        print(car.title())  # Print other car names in title case

# Output 
# Audi
# BMW
# Subaru
# Toyota

# Explanation
# The loop iterates through each car in the cars list.
# The if statement checks if the current car is 'bmw'.
# If it is, it prints the car name in uppercase using upper().
# If it is not, it prints the car name in title case using title().
# This example demonstrates how to use conditional tests to customize output based on specific conditions.




#                                                          Conditional Tests

# Understanding Conditional Tests in Python
# At the core of an if statement in Python is something called a conditional test. This is an expression that can be evaluated as either True or False. Python uses these values to decide whether to execute the code inside the if statement.
# How It Works
# If the test is True: Python runs the code that follows the if statement.
# If the test is False: Python skips the code that follows the if statement.
# Checking for Equality
# One common type of conditional test checks if a variable is equal to a specific value.

car = 'bmw'  # Set the variable car to 'bmw'
print(car == 'bmw')  # Check if car is equal to 'bmw'

#OUTPUT 
#True

car = 'audi'  # Set the variable car to 'audi'
print(car == 'bmw')  # Check if car is equal to 'bmw'

# #OUTPUT 
# #False

# # In this case, since car is now 'audi', the test returns False because 'audi' is not equal to 'bmw'.
# # Key Points
# # A single equal sign (=) is used to assign a value to a variable. For example, car = 'audi' means "set the value of car to 'audi'."
# # A double equal sign (==) is used to compare two values. For example, car == 'bmw' means "is the value of car equal to 'bmw'?"
# # This distinction is important because it helps you understand whether you're assigning a value or checking for equality in your code.
# #Most programming languages use equal signs in this way.




#                                            Ignoring Case When Checking for Equality

#Testing for equality is case sensitive in Python. For example, two values with 
#different capitalization are not considered equal

car = "Audi"
print(car == "audi")

# #OUTPUT
# #False



#                                            Case-Insensitive Comparisons in Python


# When comparing strings in Python, case sensitivity can be an issue. If you want to compare values without worrying about whether letters are uppercase or lowercase, you can convert the strings to lowercase (or uppercase) before comparing them.

car = "Audi"
print(car.lower() == "audi")


#OUTPUT 
#True




#                                            Checking for Inequality in Python

# To check if two values are not equal in Python, you can use the inequality operator !=. This operator returns True if the values are different and False if they are the same.
# Example: Pizza Toppings
# Let's say you want to check if a person did not order anchovies as a pizza topping. You can do this with an if statement:

requested_topping = 'mushrooms'  # Store the requested topping
if requested_topping != 'anchovies':  # Check if the topping is not anchovies
    print("Hold the anchovies!")  # Print a message if it's not anchovies

# #OUTPUT 
# #Hold the anchovies!


# Explanation
# In this example, the variable requested_topping is set to 'mushrooms'.
# The if statement checks if requested_topping is not equal to 'anchovies'.
# Since 'mushrooms' is indeed not equal to 'anchovies', the condition evaluates to True, and the message "Hold the anchovies!" is printed.
# Summary
# Using the != operator is useful when you want to ensure that a certain value is not present, making your conditional checks more efficient in certain situations.



#                                                        Numerical Comparisons in Python


# Testing numerical values in Python is simple and can be done using various comparison operators. Here are some common comparisons:
# Equality (==): Checks if two values are equal.
# Inequality (!=): Checks if two values are not equal.
# Less than (<): Checks if one value is less than another.
# Less than or equal to (<=): Checks if one value is less than or equal to another.
# Greater than (>): Checks if one value is greater than another.
# Greater than or equal to (>=): Checks if one value is greater than or equal to



age = 18
# Check if age is equal to 18
print(age == 18)  # Output: True


answer = 17
if answer != 42:  # Check if the answer is not equal to 42
    print("That is not the correct answer. Please try again!")
#OUTPUT : That is not the correct answer. Please try again!



age = 19
print(age < 21)   # Output: True (19 is less than 21)
print(age <= 21)  # Output: True (19 is less than or equal to 21)
print(age > 21)   # Output: False (19 is not greater than 21)
print(age >= 21)  # Output: False (19 is not greater than or equal to 21)




 #                                                         Checking Multiple Conditions in Python


#  In Python, you can check multiple conditions using the keywords and and or.
# Using and to Check Multiple Conditions
# The and keyword allows you to check if both conditions are True. The overall expression evaluates to True only if both conditions pass; if either or both fail, it evaluates to False.
# Example: Checking Ages


age_0 = 22
age_1 = 18
# Check if both ages are 21 or older
print(age_0 >= 21 and age_1 >= 21)  # Output: False


# In this example:
# The first condition (age_0 >= 21) is True.
# The second condition (age_1 >= 21) is False.
# Since both conditions are not True, the overall expression evaluates to False.
# Now, if we change age_1:


age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # Output: True



# Now both conditions are True, so the overall expression evaluates to True.
# Using or to Check Multiple Conditions
# The or keyword allows you to check if at least one of the conditions is True. The overall expression evaluates to True if either condition passes; it only evaluates to False if both conditions fail.
#Example: Checking Ages Again

age_0 = 22
age_1 = 18
# Check if at least one age is 21 or older
print(age_0 >= 21 or age_1 >= 21)  # Output: True

# In this case:
# The first condition is True, so the overall expression evaluates to True.
# Now, if we change age_0:

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)  # Output: False


# Now both conditions are False, so the overall expression evaluates to False.
# Summary
# Use and when you need both conditions to be True.
# Use or when you need at least one condition to be True.
# These logical operators help you create more complex conditional statements in your programs.






#                                                       Checking Whether a Value Is in a List


# In Python, you can check if a specific value exists in a list using the in keyword. This is useful in various scenarios, such as verifying if a username is already taken or checking if a certain item is part of a list.
# Example: Pizza Toppings
# Let's say you have a list of pizza toppings that a customer has requested. You can check if certain toppings are included in that list.


requested_toppings = ['mushrooms', 'onions', 'pineapple']
# Check if 'mushrooms' is in the list
print('mushrooms' in requested_toppings)  # Output: True
# Check if 'pepperoni' is in the list
print('pepperoni' in requested_toppings)  # Output: False


# Explanation
# In the first check, 'mushrooms' in requested_toppings evaluates to True because 'mushrooms' is indeed in the list.
# In the second check, 'pepperoni' in requested_toppings evaluates to False because 'pepperoni' is not in the list.
# Summary
# Using the in keyword allows you to easily determine if a value exists in a list, making your code more efficient and readable.



 #                                                   Checking Whether a Value Is Not in a List


# To check if a specific value does not exist in a list, you can use the not in keyword. This is useful in scenarios where you want to ensure that a certain item is not present before taking action.
# Example: Banned Users
# Suppose you have a list of users who are banned from commenting in a forum. You can check if a user is banned before allowing them to submit a comment.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# Check if the user is not in the banned list
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#OUTPUT : Marie, you can post a response if you wish.


# Explanation
# The condition user not in banned_users checks if 'marie' is not in the list of banned users.
# Since 'marie' is not banned, the message is printed, inviting her to post a response.
# Summary
# Using not in allows you to easily determine if a value is absent from a list, enabling you to control the flow of your program based on that condition.

  

#                                                               Boolean Expressions


# A Boolean expression is a type of conditional test that evaluates to either True or False. Boolean values are commonly used in programming to track specific conditions or states.
game_active = True  # Indicates that the game is currently running
can_edit = False    # Indicates that the user cannot edit content

# Explanation
# In this example, game_active is set to True, meaning the game is running.
# can_edit is set to False, meaning the user does not have permission to edit content.
# Summary
# Boolean values are a simple and efficient way to manage and check the state of various conditions in your program.



#                                                         TRY IT YOURSELF

#  5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test. Your code 
# should look something like this:
#  car = 'subaru'
#  print("Is car == 'subaru'? I predict True.")
#  print(car == 'subaru')
#  print("\nIs car == 'audi'? I predict False.")
#  print(car == 'audi')
#  •	Look closely at your results, and make sure you understand why each line 
# evaluates to True or False.
#  •	Create at least ten tests. Have at least five tests evaluate to True and 
# another five tests evaluate to False.
#  5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to ten. If you want to try more comparisons, write more tests and add 
# them to conditional_tests.py. Have at least one True and one False result for 
# each of the following:
#  •	Tests for equality and inequality with strings
#  •	Tests using the lower() method
#  •	Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
#  •	Tests using the and keyword and the or keyword
#  •	Test whether an item is in a list
#  •	Test whether an item is not in a list


#SOLUTION 
My_real_name = "Harsh"
MyFriends_call_me = "Joker"
MyGF_call_me = "Genius_Husband"
My_relative_call_me = "Scientist"
print(My_real_name == MyFriends_call_me)
print(My_real_name != MyFriends_call_me)
print(My_real_name == MyGF_call_me)
print(My_real_name == "Harsh")
print(My_real_name != MyFriends_call_me)
print(My_real_name == MyFriends_call_me)
print(My_real_name != MyGF_call_me)
print(My_real_name != "Harsh")
print(My_relative_call_me != MyGF_call_me)
print(MyGF_call_me == "Genius_Husband")
My_favourite_food = "Cheese"
My_friend_favourite_food = "Panner"
if My_favourite_food == My_friend_favourite_food:
    print("Both you love the same food :")
if My_favourite_food != My_friend_favourite_food:
    print("Both you have diffreent food preferences :")
mycar = "Audi"
print(mycar.lower() == "Audi")
print(mycar.lower() != "audi")
myage = 19
mybrother_age = 20
if myage == mybrother_age or myage >= mybrother_age:
    print("Your both Prediction,s is wrong  , we are not twins")
if myage <= mybrother_age and mybrother_age >= myage:
    print("You are right my brother is 2 year elder than me")
Blacklistperson = ["David" , "Jesmie" , "Carolina"]
if "David" in Blacklistperson:
    print("Mr David you already are in our Blacklist Person list and we are not able to give you any type of loan")
if "Harsh" not in Blacklistperson:
    print("Mr Harsh you are fully capable to take a loan from our bank Because you can't comes in the category of blacklisted person")




#                                               If Statements in Python


#An if statement allows you to execute a block of code only if a certain condition is true. The basic structure is:
# if condition:
# do something
# If the condition evaluates to True, the code inside the indented block runs. If it evaluates to False, the code is skipped.
# Example: Checking Voting Age
# Here's a simple example that checks if a person is old enough to vote:


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# In this example:
# We set the variable age to 19.
# The if statement checks if age is greater than or equal to 18.
# Since the condition is true, it prints: "You are old enough to vote!"
# If age were less than 18, nothing would be printed.
# If age is 19, both print statements run because the condition is true.
# If age were less than 18, there would be no output at all.
# You can include as many lines as needed in the indented block after the if statement.





#                                                 If-Else Statements in Python


# An if-else statement allows you to execute one block of code if a condition is true and a different block if the condition is false. This is useful when you want to handle two possible outcomes.
# Example: Checking Voting Age with If-Else
# Here's an example that checks if a person is old enough to vote and provides different messages based on their age:


age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# OUTPUT
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!

# If age is 17, the condition age >= 18 is false, so the code in the else block runs.
# This structure ensures that one of the two blocks of code will always execute, depending on the age.





#                                                    If-Elif-Else Chain


# The if-elif-else chain allows you to test multiple conditions in Python. It executes only one block of code: the first one where the condition is true. This is useful for scenarios with more than two possible outcomes.
# Example: Amusement Park Admission Prices
# Consider an amusement park with different admission prices based on age:
# Free for anyone under age 4.
# $25 for ages 4 to 17.
# $40 for ages 18 and older.
# Here’s how you can determine the admission price:

age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# OUTPUT : Your admission cost is $25.

# Explanation:
# The if statement checks if the person is under 4 years old. If true, the price is set to 0.
# The elif checks if the person is under 18. If true, the price is set to 25.
# The else block sets the price to 40 for anyone 18 or older.
# Finally, a single print statement displays the admission cost.
# This approach is efficient and easy to modify, as you only need to change the print statement if you want to update the output message.




#                                                Using Multiple Elif Blocks


# You can add as many elif blocks as needed to handle different conditions. For example, if an amusement park offers a senior discount, you can include an additional check for seniors.

# Example: Amusement Park Admission with Senior Discount
# Let’s say the admission prices are as follows:

# Free for anyone under age 4.
# $25 for ages 4 to 17.
# $40 for ages 18 to 64.
# $20 for seniors aged 65 and older.
# Here’s how you can implement this:

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
# OUTPUT : Your admission cost is $25.


# Explanation:
# The first if checks if the person is under 4 years old (price = $0).
# The first elif checks if the person is between 4 and 17 (price = $25).
# The second elif checks if the person is between 18 and 64 (price = $40).
# The else block applies to anyone 65 or older, setting the price to $20.
# This structure allows you to easily add more conditions as needed!



#                                                     Omitting the Else Block


# In Python, you don’t have to include an else block at the end of an if-elif chain. Sometimes, it’s clearer to use an additional elif statement instead of a general else.
# Example: Admission Prices Without Else
# Let’s say we want to determine admission prices based on age:




age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
# OUTPUT : Your admission cost is $25.


# Explanation:
# Each if and elif checks a specific age range.
# The last elif checks if the person is 65 or older (price = $20).
# By using an elif for the senior discount, the code is clearer than using a general else.
# Why Omit Else?
# The else block catches any condition not covered by the previous tests, which can sometimes include unexpected or invalid data.
# By using a specific elif instead, you ensure that every condition is clearly defined, making your code safer and easier to understand.
# In summary, if you have a specific condition to check, it’s better to use an elif rather than a catch-all else





#                                                   Testing Multiple Conditions


# When you want to check multiple conditions and act on each one that is true, use separate if statements instead of an if-elif-else chain. This way, all relevant conditions will be evaluated.
# Example: Pizzeria Toppings
# Let’s say a customer requests toppings for their pizza:

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")



# OUTPUT : Adding mushrooms.
# Adding extra cheese.
# Finished making your pizza!


# Explanation:
# Each if statement checks for a specific topping.
# All conditions are evaluated, so both mushrooms and extra cheese are added to the pizza.
# Why Not Use If-Elif-Else?
# If you used an if-elif-else chain, only the first true condition would be executed, and the rest would be skipped. For example:


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# OUTPUT : Adding mushrooms.
# Finished making your pizza!


# In this case, only mushrooms would be added, and extra cheese would be missed.
# Summary
# Use an if-elif-else chain when you want only one block of code to run.
# Use separate if statements when you want to check multiple conditions and act on each one that is true.



#                                                    Try It Yourself 



#  5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#  •	Write an if statement to test whether the alien’s color is green. If it is, print 
# a message that the player just earned 5 points.
#  •	Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)
#  5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
# write an if-else chain.
#  •	If the alien’s color is green, print a statement that the player just earned 
# 5 points for shooting the alien.
#  •	If the alien’s color isn’t green, print a statement that the player just earned 
# 10 points.
#  •	Write one version of this program that runs the if block and another that 
# runs the else block.
# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif
# else chain.
#  •	If the alien is green, print a message that the player earned 5 points.
#  •	If the alien is yellow, print a message that the player earned 10 points.
#  •	If the alien is red, print a message that the player earned 15 points.
#  •	Write three versions of this program, making sure each message is printed 
# for the appropriate color alien.
#  5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
# stage of life. Set a value for the variable age, and then:
#  •	If the person is less than 2 years old, print a message that the person is 
# a baby.
#  •	If the person is at least 2 years old but less than 4, print a message that 
# the person is a toddler.
#  •	If the person is at least 4 years old but less than 13, print a message that 
# the person is a kid.
#  •	If the person is at least 13 years old but less than 20, print a message that 
# the person is a teenager.
#  •	If the person is at least 20 years old but less than 65, print a message that 
# the person is an adult.
#  •	If the person is age 65 or older, print a message that the person is an 
# elder.
#  5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list.
#  •	Make a list of your three favorite fruits and call it favorite_fruits.
#  •	Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas


# Solution: 
alien_colour  = "green"
alien_colour  = "yellow"
alien_colour = "red"
if alien_colour == "green":
    print("You earned 5 points for shooting the alien.")
else:
    x = 0

alien_colour = "green"
alien_colour = "yellow"
alien_colour = "red"
if alien_colour == "green":
    print("YOu earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points") 


alien_colour = "green"
alien_colour = "yellow"
alien_colour = "red"
if alien_colour == "green":
    print("You earned 5 points for shooting the alien.")
elif alien_colour != "green":
    print("Player just earned 10 points") 


alien_colour = "green"
if alien_colour == "green":
    print("Thats you earn 5 points")
elif alien_colour == "yellow":
    print("Thats you earn 10 points")
elif alien_colour == "red":
    print("Thats you earned 15 points")


alien_colour = "yellow"
if alien_colour == "green":
    print("Thats you earn 5 points")
elif alien_colour == "yellow":
    print("Thats you earn 10 points")
elif alien_colour == "red":
    print("Thats you earned 15 points")\


alien_colour = "red"
if alien_colour == "green":
    print("Thats you earn 5 points")
elif alien_colour == "yellow":
    print("Thats you earn 10 points")
elif alien_colour == "red":
    print("Thats you earned 15 points")

age = int(input("Please enter your age :"))
if age < 2:
     print("That the person is a baby ")
elif  2 <= age < 4:
     print("That the person is a toddler")
elif  4 <=  age < 13:
     print("That the person is a kid")
elif  13 <= age < 20:
     print("That the person is a teenager")
elif  20 <= age < 65:
     print("That the person is a adult")
elif age <= 65:
     print("That the person is an elder")
Favourite_fruit = ["Apple" , "Orange" , "Banana" , "Mango" , "Grapes"]
if "Apple" in Favourite_fruit:
     print("Apple is available")
if "Orange" in Favourite_fruit:
     print("Orange is available")
if "Banana" in Favourite_fruit:
     print("You really like banana's")
if "Mango" in Favourite_fruit:
     print("Mango is available")
if "Grapes" in Favourite_fruit:
     print("Grapes is available")



#                                                 Using If Statements with Lists


# Combining lists with if statements allows for efficient handling of special values. For example, in a pizzeria, you can manage topping availability using a list and a loop.
# Here's a simple example of how to announce pizza toppings:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# OUTPUT 
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.
# Finished making your pizza!

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are all out of green peppers.")
    else:
        print(f"Adding {requested_topping}.")
print("Finishing making your pizza")

# This code checks each topping and informs the customer if a requested topping is unavailable, ensuring all other toppings are still added.



#                                                  Checking That a List Is Not Empty


#  When working with lists, it's important to check if a list is empty before running a loop, especially when user input is involved. Here's how to handle an empty list of requested pizza toppings: 

# Explanation:
# If requested_toppings contains items, the loop adds each topping to the pizza.
# If the list is empty, it prompts the user to confirm if they want a plain pizza.

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# OUTPUT : Are you sure you want a plain pizza?
# If the list had toppings, it would list each one being added to the pizza.



#                                                   Using Multiple Lists for Pizza Toppings



# To handle unusual pizza topping requests, you can use two lists: one for available toppings and another for requested toppings. This way, you can check if a requested topping is valid before adding it to the pizza.
# Here's how to implement this:

# Define the lists:

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# Check requested toppings against available toppings:

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")


# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.
# Finished making your pizza!


# Summary:
# This approach effectively manages topping requests by checking each one against a list of available options, providing clear feedback for unavailable toppings.



#                                                           Try it yourSelf

#  5-8. Hello Admin: Make a list of five or more usernames, including the name 
# 'admin'. Imagine you are writing code that will print a greeting to each user 
# after they log in to a website. Loop through the list, and print a greeting to 
# each user:
#  •	If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
#  •	Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
# logging in again.
#  5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty.
#  •	If the list is empty, print the message We need to find some users!
#  •	Remove all of the usernames from your list, and make sure the correct 
# message is printed



# Solution : 
username = []
if username:
  for name in username:
      if name ==  "admin":
          print("Hello admin would you like to see a status report")
      else:
          print(f"Hello {name} , thankyou for logging again")   
else:
    print("We need to find some users!")



# Question  5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
#  •	Make a list of five or more usernames called current_users.
#  •	Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
#  •	Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
#  •	Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.)



#Solution : 
id = input("Please enter a username for your new account :")
new_user = []
new_user.append(id)
current_users = ["Admin" , "Carolin" , "Jesmie" , "Kimsa" , "Shioka" , "Harsh"]
for name in new_user:
    names = name.title()
    if names in current_users:
        print("Sorry this username is already taken please try another one :")
    if names not in current_users:
        print("The new username is available")




# Question  5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#  •	Store the numbers 1 through 9 in a list.
#  •	Loop through the list.
#  •	Use an if-elif-else chain inside the loop to print the proper ordinal end
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
# 7th 8th 9th", and each result should be on a separate line.


#Solution
number = int(input("please enter a number :")) 
list = [1,2,3,4,5,6,7,8,9]
if number in list:
    if number == 1:
      print("1st")
    elif number == 2:
      print("2nd")
    elif number == 3:
      print("3rd")
    else:
      print(f"{number}th")
elif number not in list:
         print("This number not present in the number list")





#                                                              Styling Your if Statements

# PEP 8 recommends using a single space around comparison operators (e.g., ==, >=, <=) for better readability. For example:


# if age < 4:

# if age<4:
# This spacing improves code readability without affecting how Python interprets it.



#                                                                      SUMMARY


# In this chapter, you learned to write conditional tests that evaluate to True or False, including simple if statements, if-else chains, and if-elif-else chains. You practiced handling specific items in a list differently while using for loops and followed Python's style recommendations for readability.

# In Chapter 6, you'll explore Python's dictionaries, which allow you to connect pieces of information. You'll learn to build and loop through dictionaries, and use them with lists and if statements, enabling you to model a wider range of real-world situations.



#Congratulation you  successfully complete this chapter.



















