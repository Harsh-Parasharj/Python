




#                                             Ch 10 File and Expections with Harsh Parashar




# Chapter Overview: Enhancing Program Usability
# In this chapter, you will learn how to improve your programs by:

# Working with Files:

# Learn to read and write data to files, allowing your programs to analyze large datasets and save user data for later use.
# Handling Errors:

# Understand how to manage unexpected situations to prevent your programs from crashing.
# Using Exceptions:

# Discover how Python uses exceptions to handle errors that occur during program execution, making your programs more robust.
# Using the JSON Module:

# Learn to save user data in JSON format, ensuring that data is not lost when the program stops running.
# By mastering these skills, your programs will become more user-friendly, allowing users to input data at their convenience and resume work later. You will also enhance the stability of your programs, making them better equipped to handle errors and bad data. Overall, these improvements will make your programs more relevant, usable, and reliable.





#                                                                     Reading from a file

# Working with Text Files
# Text files contain a vast amount of data, including weather, traffic, socioeconomic information, and literary works. Reading from text files is essential for data analysis and allows you to analyze or modify stored information.

# To work with a text file, the first step is to read its contents into memory. You can either read the entire file at once or process it line by line. This capability enables you to format the data for display in applications like web browsers or perform various analyses.





#                                        Reading an Entire File



# Reading from a Text File in Python
# To work with a text file, you first need to create one. For example, you can create a file named pi_digits.txt containing the digits of pi:



# You can either type this into a text editor and save it or download it from the book's resources.

# Example Program: Reading the File
# Here’s a simple program to read and print the contents of pi_digits.txt:


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


# Key Points:

# Opening the File: The open() function is used to access the file. It returns a file object, which is stored in file_object.
# Automatic Closing: The with statement ensures that the file is automatically closed when you're done with it, preventing potential data loss or corruption.
# Reading the File: The read() method reads the entire file and stores it as a single string in contents.
# Printing the Contents: When printed, the output includes an extra blank line at the end because read() returns an empty string when it reaches the end of the file.
# To remove the extra blank line, you can use the rstrip() method:

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())



# This will ensure the output matches the original file exactly, without the extra blank line.





#                                                                            File Paths



# File Paths in Python
# When using the open() function with a simple filename (e.g., pi_digits.txt), Python looks for the file in the same directory as the currently running program. However, if your file is in a different directory, you need to provide a file path.

# Relative File Paths
# A relative file path specifies a location relative to the directory of the running program. For example, if you have a folder structure like this:


# python_work/
#     your_program.py
#     text_files/
#         filename.txt


# You can open the file using:

# On Linux and macOS:

#with open('text_files/filename.txt') as file_object:


# On Windows:

#with open('text_files\\filename.txt') as file_object:



# Absolute File Paths
# An absolute file path specifies the complete path to the file on your system, regardless of where the program is stored. For example:


# On Linux and macOS:

# file_path = '/home/username/other_files/text_files/filename.txt'
# with open(file_path) as file_object:




# On Windows:
# file_path = 'C:\\Users\\username\\other_files\\text_files\\filename.txt'
# with open(file_path) as file_object:
# Using absolute paths allows you to access files from any location on your system. For simplicity, it's often easiest to keep files in the same directory as your program or in a subfolder like text_files.

# Note: Windows may interpret forward slashes in file paths correctly, but if you encounter issues, try using backslashes.





#                                                       Reading Lines from a File in Python


# When reading a file, you may want to examine or modify each line. For example, you might look for specific keywords in weather data or format lines in a news report.

# You can use a for loop to read each line from a file one at a time:



filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)



# File Name: The name of the file is stored in the variable filename, making it easy to change the file later.
# File Object: The open() function creates a file object stored in file_object, and the with statement ensures the file is properly opened and closed.
# When printing each line, you may notice extra blank lines. This happens because each line in the file ends with a newline character, and the print() function adds another newline. To remove the extra blank lines, use rstrip():



filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


#  Now the output matches the contents of the file once again:
#  3.1415926535
#   8979323846
#   2643383279

#This will print each line without the additional blank lines





#                                                         Making a List of Lines from a File


# Retaining File Contents Outside the with Block
# When using the with statement to open a file, the file object is only accessible within that block. If you want to keep access to the file's contents after the block, you can store the lines in a list.


# Here’s how to do it:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # Store lines in a list
    print(lines)

for line in lines:  # Access the list outside the with block
    print(line.rstrip())



# Storing Lines: The readlines() method reads all lines from the file and stores them in the list lines.
# Printing Lines: After the with block, you can use a for loop to print each line from the list, ensuring the output matches the original file without extra blank lines.





#                                                           Working with a File’s Contents



# Building a String from File Data
# After reading a file into memory, you can manipulate the data as needed. Here’s how to create a single string containing all the digits of pi without any whitespace:



filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # Read lines into a list

pi_string = ''  # Initialize an empty string
for line in lines:
    pi_string += line.strip()  # Add each line to the string, removing whitespace

print(pi_string)  # Print the combined string
print(len(pi_string))  # Print the length of the string



# Creating the String: The variable pi_string holds the digits of pi. The strip() method removes any leading or trailing whitespace, including newline characters.
# Output: The resulting string contains pi to 30 decimal places, and its length is 32 characters (including the leading '3' and the decimal point).
# Note
# When reading numbers from a text file, Python treats them as strings. To use them as numbers, you must convert them using int() for integers or float() for floating-point numbers.




#                                                              Large Files: One Million Digits



# Analyzing Pi Digits in Python

# Reading Pi Digits from a File
# You can read a text file containing pi to 1,000,000 decimal places.
# The code below creates a single string from the file's contents and prints the first 50 digits.



filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))



# Checking for Birthdays in Pi
# You can check if a birthday appears in the digits of pi by inputting it as a string



filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")




#Example Input/Output
# Input: 120372
# Output: Your birthday appears in the first million digits of pi!
# Conclusion

# This program demonstrates how to handle large text files in Python and perform string searches efficiently.



#                                                           Try It yourself


#  10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far . Start each line
# with the phrase In Python you can... . Save the file as learning_python.txt in the
# same directory as your exercises from this chapter . Write a program that reads
# the file and prints what you wrote three times . Print the contents once by read
# ing in the entire file, once by looping over the file object, and once by storing
# the lines in a list and then working with them outside the with block .
#  >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word . Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
#  Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C . Print
# each modified line to the screen


# #Solution1
# 1sttime
with open("learning_python.txt") as data:
    content = data.read()
    print(content)


# 2ndtime
with open("learning_python.txt") as data:
    for content in data:
        print(content)


# 3rd time
with open("learning_python.txt") as data:
    content = data.readlines()
file_content = ""
for stri in content:
    file_content += stri.strip()
print(file_content)


message = "I really like dogs"
print(message)
message = message.replace("dogs" , "cat")
print(message)

# Solution2
with open("learning_python.txt") as file:
    content = file.read()
    content = content.replace("python" , "C")
    print(content)





# # #                                                            Writing to a file




# Writing Data to Files in Python
# Overview Writing data to a file allows you to save output for later use, share it, and read it back into your program.

# Writing to a File
# To write text to a file, use the open() function with the mode set to 'w' (write mode).
# If the file does not exist, Python will create it. If it does exist, the file will be erased before writing.
# Example: Writing a Simple Message



filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")



# This creates a file named programming.txt containing:
#Output
#I love programming.




# Note: Python can only write strings to a text file. Convert numbers to strings using str() if needed.

# Writing Multiple Lines
# The write() function does not automatically add newlines. To write multiple lines, include \n for new lines.
# Example: Writing Multiple Lines



with open (filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")



# This results in:
# I love programming.
# I love creating new games.


# Appending to a File
# To add content without erasing existing data, open the file in append mode using 'a'.
# Example: Appending New Content


with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


# The file now contains:

# I love programming.
# I love creating new games.
# I also love finding meaning in large datasets.
# I love creating apps that can run in a browser.



# Summary
# Use 'w' to write (overwrites existing content) and 'a' to append (adds to existing content).
# Include \n for new lines when writing multiple lines.





#                                                                    Try It yourself


#  10-3. Guest: Write a program that prompts the user for their name . When they
# respond, write their name to a file called guest.txt .
#  10-4. Guest Book: Write a while loop that prompts users for their name . When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt . Make sure each entry appears on a
# new line in the file .
#  10-5. Programming Poll: Write a while loop that asks people why they like
# programming . Each time someone enters a reason, add their reason to a file
# that stores all the responses


#Solution1
name = input("Plese enter your name :")
with open("guest.txt" , "w") as file:
    file.write(name)

#Solution2
# while True:
#     name = input("Enter your name :")
#     print(f"Thankyou {name} your name is added to the guest book list ")
#     with open("guest_book.txt" , "a") as file:
#         file.write(name + "\n")

# while True:
#     Why_you_like_coding = input("Tell one reason why you like coding")
#     with open("programming_pole" , "a") as file:
#         file.write(Why_you_like_coding + "\n")
# print("Hello world")











#                                                                             Exceptions


# Handling Exceptions in Python
# Overview Python uses exceptions to manage errors that occur during program execution. When an error arises, Python creates an exception object. If the exception is not handled, the program stops and displays a traceback. However, you can use try-except blocks to handle exceptions gracefully, allowing the program to continue running.

# What is a Try-Except Block?
# A try-except block allows you to write code that may cause an error and specify how to handle that error if it occurs.
# If the code in the try block runs without errors, the except block is skipped. If an error occurs, Python executes the code in the except block.
# Example: Handling ZeroDivisionError
# Attempting to divide by zero raises a ZeroDivisionError.
# Code Example: Without Exception Handling

# This will produce a traceback:
# ZeroDivisionError: division by zero
# Code Example: With Exception Handling

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


try:
    number = input("Please enter a number :")
    operation = number//2
    print(operation)
except TypeError:
    print("You enter a wrong value :")


# You can't divide by zero!

# Benefits of Using Try-Except Blocks
# Users see friendly error messages instead of confusing tracebacks.
# The program continues running after handling the error, allowing for a smoother user experience.
# Summary
# Use try-except blocks to handle potential errors in your code.
# This approach allows you to manage exceptions and keep your program running smoothly, even when errors occur.





#                                                     Using Exceptions to Prevent Crashes


# Handling errors effectively is crucial in programs that require user input, as it prevents crashes and improves user experience. Here's a simplified version of a division calculator that incorporates error handling:



# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)


# Key Points:
# Try-Except Block: Wraps the division operation to catch errors.
# ZeroDivisionError Handling: Provides a user-friendly message if division by zero is attempted.
# Else Block: Executes only if the try block is successful, displaying the result.
# This approach ensures the program continues running smoothly, even with invalid input, enhancing user experience and security.




#                                                          Handling the FileNotFoundError Exception




# When working with files, a common issue is handling missing files. If a file is not found, Python raises a FileNotFoundError. You can manage this situation using a try-except block. Here's a simplified example:



filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")



# Key Points:
# Try Block: Attempts to open and read the file.
# Except Block: Catches the FileNotFoundError and prints a user-friendly message if the file is missing.
# This approach prevents the program from crashing and provides clear feedback to the user when a file cannot be found.





#                                                                   Analyzing Text



# You can analyze public domain texts, such as those from Project Gutenberg, to perform tasks like counting words. Here's a simplified example of how to count the number of words in "Alice in Wonderland" using Python:

# Read the File: Attempt to open and read the text file.
# Count Words: Use the split() method to create a list of words and then count the items in that list.


filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()  # Split the text into words
    num_words = len(words)    # Count the number of words
    print(f"The file '{filename}' has about {num_words} words.")



# Key Points:
# File Handling: The program tries to read the file and handles the case where the file might not exist.
# Word Counting: The split() method divides the text into words, and len() counts them.
# Output: It prints the approximate number of words in the file.
# This method provides a rough estimate of the word count in "Alice in Wonderland," which is useful for text analysis.



#                                                                     Working with Multiple Files


# To analyze multiple books for word counts, we can encapsulate the functionality in a function called count_words(). This makes it easier to process several text files. Here’s a simplified version of the program:



def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' does not exist.")
    else:
        words = contents.split()  # Split the text into words
        num_words = len(words)    # Count the number of words
        print(f"The file '{filename}' has about {num_words} words.")

# List of files to analyze
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

# Analyze each file
for filename in filenames:
    count_words(filename)



# Key Points:
# Function Definition: The count_words() function handles file reading and word counting, including error handling for missing files.
# File List: A list of filenames is created to specify which texts to analyze.
# Loop Through Files: The program iterates through the list, calling count_words() for each file.
# Benefits:
# Error Handling: If a file is missing (like siddhartha.txt), the program prints a friendly message instead of crashing, allowing it to continue analyzing the other files.
# Modularity: Encapsulating the logic in a function makes the code cleaner and reusable for any number of text files.





#                                                                     Failing Silently


# In some cases, you may want your program to handle exceptions silently, without notifying users about missing files. You can achieve this by using the pass statement in the except block. Here’s how to modify the count_words() function to do this:




def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass  # Do nothing if the file is not found
    else:
        words = contents.split()  # Split the text into words
        num_words = len(words)    # Count the number of words
        print(f"The file '{filename}' has about {num_words} words.")

# List of files to analyze
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

# Analyze each file
for filename in filenames:
     count_words(filename)

# Key Points:
# Silent Failure: The pass statement in the except block allows the program to continue without any output if a file is missing.
# Output: Users will only see the word counts for the files that exist, with no indication of any missing files.
# Future Consideration:
# The pass statement can serve as a placeholder for future error handling, such as logging missing filenames to a separate file without interrupting the user experience.






                                                                             Deciding Which Errors to Report



# Error Reporting vs. Silent Failure

# Deciding when to report errors to users and when to fail silently depends on user expectations and the context of the program:

# User Awareness: If users know which texts should be analyzed, they may appreciate being informed about any texts that were not processed. Conversely, if they are unaware of the expected inputs, they might not need to know about unavailable texts.

# Usability: Providing unnecessary information can reduce the usability of your program. It's important to balance the amount of information shared with users when errors occur.

# Error Handling: Python's error-handling structures allow you to control how much information to share with users. The decision on what to report is up to you.

# Code Reliability: Well-written and tested code is less likely to have internal errors. However, external factors like user input, file existence, or network availability can lead to exceptions.

# Experience: With experience, you'll learn where to implement exception handling and how much detail to provide to users regarding errors.

# In summary, consider user expectations and the context when deciding how to handle errors in your program.





#                                                                                          Try it yourself


#  10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers . When you try to convert
# the input to an int, you’ll get a TypeError . Write a program that prompts for
# two numbers . Add them together and print the result . Catch the TypeError if
# either input value is not a number, and print a friendly error message . Test your
# program by entering two numbers and then by entering some text instead of a
# number .
#  (continued)
#  207
#  Files and Exceptions
# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number .
#  10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt . Store at least three
# names of cats in the first file and three names of dogs in the second file . Write
# a program that tries to read these files and print the contents of the file to the
# screen . Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing . Move one of the files to a dif
# ferent location on your system, and make sure the code in the except block
# executes properly .
#  10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing .
#  10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze . Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer .
#  You can use the count() method to find out how many times a word or
# phrase appears in a string . For example, the following code counts the number
# of times 'row' appears in a string:
#  >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
#  3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted .
#  Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text




# Solution1

try:
    first_number =input("Enter first number :")
    second_number = input("Enter second number :")
    first_number = int(first_number)
    second_number = int(second_number)
    sum = first_number + second_number
    print(f"The sum of the {first_number} or {second_number} is {sum}")
except ValueError:
    print(f"Sorry you enter text rather than a number")



# Solution2


# while True:
#     try:
#       first_number =input("Enter first number :")
#       second_number = input("Enter second number :")
#       first_number = int(first_number)
#       second_number = int(second_number)
#       sum = first_number + second_number
#       print(f"The sum of the {first_number} or {second_number} is {sum}")
#     except ValueError:
#        print(f"Sorry you enter text rather than a number")


# Solution 3
def file_reader(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        print("Sorry this file does not exist")
files = ["cats.txt" , "dogs.txt"]
for file in files:
    file_reader(file)



# #Solution4
def file_reader(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        pass #Do nothing if file is missing
files = ["cats.txt" , "dogs.txt"]
for file in files:
    file_reader(file)


# Solution5
def file_reader(file_name):
    try:
        with open(file_name) as file_object:
            content = file_object.read()
            apperance = content.count("kitty")
            print(apperance)
            print(content)
    except FileNotFoundError:
        pass #Do nothing if file is missing
files = ["cats.txt" , "dogs.txt"]
for file in files:
    file_reader(file)



#                                                                        Storing data


# The json module in Python allows you to easily save and load data, such as user preferences, using simple data structures like lists and dictionaries. This makes it easy to store information when a program closes and retrieve it the next time the program runs. JSON (JavaScript Object Notation) is a widely-used format that can be shared across different programming languages, making it a versatile and portable option for data storage.

#                                                 Using json.dump() and json.load()


# Here's a simplified explanation of how to store and retrieve a list of numbers using JSON in Python:
# Storing Numbers: In the first program (number_writer.py), we create a list of numbers and use the json.dump() function to save it to a file called numbers.json. The code looks like this:
# Storing Numbers: In the first program (number_writer.py), we create a list of numbers and use the json.dump() function to save it to a file called numbers.json. The code looks like this:


import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


# This writes the list to the file in JSON format, which looks like this: [2, 3, 5, 7, 11, 13].
# Reading Numbers: In the second program (number_reader.py), we read the list back into memory using json.load(). The code is as follows:


import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)


# This reads the data from numbers.json and prints the list, which will be the same as the original: [2, 3, 5, 7, 11, 13].

# This process allows you to easily share data between two Python programs using JSON.





#                                                              Saving and Reading User-Generated Data


# Storing the User's Name: In the first part of the program (remember_me.py), we prompt the user for their name and store it in a file called username.json using json.dump(). The code looks like this:


import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")


# When the user runs this for the first time, they might see:


#OUTPUT
# What is your name? Eric
# We'll remember you when you come back, Eric!


# Retrieving the User's Name: In the second part, we want to greet the user if their name is already stored. We use json.load() to read the name from username.json:


import json
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")



# If the file exists, it reads the username and welcomes the user back.
# If the file doesn't exist (the first time running), it prompts for the name, stores it, and prints a greeting.
# This combined program ensures that the user's name is remembered across sessions, providing an appropriate greeting each time they run it.





#                                                                       Refactoring


# Refactoring Code for Clarity
# Refactoring is the process of restructuring code to improve its readability and maintainability. In the example of remember_me.py, we can break the code into smaller, focused functions.

# Original Code
# The original code had all logic in a single function, greet_user(), which handled greeting the user, retrieving a stored username, and prompting for a new username.


import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()


#                                                            Refactored Code


# Separate Function for Retrieving Username: We create get_stored_username() to handle retrieving the username from a file.
# Separate Function for New Username: We create get_new_username() to prompt for a new username and save it.



import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    import json
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()


# Benefits of Refactoring:

# Clear Purpose: Each function has a specific task, making the code easier to understand.
# Maintainability: The code is organized, making it easier to modify or extend in the future.
# In summary, refactoring improves code quality by breaking it into smaller, manageable functions, enhancing clarity and maintainability.




#                                                                      Try It yourself


#  10-11. Favorite Number: Write a program that prompts for the user’s favorite 
# number . Use json.dump() to store this number in a file . Write a separate pro
# gram that reads in this value and prints the message, “I know your favorite 
# number! It’s _____ .”
#  10-12. Favorite Number Remembered: Combine the two programs from 
# Exercise 10-11 into one file . If the number is already stored, report the favorite 
# number to the user . If not, prompt for the user’s favorite number and store it in a 
# file . Run the program twice to see that it works .
#  10-13. Verify User: The final listing for remember_me.py assumes either that the 
# user has already entered their username or that the program is running for the 
# first time . We should modify it in case the current user is not the person who 
# last used the program .
#  Before printing a welcome back message in greet_user(), ask the user if 
# this is the correct username . If it’s not, call get_new_username() to get the correct username


#Solution1

def Store_favourite_number():
    import json
    file_name = "Fav_num.json"
    fav_number = int(input("Enter your favourite number  :"))
    with open(file_name , "w") as file_object:
        json.dump(fav_number , file_object)
def identifier():
    import json
    file_name = "Fav_num.json"
    with open(file_name) as fil_object:
        number = json.load(fil_object)
        print(f"I know your favourite number ! It's {number}")
# Store_favourite_number()
# identifier()

#Solution2
import json
def favorite_number():
    file_name = "fav_num.json"
    try:
        # Try to read the favorite number from the file
        with open(file_name) as file_object:
            number = json.load(file_object)
            print(f"I know your favorite number is {number}.")
    except FileNotFoundError:
        # If the file does not exist, prompt for the favorite number
        number = int(input("Enter your favorite number: "))
        with open(file_name, "w") as file_object:
            json.dump(number, file_object)
            print("We'll remember your favorite number next time.")
# Run the function
favorite_number()
import json
filename = "username.json"
with open(filename) as file_object:
     name = json.load(file_object)
     data = input(f"Are you {name} Y/N :")
     i = data.lower()
     if i == 'n':
        name = input("Enter you name :")
        with open(filename , "w") as file_object:
            names = json.dump(name , file_object)     
            print(f"We will remember you {name}")    
     elif i == 'y':       
           filename = 'username.json'
           try:
               with open(filename) as f_obj:
                 username = json.load(f_obj)
           except FileNotFoundError:
              username = input("What is your name? ")
              with open(filename, 'w') as f_obj:
                json.dump(username, f_obj)
              print("We'll remember you when you come back, " + username + "!")
           else: 
               print("Welcome back, " + username + "!")
     else:
        print("Invalid Input")




#Summary :
# In this chapter, you learned how to work with files. You learned to read an 
# entire file at once and read through a file’s contents one line at a time. You 
# learned to write to a file and append text onto the end of a file. You read 
# about exceptions and how to handle the exceptions you’re likely to see in 
# your programs. Finally, you learned how to store Python data structures so 
# you can save information your users provide, preventing them from having 
# to start over each time they run a program.
#  In Chapter 11 you’ll learn efficient ways to test your code. This will help 
# you trust that the code you develop is correct, and it will help you identify 
# bugs that are introduced as you continue to build on the programs you’ve 
# written.


    


