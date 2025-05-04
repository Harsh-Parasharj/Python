# Chapter 1: Python Basics - Variables and Data Types
# With Harsh Parashar

# -----------------------------
# Introduction to Variables
# -----------------------------
# A variable stores data in memory for later use.
# Variables can store different data types like strings, integers, floats, etc.

# String data type example
greeting = "Hello world"
print(greeting)  # Output: Hello world

name = "Kin"
print(name)  # Output: Kin

full_name = "Harsh Parashar"

# -----------------------------
# String Formatting with f-Strings (Python 3.6+)
# -----------------------------
# f-Strings allow embedding expressions inside string literals
print(f"Hello {full_name.title()}, would you like to learn Python today?")
# Output: Hello Harsh Parashar, would you like to learn Python today?

# -----------------------------
# String Methods
# -----------------------------
# .title() capitalizes the first letter of each word
print(full_name.title())  # Output: Harsh Parashar

# .upper() converts the entire string to uppercase
print(full_name.upper())  # Output: HARSH PARASHAR

# .lower() converts the entire string to lowercase
print(full_name.lower())  # Output: harsh parashar

# -----------------------------
# Printing Quotes
# -----------------------------
quote = "Elon Musk once said, 'Nothing is impossible.'"
print(quote)
# Output: Elon Musk once said, 'Nothing is impossible.'

# -----------------------------
# Removing Whitespace from Strings
# -----------------------------
# Whitespace is often an issue when working with user input

# .lstrip() removes leading spaces
print(" python".lstrip())  # Output: python

# .rstrip() removes trailing spaces
print("python  ".rstrip())  # Output: python

# .strip() removes both leading and trailing spaces
print(" python  ".strip())  # Output: python

# -----------------------------
# Numeric Data Types
# -----------------------------
# Using underscores for better readability in large numbers
universe_age = 14_5322_888483_98
print(universe_age)  # Output: 14532288848398

# Integer (int) and Floating-point (float) Examples
print(5 + 3)     # Output: 8         (Addition - int)
print(3 / 9)     # Output: 0.333...  (Division - float)
print(7 - 5)     # Output: 2         (Subtraction - int)
print(8 * 9)     # Output: 72        (Multiplication - int)

# -----------------------------
# Favorite Number Example
# -----------------------------
favorite_number = 87
print(f"My favorite number is {favorite_number}.")
# Output: My favorite number is 87.

# -----------------------------
# The Zen of Python (Easter Egg)
# -----------------------------
import this
# Output will be:
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# ...
# (These are the guiding principles of Python)

# -----------------------------
# Summary of Chapter
# -----------------------------
# - Variables store values of different data types (string, int, float)
# - f-Strings format output with variable content
# - String methods like title(), upper(), lower() help format text
# - strip(), lstrip(), rstrip() remove unwanted whitespace
# - You performed basic arithmetic operations
# - Underscores in numbers improve readability
# - You explored Python’s philosophy using `import this`
