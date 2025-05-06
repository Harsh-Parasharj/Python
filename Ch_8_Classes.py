



#                                            Classes in Python with Harsh Parashar

# Object-oriented programming (OOP) is a powerful approach to software development where you create classes that represent real-world entities and situations. By defining a class, you establish general behaviors that all objects (instances of the class) will share, while also allowing for unique traits for each object.
# Key concepts include:
# Instantiation: Creating an object from a class.
# Attributes and Methods: Specifying what information can be stored in objects and what actions can be performed.
# Inheritance: Extending existing classes to share code efficiently.
# OOP helps programmers think logically and understand the broader concepts behind their code, making collaboration easier and enabling teams to tackle complex challenges effectively.





#                                                     Creating and using a Class


# We can create a class called Dog to represent any dog. This class will include common attributes like name and age, as well as behaviors like sit and roll_over. Once we define the Dog class, we can create individual instances of it, each representing a specific dog.




#                                                      Creating the Dog Class



# To create a Dog class, we define it with attributes for name and age, and methods for sit() and roll_over(). Here's a breakdown:

# Class Definition: class Dog(): defines the class.
# Constructor: The __init__ method initializes the name and age attributes.
# Methods: sit() and roll_over() simulate the dog's actions.
# The class name is capitalized by convention, and the parentheses indicate that it's a new class. A docstring describes the class's purpose. You'll become familiar with this structure as you practice.




# Here's a simplified explanation of the Dog class along with the code:

# The Dog class models a dog with attributes for name and age, and methods for sit() and roll_over().


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")



# Summary:
# Attributes: Each dog instance has a name and age.
# Methods: The sit() method prints a message indicating the dog is sitting, and the roll_over() method prints a message indicating the dog rolled over.



#                                                                        The __init__() Method



# In Python, a method is a function that ___init__() method is a special method that initializes new instances of a class. It automatically runs when you create a new instance of the Dog class.belongs to a class.

# Parameters: The __init__() method has three parameters: self, name, and age.
# Self: Refers to the instance itself and must be the first parameter.
# Attributes: self.name and self.age store the values for each instance.
# The Dog class also includes two methods, sit() and roll_over(), which allow the dog to perform actions.


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# Key Points:
# Attributes: self.name and self.age are accessible throughout the class.
# Methods: sit() and roll_over() print messages indicating the dog's actions.
# Python 2.7: In Python 2.7, you define a class with object in parentheses (e.g., class Dog(object):) to make it behave like Python 3 classes.






#                                                                    Making an Instance from a Class



# A class in Python serves as a blueprint for creating instances. For example, the Dog class provides instructions on how to create specific dog instances.


# Example of Creating an Instance:

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")



# In this example:

# We create an instance called my_dog representing a dog named 'Willie' who is 6 years old. This calls the __init__() method of the Dog class, which sets the name and age attributes.
# The instance is stored in the variable my_dog, following the convention that class names are capitalized (like Dog), while instance names are lowercase (like my_dog).
# Accessing Attributes:
# We use dot notation to access attributes of the instance. For example, my_dog.name retrieves the dog's name, and my_dog.age retrieves the dog's age.
# The output will be

#OUTPUT
# My dog's name is Willie.
# My dog is 6 years old.



# This demonstrates how to create an instance of a class and access its attributes.



#                                                                      Calling Methods


# After creating an instance of the Dog class, you can use dot notation to call any method defined in the class. For example:

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

# When you call my_dog.sit(), Python looks for the sit() method in the Dog class and executes it, resulting in:


#OUTPUT
# Willie is now sitting.
# Willie rolled over!



#                                                                      Creating Multiple Instances



# You can create multiple instances of a class. For example, you can create another dog named Lucy:


your_dog = Dog('lucy', 3)

# Each dog is a separate instance with its own attributes and can perform the same actions:


print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


#OUTPUT
# My dog's name is Willie.
# My dog is 6 years old.
# Willie is now sitting.
# Your dog's name is Lucy.
# Your dog is 3 years old.
# Lucy is now sitting.



# Even if you use the same name and age for different dogs, Python will create separate instances. You can create as many instances as needed, as long as each has a unique variable name or is stored in a unique location (like a list or dictionary).




 #                                                                           Try It yourself


#  9-1. Restaurant: Make a class called Restaurant . The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi
# cating that the restaurant is open .
#  Make an instance called restaurant from your class . Print the two attri
# butes individually, and then call both methods .
#  9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three
# different instances from the class, and call describe_restaurant() for each
# instance .
#  9-3. Users: Make a class called User . Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile . Make a method called describe_user() that prints a summary
# of the user’s information . Make another method called greet_user() that prints
# a personalized greeting to the user .
#  Create several instances representing different users, and call both methods
# for each user




#Solution1
class Restaurent():
    def __init__(self , restaurent_name , cuisine_type):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to our {self.restaurent_name}\n")
        print(f"Our Restaurent have a {self.cuisine_type} cuisine type")

    def open_restaurant(self):
        print("Now the Restaurant is open")

restaurant0 = Restaurent("Strabucks" , "Italian")
restaurant0.describe_restaurant()
restaurant0.open_restaurant()



# Solution2
restaurent1 = Restaurent("Willi_Restaurent" , "Italian")
restaurent1.describe_restaurant()
restaurent2 = Restaurent("Milso_Restaurent" , "American")
restaurent2.describe_restaurant()
restaurent3 = Restaurent("Milsi_Restaurent" , "Chinnesse")
restaurent3.describe_restaurant()



#Solution3
class User():

    def __init__(self , first_name , last_name , Age , Country):
        self.first_name = first_name
        self.last_name = last_name
        self.Age = Age
        self.Country = Country

    def describe_user(self):
        print(f"\nUser Details :\n")
        print(f" Name : {self.first_name} {self.last_name}")
        print(f" Age : {(self.Age)}")
        print(f" Country : {self.Country}\n")


    def greet_user(self):
        print(f"Hi {self.first_name}, I wish you a very good day")

user1 = User("Harsh" , "Parashar" , 19 , "India")
user1.describe_user()
user1.greet_user()
user2 = User("Jesmie" , "Fermandus" , 18 , "Russia")
user2.describe_user()
user2.greet_user()
user3 = User("Akshita" , "Rajput" , 17 , "India")
user3.describe_user()
user3.greet_user()






#                                                               Working with Classes and Instances



# Classes are used to model real-world situations in programming. After creating a class, you'll primarily work with instances (objects) of that class. A common task is to modify the attributes of these instances. You can do this either directly or by using methods designed to update the attributes in specific ways.



# Car Class Overview
# Purpose: The Car class represents a car and stores information about its make, model, and year.

# Initialization:

# The __init__ method initializes the car's attributes: make, model, and year.
# These attributes are set when a new instance of the class is created.
# Descriptive Method:

# The get_descriptive_name method returns a formatted string that combines the car's year, make, and model into a single descriptive name.

# Example Usage:


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

# Creating an instance of Car
my_new_car = Car('audi', 'a4', 2016)
# Printing the descriptive name of the car
print(my_new_car.get_descriptive_name())  # Output: 2016 Audi A4



# Adding Mileage
# To make the class more interesting, you can add an attribute for the car's mileage, which can change over time. This would allow you to track how much the car has been driven.

# Summary
# The Car class encapsulates the properties of a car.
# It provides a method to get a formatted description of the car.
# You can enhance the class by adding attributes that can change, like mileage






#                                                                     Setting a Default Value for an Attribute

# In the Car class, we initialize an attribute called odometer_reading to 0 in the __init__() method. This allows us to track the car's mileage. We also define a method called read_odometer() to display the current mileage. Here's a simplified version of the class:


class Car:
    def __init__(self, make, model, year ,odometer_reading=0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Initial mileage

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make.title()} {self.model.title()}"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

# Example usage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()



# Output:
# 2016 Audi A4
# This car has 0 miles on it.


# This class initializes the car's attributes and provides a method to read the odometer, starting at 0 miles.



#                                                                     Modifying Attribute Values



#  You can change an attribute’s value in three ways: you can change the value
# directly through an instance, set the value through a method, or increment
# the value (add a certain amount to it) through a method. Let’s look at each
# of these approaches.



#                                                               Modifying an attribute’s Value Directly



# To modify an attribute in a class, you can directly access it through an instance using dot notation. For example, in the Car class, you can set the odometer_reading like this:

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  # Directly setting the odometer reading
my_new_car.read_odometer()


#This code sets the odometer_reading of my_new_car to 23. The output will be:

# 2016 Audi A4
# This car has 23 miles on it.

# While direct access is simple, you may also want to create a method to update the attribute, which can help encapsulate the logic for changing the value.





#                                                            Modifying an attribute’s Value through a Method


# To manage the odometer_reading attribute more effectively, you can create a method called update_odometer() in the Car class. This method allows you to update the odometer reading while also enforcing rules to prevent invalid changes, such as rolling back the odometer.

# Here’s a simplified version of the implementation:



class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make.title()} {self.model.title()}"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Example usage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)  # Update to 23 miles
my_new_car.read_odometer()

my_new_car.update_odometer(20)  # Attempt to roll back



#Output:
# 2016 Audi A4
# This car has 23 miles on it.
# You can't roll back an odometer!


# Summary:
# The update_odometer() method updates the odometer_reading if the new mileage is greater than or equal to the current reading.
# If an attempt is made to roll back the odometer, a warning message is displayed. This approach helps maintain the integrity of the odometer reading.



#                                                              Incrementing an attribute’s Value through a Method

# To allow for incrementing the odometer_reading in the Car class, you can add a method called increment_odometer(). This method takes an amount of miles and adds it to the current odometer reading. Here's a simplified version of the implementation:



class Car:
    def __init__(self, make, model, year, odometer_reading=0):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make.title()} {self.model.title()}"

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value, rejecting rollbacks."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:  # Reject negative increments
            self.odometer_reading += miles
        else:
            print("You can't increment by a negative amount!")

# Example usage
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)  # Set initial mileage
my_used_car.read_odometer()

my_used_car.increment_odometer(100)  # Increment mileage by 100
my_used_car.read_odometer()



# Output:
# 2013 Subaru Outback
# This car has 23500 miles on it.
# This car has 23600 miles on it.


# Summary:
# The increment_odometer() method adds a specified number of miles to the current odometer reading.
# It includes a check to reject negative increments, preventing the user from rolling back the odometer.
# While these methods help control how the odometer is updated, direct access to the attribute can still allow changes without restrictions, highlighting the need for careful design in managing data integrity.




#                                                                          Try It yourself



#  9-4. Number Served: Start with your program from Exercise 9-1 (page 166) .
# Add an attribute called number_served with a default value of 0 . Create an
# instance called restaurant from this class . Print the number of customers the
# restaurant has served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number
# of customers that have been served . Call this method with a new number and
# print the value again .
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served . Call this method with any num
# ber you like that could represent how many customers were served in, say, a
# day of business .
#  9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166) . Write a method called increment_
#  login_attempts() that increments the value of login_attempts by 1 . Write
# another method called reset_login_attempts() that resets the value of login_
#  attempts to 0 .
#  Make an instance of the User class and call increment_login_attempts()
# several times . Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts() . Print login_attempts again to
# make sure it was reset to 0




# Solution1
class Restaurent():
    def __init__(self , restaurent_name , cuisine_type ):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to our {self.restaurent_name}\n")
        print(f"Our Restaurent have a {self.cuisine_type} cuisine type")

    def open_restaurant(self):
        print("Now the Restaurant is open")

    def set_number_saved(self , number_of_serves):
        if number_of_serves >= 0:
            self.number_served = number_of_serves
            print(f"Number of serves updated succesfully : {number_of_serves}")
        else:
            print("You can't set number_of_serves in negative")


Restaurent1 = Restaurent('Starbucks' , 'Italian')
Restaurent1.describe_restaurant()
Restaurent1.open_restaurant()
Restaurent1.set_number_saved(54)


#solution2
class User():

    def __init__(self , first_name , last_name , Age , Country , login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.Age = Age
        self.Country = Country

    def describe_user(self):
        print(f"\nUser Details :\n")
        print(f" Name : {self.first_name} {self.last_name}")
        print(f" Age : {(self.Age)}")
        print(f" Country : {self.Country}\n")

    def greet_user(self):
        print(f"Hi {self.first_name}, I wish you a very good day")

    def login_increment(self):
        self.login_attempts += 1
        print(f"Login attempts : {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts : {self.login_attempts}")


user = User("Harsh" , "Parashar" , 13 , "India"  )
user.login_increment()
user.reset_login_attempts()






#                                                                             Inheritance


# When creating a new class that is a specialized version of an existing class, you can use inheritance. The existing class is called the parent class, and the new The child class inherits all class is the child class. the attributes and methods of the parent class but can also add its own unique attributes and methods.




#                                                                    The __init__() Method for a Child Class


# When you create a child class in Python, it inherits attributes and methods from its parent class. To initialize the parent class's attributes, the child class uses the super() function in its __init__() method. This allows the child class to have all the functionality of the parent class while also enabling the addition of specific features for the child class



# Parent class
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

# Create an instance of ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # Output: 2016 Tesla Model S





#                                                                          Inheritance in Python 2.7



#In Python 2.7, when using inheritance, the super() function requires two arguments: a reference to the child class and the self object. This helps Python establish the connection between the parent and child classes. Additionally, the parent class should be defined using the object syntax.



class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        # Additional ElectricCar-specific initialization can go here



#                                                              Defining Attributes and Methods for the Child Class



#Once you have a child class that inherits from a parent class, you can add new attributes and methods to make the child class unique. For example, in the ElectricCar class, you can add a specific attribute for the battery size and a method to describe it.



class Car:
    # Parent class code here
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class and specific to electric cars."""
        super().__init__(make, model, year)
        self.battery_size = 70  # Specific attribute for electric cars

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Create an instance of ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # Output: 2016 Tesla Model S
my_tesla.describe_battery()  # Output: This car has a 70-kWh battery.



# Summary
# In this example, the ElectricCar class adds a battery_size attribute and a describe_battery() method, which are specific to electric cars. You can continue to specialize the ElectricCar class as needed, while general attributes and methods should remain in the Car class to be available to all car instances.




#                                                                Overriding Methods from the Parent Class


# You can override methods from a parent class in a child class by defining a method with the same name in the child class. This allows you to customize or replace functionality that doesn't fit the child class's purpose.

# For example, if the Car class has a method called fill_gas_tank(), you can override it in the ElectricCar class like this:


class ElectricCar(Car):
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

Ele = ElectricCar("Make" , "Model" , "Year")
Ele.fill_gas_tank()
# Now, if you call fill_gas_tank() on an instance of ElectricCar, Python will use the overridden method instead of the one from Car. This way, you can keep the necessary features from the parent class while removing or modifying those that aren't relevant.






#                                                                        Instances as Attributes


#When a class becomes too detailed and lengthy, you can break it into smaller, more manageable classes that work together. For example, if the ElectricCar class has many attributes and methods related to the battery, you can create a separate Battery class to handle those details.



class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Create a Battery instance

# Create an instance of ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # Output: 2016 Tesla Model S
my_tesla.battery.describe_battery()      # Output: This car has a 70-kWh battery.
my_tesla.battery.get_range()              # Output: This car can go approximately 240 miles on a full charge.



# Summary
# In this example, the Battery class handles battery-related attributes and methods, while the ElectricCar class uses an instance of Battery. This separation keeps the code organized and allows for more detailed battery management without cluttering the ElectricCar class.




#                                                                    Modeling Real-World Objects

# As you model complex items like electric cars, you'll face questions about how to organize your code. For example, should the range of an electric car be a property of the battery or the car itself?

# If you're focusing on a single car, it makes sense for the get_range() method to belong to the Battery class. However, if you're considering a whole line of cars, it might be better to move get_range() to the ElectricCar class, where it can report a range specific to that car while still checking the battery size.

# Alternatively, you could keep get_range() in the Battery class but pass the car model as a parameter to provide a range based on both the battery size and the car model.

# These decisions reflect your growth as a programmer, as you're thinking about how to represent real-world situations in code rather than just focusing on syntax. There are often multiple valid approaches, and finding the most efficient one takes practice. It's normal to revise your classes and code multiple times as you refine your design. If your code works as intended, you're on the right track





#                                                                         Try It yourself


#  9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of
# the class will work; just pick the one you like better . Add an attribute called
# flavors that stores a list of ice cream flavors . Write a method that displays
# these flavors . Create an instance of IceCreamStand, and call this method .
#  9-7. Admin: An administrator is a special kind of user . Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on .
# Write a method called show_privileges() that lists the administrator’s set of
# privileges . Create an instance of Admin, and call your method .
#  9-8. Privileges: Write a separate Privileges class . The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7 .
# Move the show_privileges() method to this class . Make a Privileges instance
# as an attribute in the Admin class . Create a new instance of Admin and use your
# method to show its privileges .
#  9-9. Battery Upgrade: Use the final version of electric_car.py from this section .
# Add a method to the Battery class called upgrade_battery() . This method
# should check the battery size and set the capacity to 85 if it isn’t already .
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery . You should
# see an increase in the car’s range



# Solution1

class Restaurent():
    def __init__(self , restaurent_name , cuisine_type ):
        self.restaurent_name = restaurent_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to our {self.restaurent_name}\n")
        print(f"Our Restaurent have a {self.cuisine_type} cuisine type")

    def open_restaurant(self):
        print("Now the Restaurant is open")

    def set_number_saved(self , number_of_serves):
        if number_of_serves >= 0:
            self.number_served = number_of_serves
            print(f"Number of serves updated succesfully : {number_of_serves}")
        else:
            print("You can't set number_of_serves in negative")
class Icerestaurent(Restaurent):
    def __init__(self, restaurent_name, cuisine_type , flavours=[]):
        self.flavours = flavours
        super().__init__(restaurent_name, cuisine_type)

    def show_flavour(self):
        print(f"Available Ice crem flavour :")
        for flavour in self.flavours:
           print(flavour)
Icecreamstand = Icerestaurent("Strabucks" , "Italian" , ["Veniele" , "Strawberyy" , "Creamy" , "Choco"])
Icecreamstand.describe_restaurant()
Icecreamstand.show_flavour()


#Solution2

class User():

    def __init__(self , first_name , last_name , Age , Country , login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.Age = Age
        self.Country = Country

    def describe_user(self):
        print(f"\nUser Details :\n")
        print(f" Name : {self.first_name} {self.last_name}")
        print(f" Age : {(self.Age)}")
        print(f" Country : {self.Country}\n")

    def greet_user(self):
        print(f"Hi {self.first_name}, I wish you a very good day")

    def login_increment(self):
        self.login_attempts += 1
        print(f"Login attempts : {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts : {self.login_attempts}")


class Admin(User):
    def __init__(self, first_name, last_name, Age, Country, login_attempts=0 , privilages=["can add post" , "can del user" , "can ban user"]):
        self.show_privilagas = privilages
        super().__init__(first_name, last_name, Age, Country, login_attempts)

    def show_privilegas(self):
        for privilage in self.show_privilagas:
            print(privilage)
privilages = Admin("Harsh" , "Parashar" , 18 , "India"  )
privilages.show_privilegas()


#Solution3

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
             range = 240
        elif self.battery_size == 85:
             range = 270
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Create a Battery instance

#Create an instance of ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # Output: 2016 Tesla Model S
my_tesla.battery.describe_battery()      # Output: This car has a 70-kWh battery.
my_tesla.battery.get_range()
electric_car = Battery()
electric_car.get_range()
electric_car = Battery(battery_size=85)
electric_car.get_range()






#                                                                      Importing Classes


# To keep your Python files organized and uncluttered, you can store classes in separate modules. This allows you to import only the classes you need into your main program, making your code cleaner and easier to manage.


#                                                                  Importing a Single Class


#To organize your code, create a module named car.py that contains the Car class. This allows you to keep your main program clean. Here’s how to do it:


from car import Car
mynew_car = Car("tesla" , "G90i " , 2018)
print(mynew_car.describe_car())
mynew_car.read_odometer()


#Output
# tesla ,G90i  ,2018
# This car has 45 miles on it




#                              Storing Multiple Classes in a Module




# You can store multiple related classes in a single module. For example, in car.py, you can define the Car, Battery, and ElectricCar classes:



"""A set of classes used to represent gas and electric cars."""


from car import ElectricCar

my_tesla = ElectricCar('Tesla', 'Model S', 2016)
print(my_tesla.describe_car())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



#                                                   Importing Multiple Class from a Module


# You can import multiple classes from a module into a program file by separating them with commas. For example, in my_cars.py, you can import both the Car and ElectricCar classes:


from car import Car, ElectricCar
my_beetle = Car('Volkswagen', 'Beetle', 2016)
print(my_beetle.describe_car())
my_tesla = ElectricCar('Tesla', 'Roadster', 2016)
print(my_tesla.describe_car())




#                                                      Importing an Entire Module



# You can import an entire module and access its classes using dot notation, which makes your code clear and avoids naming conflicts. For example, in my_cars.py, you can import the car module and create instances of Car and ElectricCar like this:




import car
my_beetle = car.Car('Volkswagen', 'Beetle', 2016)
print(my_beetle.describe_car())
my_tesla = car.ElectricCar('Tesla', 'Roadster', 2016)
print(my_tesla.describe_car())

#This way, you create a Volkswagen Beetle and a Tesla Roadster while keeping the code easy to read.



#                                                   Importing All Classes from a Module


# Using from module_name import * to import all classes from a module is not recommended for two main reasons:
# Clarity: It makes it difficult to see which classes are being used in the program, as the import statements do not specify them clearly.
# Naming Conflicts: It can lead to errors if there are classes with the same name in your program, making it hard to diagnose issues.
# A better approach is to import the entire module using import module_name and then access classes with module_name.class_name. This way, you maintain clarity about where each class comes from and avoid naming conflicts.




#                                                     Importing a Module into a Module



# To keep your code organized, you can spread your classes across multiple modules. For example, you can store the Car class in one module and the ElectricCar and Battery classes in another module called electric_car.py.
# In electric_car.py, you import the Car class from the car module because ElectricCar depends on it. If you forget to import it, you'll encounter an error when creating an ElectricCar instance.
# Here's how the structure looks:
# car.py: Contains only the Car class.
# electric_car.py: Contains the Battery class and the ElectricCar class, which imports Car.
# In your main file, my_cars.py, you can import both classes separately and create instances of each:



from car import Car
from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
my_tesla = ElectricCar('tesla', 'roadster', 2016)


# This way, you can create both regular and electric cars without issues.




#                                                      Finding Your Own Workflow



# Python offers various ways to structure code in large projects, and it's essential to understand these options to organize your own projects and comprehend others' work.
# When starting out, keep your code structure simple by using a single file. Once your code is working, you can move classes into separate modules. If you find that you like how modules interact, consider using them from the beginning of your next project. The key is to find an approach that allows you to write functional code and build from there.




#                                                           Try It yourself

#  9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod
# ule . Make a separate file that imports Restaurant . Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is work
# ing properly .
#  9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178) .
# Store the classes User, Privileges, and Admin in one module . Create a sepa
# rate file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly .
#  9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module . In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly



from restaurent import Restaurent
Starbucks = Restaurent("Starbucks" , "Italian")
Starbucks.open_restaurant()
from Admin1 import Admin
admin  = Admin("Harsh" , "Parashar" , 19 , "India" ," Male" , "Faridabad" , "Hindu")
admin.priveleges.show_priviliges()
admin.priveleges.show_priviliges()







#                                                                                      The Python standard library



# The Python standard library includes various modules, one of which is collections, which contains the OrderedDict class. Unlike regular dictionaries, OrderedDict maintains the order in which key-value pairs are added.
# Here's a brief example using OrderedDict to track favorite programming languages:
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")




#                                                                                       Try it yourself


#  9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary . Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary .
#  9-14. Dice: The module random contains functions that generate random num
# bers in a variety of ways . The function randint() returns an integer in the
# range you provide . The following code returns a number between 1 and 6:
#  from random import randint
#  x = randint(1, 6)
#  Make a class Die with one attribute called sides, which has a default
# value of 6 . Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has . Make a 6-sided die and roll
# it 10 times .
#  Make a 10-sided die and a 20-sided die . Roll each die 10 times .
#  9-15. Python Module of the Week: One excellent resource for exploring the
# Python standard library is a site called Python Module of the Week . Go to
# http://pymotw.com/ and look at the table of contents . Find a module that
# looks interesting to you and read about it, or explore the documentation of
# the collections and random modules



#Solution Do it Yourself Without Using Ai




#                                                                         Styling Classes in Python

# Naming Conventions:

# Class Names: Use CamelCaps (capitalize the first letter of each word, no underscores). For example, MyClass.
# Instance and Module Names: Use lowercase with underscores between words. For example, my_instance or my_module.
# Docstrings:

# Every class should have a docstring immediately after the class definition, describing its purpose.
# Each module should also have a docstring explaining what the classes within it do.
# Blank Lines:

# Use blank lines to organize code, but avoid excessive use.
# Within a class, use one blank line between methods.
# Use two blank lines to separate classes in a module.
# Import Statements:

# When importing modules, place standard library imports first, followed by a blank line, then your own module imports. This helps clarify the source of different modules.
# Summary of Chapter 9
# You learned to create classes, store information using attributes, and define methods for behavior.
# You understood how to use __init__() methods for instance creation and how to modify attributes.
# Inheritance was introduced to simplify related class creation, and you learned to use instances of one class as attributes in another.
# Storing classes in modules and importing them helps keep projects organized.
# You were introduced to the Python standard library, specifically the OrderedDict class.
# Finally, you learned about styling conventions for writing classes in Python.
# Looking Ahead
# In Chapter 10, you will learn about file handling to save program data and how to manage exceptions to handle errors effectively.






























