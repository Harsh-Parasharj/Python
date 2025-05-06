








#                                        TestIng your Code  With Harsh Parashar




# In this chapter, you'll learn how to test your code using Python's unittest module. Testing ensures your code works correctly with various inputs and helps catch mistakes before users encounter them. You'll discover how to create test cases, check expected outputs, and understand the difference between passing and failing tests. This process will help you improve your code and determine how many tests to write for your projects.





#                                                            Testing a function



# To test our code, we start with a function that formats a full name from a first and last name:


# name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

print(get_formatted_name("harsh" , "ritkk"))

# We also have a program that allows users to input names and see the formatted output:



# names.py
from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')



# Example output:

# Enter 'q' at any time to quit.
# Please give me a first name: janis
# Please give me a last name: joplin
# Neatly formatted name: Janis Joplin.



# test_name_function.py
import unittest
from name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('bob', 'dylan')
        self.assertEqual(formatted_name, 'Bob Dylan')
if __name__ == '__main__':
    unittest.main()
 


# This way, we can confidently modify our function without breaking existing functionality.



#                                                              Unit Tests and Test Cases



# The unittest module in Python provides tools for testing your code. A unit test checks a specific aspect of a function's behavior, while a test case is a collection of unit tests that together ensure the function works correctly across various situations. A good test case covers all possible inputs the function might receive. While achieving full coverage can be challenging, it's often sufficient to test the critical behaviors of your code, aiming for full coverage only if the project gains widespread use.





#                                                                A Passing Test



# To set up a test case using Python's unittest module, you need to import the module and the function you want to test. Create a class that inherits from unittest.TestCase and define methods to test different aspects of the function.

# Here’s an example of a test case for the get_formatted_name() function:




# test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()


# In this example:

# We import unittest and the function to test.
# We create a class NamesTestCase that contains a method test_first_last_name() to check if the function formats names correctly.
# The method uses assertEqual() to compare the expected output with the actual output.
# Running unittest.main() executes the tests.
# When you run the test, you'll see output indicating whether the test passed. If it does, you can be confident that get_formatted_name() works for names with a first and last name. You can rerun the test after modifying the function to ensure it still behaves correctly.



#                                                                    A Failing Test



# A failing test occurs when the code does not behave as expected. For example, if we modify the get_formatted_name() function to require a middle name, like this:




# name_function.py
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()



# This change breaks the function for names with just a first and last name. When we run the test case in test_name_function.py, we get the following output:


# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_name_function.py", line 8, in test_first_last_name
#     formatted_name = get_formatted_name('janis', 'joplin') 
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'



# The output indicates:

# An error occurred in the test_first_last_name() method.
# The error message shows that the function call is missing a required argument.
# It also states that one unit test was run and that the test case failed.
# This information helps identify which test failed and why, making it easier to debug the issue.





#                                                                       Responding to a Failed Test




# When a test fails, the appropriate response is to fix the code that caused the failure rather than changing the test itself. A passing test indicates that the function behaves correctly, while a failing test signals an error in the code.
# For example, if a function get_formatted_name() was modified to require a middle name, it could break existing functionality for names that do not include a middle name. To resolve this, we can make the middle name parameter optional by moving it to the end of the parameter list and providing a default value (e.g., an empty string).
# Here’s a simplified version of the function:


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()



# With this change, the function can handle both names with and without a middle name. After modifying the function, we can run the tests again. If they pass, it confirms that the function now works correctly for all cases, including names like "Janis Joplin." This process illustrates how failed tests can guide us in identifying and fixing issues in our code efficiently






#                                                                          Adding New Tests


# Now that the get_formatted_name() function works for simple names, we can add a second test to check its functionality with middle names. We do this by creating a new method in the NamesTestCase class:



import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()



# Key Points:
# The new method test_first_last_middle_name() checks if the function correctly formats names with a middle name.
# Method names must start with test_ to run automatically during testing.
# Descriptive method names help identify which functionality is being tested, making it easier to understand test failures.
# After adding the new test, running test_name_function.py confirms that both tests pass, ensuring the function works for both simple and complex names.
# This approach gives us confidence that get_formatted_name() handles various name formats correctly.






#                                                                         Try It yourself


#  11-1. City, Country: Write a function that accepts two parameters: a city name 
# and a country name . The function should return a single string of the form 
# City, Country, such as Santiago, Chile . Store the function in a module called 
# city_functions.py .
#  Create a file called test_cities.py that tests the function you just wrote 
# (remember that you need to import unittest and the function you want to test) . 
# Write a method called test_city_country() to verify that calling your function 
# with values such as 'santiago' and 'chile' results in the correct string . Run 
# test_cities.py, and make sure test_city_country() passes .
#  11-2. Population: Modify your function so it requires a third parameter, 
# population . It should now return a single string of the form City, Country –  
# population xxx, such as Santiago, Chile – population 5000000 . Run 
# test_cities.py again . Make sure test_city_country() fails this time .
#  Modify the function so the population parameter is optional . Run 
# test_cities.py again, and make sure test_city_country() passes again .
#  Write a second test called test_city_country_population() that veri
# f
#  ies you can call your function with the values 'santiago', 'chile', and 
# 'population=5000000' . Run test_cities.py again, and make sure this new test 
# passes 

#Solution1
import unittest
from cityfunction import city
class testcase(unittest.TestCase):
    def test_city(self):
        print("Hello")
        city_property = city("Delhi" , "India")
        self.assertEqual(city_property , f"Delhi, India")

if __name__ == "__main__":
    unittest.main()


#Solution2
import unittest
from cityfunction import city
class Test_city(unittest.TestCase):
    def test_city(self):
        format = city("Delhi" , "India" )
        print(format)
        self.assertEqual(format , f"Delhi, India - population " )


if __name__  == "__main__":
    unittest.main()





#                                                                                    Testing a Class


# In this chapter, you'll learn how to write tests for a class, which is important because you'll often use classes in your programs. Having tests that pass for a class gives you confidence that any improvements you make won't unintentionally break its existing functionality.


#  A Variety of Assert Methods


# Python provides a number of assert methods in the unittest.TestCase class. 
# As mentioned earlier, assert methods test whether a condition you believe is 
# true at a specific point in your code is indeed true. If the condition is true 
# as expected, your assumption about how that part of your program behaves 
# is confirmed; you can be confident that no errors exist. If the condition you 
# assume is true is actually not true, Python raises an exception.
# Table 11-1 describes six commonly used assert methods. With these 
# methods you can verify that returned values equal or don’t equal expected 
# values, that values are True or False, and that values are in or not in a given 
# list. You can use these methods only in a class that inherits from unittest 
# TestCase, so let’s look at how we can use one of these methods in the con

# text of testing an actual class.
#  Table 11-1: Assert Methods Available from the unittest Module
#  Method
#  Use
#  assertEqual(a, b)
#  assertNotEqual(a, b)
#  assertTrue(x)
#  assertFalse(x)
#  assertIn(item, list)
#  assertNotIn(item, list)
#  Verify that a == b
#  Verify that a != b
#  Verify that x is True
#  Verify that x is False
#  Verify that item is in list
#  Verify that item is not in list




#                                                                                  A Class to Test


# Certainly! Below is a simplified version of the AnonymousSurvey class along with a program that uses it, followed by a set of unit tests to ensure its functionality remains intact as you make improvements.


# main.py - Using the Class


from survey import AnonymousSurvey

# Define a question and create a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# Show the question and store responses.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()
# test_survey.py - Unit Tests
# Now, let's write some unit tests for the AnonymousSurvey class to ensure it behaves as expected.

import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """Create a survey and a set of responses for use in tests."""
        question = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        """Test that a single response is stored correctly."""
        self.survey.store_response('English')
        self.assertIn('English', self.survey.responses)
    def test_store_multiple_responses(self):
        """Test that multiple responses are stored correctly."""
        for response in self.responses:
            self.survey.store_response(response)
        self.assertEqual(len(self.survey.responses) , 4)
    def test_show_results(self):
        """Test that the results are displayed correctly."""
        for response in self.responses:
            self.survey.store_response(response)
        # Capture the output of show_results
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output  
        self.survey.show_results()     
        sys.stdout = sys.__stdout__  # Reset redirect.
        output = captured_output.getvalue()
        # Check if the output contains the expected responses
        for response in self.responses:
            self.assertIn(response, output)
if __name__ == '__main__':
    unittest.main()






# Summary
# Class Definition: The AnonymousSurvey class allows you to create a survey, store responses, and display results.
# Main Program: The main.py file demonstrates how to use the class to collect survey responses from users.
# Unit Tests: The test_survey.py file contains tests to verify that the class behaves correctly, ensuring that any future changes do not break existing functionality.
# You can run the tests by executing python test_survey.py in your terminal. This setup allows you to confidently make improvements to the AnonymousSurvey class while ensuring its core functionality remains intact.




#                                                                The setUp() Method


# The setUp() method in a unittest.TestCase class allows you to create objects that can be reused across multiple test methods. This reduces redundancy and makes your tests cleaner and easier to maintain. When you run your tests, the setUp() method is called before each test method that starts with test_.



import unittest
from survey import AnonymousSurvey  # Import the AnonymousSurvey class

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)  # Create an instance of AnonymousSurvey
        self.responses = ['English', 'Spanish', 'Mandarin']  # List of sample responses

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])  # Store the first response
        self.assertIn(self.responses[0], self.my_survey.responses)  # Check if it's stored

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)  # Store each response
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)  # Check if all are stored

if __name__ == '__main__':
    unittest.main()  # Run the tests




# Key Points
# setUp() Method: Initializes the survey instance and a list of responses before each test runs.
# Test Methods:
# test_store_single_response(): Tests if a single response can be stored correctly.
# test_store_three_responses(): Tests if multiple responses can be stored correctly.
# Running Tests: The unittest.main() function runs all test methods, providing feedback on their success or failure.
# Benefits of Using setUp()
# Code Reusability: Create objects once and reuse them in multiple tests.
# Cleaner Tests: Each test focuses on its specific functionality without redundant setup code.
# Easier Maintenance: Changes to the setup only need to be made in one place.
# This structure helps ensure that your tests are efficient and easy to understand, making it simpler to expand the functionality of your classes while maintaining test integrity.




#  TrY iT Yourself
#  11-3. Employee: Write a class called Employee. The __init__() method should 
# take in a first name, a last name, and an annual salary, and store each of these 
# as attributes. Write a method called give_raise() that adds $5,000 to the 
# annual salary by default but also accepts a different raise amount.
#  Write a test case for Employee. Write two test methods, test_give_default 
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t 
# have to create a new employee instance in each test method. Run your test 
# case, and make sure both tests pass.


#Solution
# test_employee.py
import unittest
from Employee import Employee  # Make sure Employee.py is in the same directory
class TestEmployee(unittest.TestCase):
    def setUp(self):
        """Create an Employee instance for use in all test methods."""
        self.employee = Employee("John", "Doe", 60000)  # Initial salary of $60,000
    def test_give_default_raise(self):
        """Test the default raise of $5,000."""
        new_salary = self.employee.give_raise()  # Call give_raise() with default
        self.assertEqual(new_salary, 65000)  # Check if the new salary is $65,000
        self.assertEqual(self.employee.annual_salary, 65000)  # Check the employee's salary
    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        new_salary = self.employee.give_raise(3000)  # Call give_raise() with a custom raise
        self.assertEqual(new_salary, 63000)  # Check if the new salary is $63,000
        self.assertEqual(self.employee.annual_salary, 63000)  # Check the employee's salary
if __name__ == "__main__":
    unittest.main()  # Run the tests


#Summary
# In this chapter, you learned how to write tests for functions and classes using the unittest module in Python. Key points include:
# Creating Test Classes: You can create a class that inherits from unittest.TestCase to organize your tests.
# Writing Test Methods: Each test method verifies specific behaviors of your functions and classes.
# Using setUp(): The setUp() method allows you to create instances and attributes that can be reused across multiple test methods, making your tests more efficient.
# Importance of Testing
# Confidence in Code: Testing helps ensure that new changes don’t break existing functionality, allowing you to improve your code with confidence.
# Quick Bug Detection: If a test fails, you can quickly identify and fix the issue, which is easier than responding to user-reported bugs.
# Professionalism: Including tests in your projects makes them more respectable to other programmers, who may be more willing to collaborate or contribute.
# Recommendations
# Start Simple: You don’t need to test every small project as a beginner, but begin testing critical behaviors as your projects grow.
# Experiment with Testing: Familiarize yourself with writing tests, focusing on the most important functionalities without aiming for complete coverage initially.
# By incorporating testing into your development process, you enhance the reliability and maintainability of your code. 



######################################CONGRATULATION CHAMPION YOU COMPLETED OR DO MASTERY IN PYTHON BASICS ########################################


        
