# Chapter 3: Working with Lists (by Harsh Parashar)

# ===================== Introduction =====================
"""
In our previous chapter we worked with lists. Now in this chapter we will apply 
some basic operations on these lists.

Lists are one of Python's most versatile data structures, allowing you to store 
and manipulate collections of items efficiently.
"""

# ===================== 1. Looping Through Lists =====================
print("\n=== 1. Looping Through Lists ===\n")

"""
Looping Through an Entire List:
You'll often want to run through all entries in a list, performing the same task 
with each item. For example, in a game you might want to move every element on 
the screen by the same amount, or in a list of numbers you might want to perform 
the same statistical operation on every element.

Let's use a for loop to print each name in a list of magicians:
"""

Magicians = ["Carley", "Hamilton", "Wshy", "Sophia", "Jesmie"]
x = 0
for magician in Magicians:
    x += 1
    print(f"The name of the {x} magician is {magician}")

"""
OUTPUT:
The name of the 1 magician is Carley
The name of the 2 magician is Hamilton
The name of the 3 magician is Wshy
The name of the 4 magician is Sophia
The name of the 5 magician is Jesmie

Explanation:
The concept of looping is important because it's one of the most common ways a 
computer automates repetitive tasks. Python manages the iteration internally, 
handling each item in the list one by one.
"""

# ===================== 2. Doing More in Loops =====================
print("\n=== 2. Doing More in Loops ===\n")

"""
Let's do more work within a for loop. Let's print a unique message for each 
magician showing their speciality:
"""

Behaviour_of_all_magician = ["Good", "Excelent", "bad", "Rude", "Aquard"]
x = 0
for magician in Magicians:
    print(f"The behavior of {magician} is {Behaviour_of_all_magician[x]}")
    x += 1

"""
OUTPUT:
The behavior of Carley is Good
The behavior of Hamilton is Excelent
The behavior of Wshy is bad
The behavior of Sophia is Rude
The behavior of Jesmie is Aquard

Explanation:
Here we're using two lists in parallel - one with magician names and one with 
their behaviors. The index variable x helps us match each magician with their 
corresponding behavior.
"""

# ===================== 3. Avoiding Indentation Errors =====================
print("\n=== 3. Avoiding Indentation Errors ===\n")

"""
In Python, indentation is crucial for defining the structure of your code, 
especially in loops. Common errors include:

1. Forgetting to indent after a for statement
2. Forgetting to indent additional lines
3. Unnecessary indentation
4. Forgetting the colon

Example of incorrect indentation:
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
print(magician)  # This will cause an IndentationError

Correct version:
"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician)  # Properly indented

"""
OUTPUT:
alice
david
carolina

Explanation:
Python uses indentation to determine which lines belong to loops or conditionals.
Always indent the code block that should be repeated in the loop.
"""

# ===================== 4. Numerical Lists =====================
print("\n=== 4. Numerical Lists ===\n")

"""
Using range() to Make a List of Numbers:
The range() function generates a sequence of numbers. When wrapped with list(), 
it creates a numerical list.
"""

numbers = list(range(1, 6))
print("Numbers 1-5:", numbers)

"""
You can specify a step size as the third argument to skip numbers:
"""
even_numbers = list(range(0, 11, 2))
print("Even numbers 0-10:", even_numbers)

"""
Simple Statistics with Lists:
Python provides built-in functions for numerical lists:
"""
scores = [85, 90, 78, 92, 88]
print("Min:", min(scores), "Max:", max(scores), "Sum:", sum(scores))

"""
List Comprehensions:
A concise way to generate lists:
"""
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

"""
OUTPUT:
Numbers 1-5: [1, 2, 3, 4, 5]
Even numbers 0-10: [0, 2, 4, 6, 8, 10]
Min: 78 Max: 92 Sum: 433
Squares: [1, 4, 9, 16, 25]

Explanation:
List comprehensions combine the loop and list creation into one line, making 
your code more Pythonic and readable.
"""

# ===================== 5. List Slicing =====================
print("\n=== 5. List Slicing ===\n")

"""
Working with Part of a List (Slicing):
Slicing lets you work with a specific subset of a list by specifying start and 
end indices.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Original list:", players)
print("First three:", players[:3])
print("Middle three:", players[1:4])
print("Last three:", players[-3:])

"""
OUTPUT:
Original list: ['charles', 'martina', 'michael', 'florence', 'eli']
First three: ['charles', 'martina', 'michael']
Middle three: ['martina', 'michael', 'florence']
Last three: ['michael', 'florence', 'eli']

Explanation:
Slicing syntax is list[start:end], where start is inclusive and end is exclusive.
Omitting start defaults to 0, omitting end defaults to the list length.
Negative indices count from the end of the list.
"""

# ===================== 6. Copying Lists =====================
print("\n=== 6. Copying Lists ===\n")
"""
Copying a List:
To create a true copy of a list (not just a reference), use slicing:
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Creates a new copy

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My foods:", my_foods)
print("Friend's foods:", friend_foods)

"""
OUTPUT:
My foods: ['pizza', 'falafel', 'carrot cake', 'cannoli']
Friend's foods: ['pizza', 'falafel', 'carrot cake', 'ice cream']

Explanation:
If you simply assign with = (friend_foods = my_foods), both variables reference 
the same list in memory. Using slicing creates a new independent copy.
"""

# ===================== 7. Tuples =====================
print("\n=== 7. Tuples ===\n")

"""
Tuples are similar to lists but are immutable (cannot be changed after creation).
They're defined using parentheses instead of square brackets.
"""

dimensions = (200, 50)
print("Original dimensions:", dimensions)

"""
Attempting to change a tuple raises an error:
# dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment

However, you can reassign the entire tuple:
"""
dimensions = (400, 100)
print("Modified dimensions:", dimensions)

"""
OUTPUT:
Original dimensions: (200, 50)
Modified dimensions: (400, 100)

Explanation:
Tuples are useful when you want to ensure data integrity - the values cannot be 
changed accidentally after creation.
"""

# ===================== 8. Exercises Solutions =====================
print("\n=== 8. Exercises Solutions ===\n")

# Exercise 4-1: Pizzas
print("\nExercise 4-1: Pizzas")
pizzas = ["Cheese pizza", "Periponni pizza", "Onion pizza"]
print("Pizza available in our Restaurant:")
for pizza in pizzas:
    if pizza == "Cheese pizza":
        print("Cheese pizza is very creamy pizza......")
    elif pizza == "Periponni pizza":
        print("Periponni pizza is a very spicy pizza")
    elif pizza == "Onion pizza":
        print("Onion pizza is very sweet pizza......")
print("I really love pizza!")

"""
OUTPUT:
Cheese pizza is very creamy pizza......
Periponni pizza is a very spicy pizza
Onion pizza is very sweet pizza......
I really love pizza!
"""

# Exercise 4-10: Slices
print("\nExercise 4-10: Slices")
numbers = list(range(1, 21))
print("The first three items in the list are:", numbers[:3])
print("Three items from the middle of the list are:", numbers[9:12])
print("The last three items in the list are:", numbers[-3:])

"""
OUTPUT:
The first three items in the list are: [1, 2, 3]
Three items from the middle of the list are: [10, 11, 12]
The last three items in the list are: [18, 19, 20]
"""

# ===================== 9. PEP 8 Guidelines =====================
print("\n=== 9. PEP 8 Guidelines ===\n")

"""
Styling Your Code:
Python's style guide (PEP 8) recommends:
1. Use 4 spaces per indentation level
2. Limit lines to 79 characters
3. Use blank lines to separate functions/classes
4. Use spaces around operators
5. Use descriptive variable names
6. Put imports at the top of the file

Following these guidelines makes your code more readable and professional.
"""

# ===================== 10. Chapter Summary =====================
print("\n=== 10. Chapter Summary ===\n")

"""
In this chapter we covered:
- List iteration with for loops
- Numerical lists and list comprehensions
- List slicing and copying
- Immutable tuples
- PEP 8 style guidelines
- Practical exercises with solutions

Key Takeaways:
1. Lists are versatile and powerful data structures
2. Proper indentation is crucial in Python
3. List comprehensions offer concise list creation
4. Slicing provides flexible access to list subsets
5. Tuples protect data from accidental modification

If you are reading this line, means you successfully completed this chapter!
"""