# Chapter 3: Lists & Tuples – Python Practice with Output and Explanations

# ----------------------------------
# Creating and Printing Lists
# Why: Lists store multiple items in one variable.
# How: Define using square brackets [item1, item2, ...]
# Use: Group related data (e.g., names, numbers)
# ----------------------------------
list1 = [1, 2, 3, 4]
list2 = ["A", 0.1, 89]
list3 = ["Harsh", "Kunal", "Kinney"]

print("List 1:", list1)      # Output: [1, 2, 3, 4]
print("List 2:", list2)      # Output: ['A', 0.1, 89]
print("List 3:", list3)      # Output: ['Harsh', 'Kunal', 'Kinney']

# ----------------------------------
# Accessing and Formatting Elements
# Why: Use indexing to access specific elements.
# Use: f-string + title() formats the string nicely.
# ----------------------------------
cars = ["bugatti", "veron", "mustang"]
print(f"I would like to own a {cars[0].title()} car.")
# Output: I would like to own a Bugatti car.

# ----------------------------------
# Guest List (Exercise 3-4)
# Why: Practice working with list elements
# Use: Indexing and string formatting
# ----------------------------------
guestlist = ["Harsh", "Kunal", "John"]
print(f"Hi {guestlist[0]}, you are invited to dinner!")  # Output: Hi Harsh...
print(f"Hi {guestlist[1]}, you are invited to dinner!")  # Output: Hi Kunal...
print(f"Hi {guestlist[2]}, you are invited to dinner!")  # Output: Hi John...

# ----------------------------------
# Updating Guest List (Exercise 3-5)
# Why: Learn how to update list values using indexing
# Use: Replace an unavailable guest
# ----------------------------------
print(f"\nUnfortunately, {guestlist[2]} can't make it to dinner.")
# Output: Unfortunately, John can't make it to dinner.
guestlist[2] = "Kimoha"
print(f"{guestlist[2]} has been invited instead.")  
# Output: Kimoha has been invited instead.

for guest in guestlist:
    print(f"Hi {guest}, you are still invited to dinner!")
# Output:
# Hi Harsh, you are still invited...
# Hi Kunal, you are still invited...
# Hi Kimoha, you are still invited...

# ----------------------------------
# Adding More Guests (Exercise 3-6)
# Why: Learn insert(), append() methods to modify list
# ----------------------------------
print("\nGood news! We found a bigger table.")
guestlist.insert(0, "Hassan")     # Insert at beginning
guestlist.insert(2, "Rahees")     # Insert at middle
guestlist.append("Arhaan")        # Add to end

for guest in guestlist:
    print(f"Hi {guest}, you're invited to dinner!")
# Output:
# Hi Hassan...
# Hi Harsh...
# Hi Rahees...
# Hi Kunal...
# Hi Kimoha...
# Hi Arhaan...

# ----------------------------------
# Reducing the Guest List (Exercise 3-7)
# Why: Learn pop() and manage list length dynamically
# Use: Real-world logic — not enough space
# ----------------------------------
print("\nUnfortunately, the new table won’t arrive in time. Can only invite two people.")

while len(guestlist) > 2:
    removed = guestlist.pop()
    print(f"Sorry {removed}, we can’t invite you to dinner.")
# Output: Removes Arhaan, Kimoha, Kunal, Rahees...

for guest in guestlist:
    print(f"{guest}, you're still invited.")
# Output:
# Hassan, you're still invited.
# Harsh, you're still invited.

guestlist.clear()  # Empties the list
print("Final guest list:", guestlist)  # Output: []

# ----------------------------------
# Favorite Places List
# Why: Practice sorted(), reverse(), sort()
# Use: Learn difference between temporary and permanent sorting
# ----------------------------------
places = ["Turkey", "Switzerland", "Kashmir", "Canada", "UAE"]
print("\nOriginal order:", places)
# Output: ['Turkey', 'Switzerland', 'Kashmir', 'Canada', 'UAE']

print("Alphabetical:", sorted(places))
# Output: ['Canada', 'Kashmir', 'Switzerland', 'Turkey', 'UAE']

print("Original after sorted():", places)
# Output: Original list remains unchanged

print("Reverse alphabetical:", sorted(places, reverse=True))
# Output: ['UAE', 'Turkey', 'Switzerland', 'Kashmir', 'Canada']

places.reverse()
print("Reversed order:", places)
# Output: ['UAE', 'Canada', 'Kashmir', 'Switzerland', 'Turkey']

places.sort()
print("Sorted (permanent):", places)
# Output: ['Canada', 'Kashmir', 'Switzerland', 'Turkey', 'UAE']

places.sort(reverse=True)
print("Reverse sorted:", places)
# Output: ['UAE', 'Turkey', 'Switzerland', 'Kashmir', 'Canada']

# ----------------------------------
# List Length
# Why: Use len() to count items in a list
# ----------------------------------
fav_places = ["Turkey", "Switzerland", "Kashmir", "Canada", "UAE"]
print("\nLength of fav_places:", len(fav_places))  
# Output: 5

# ----------------------------------
# List Examples with Loops
# Why: Use loops to work with list data
# Use: Display messages for each list element
# ----------------------------------
print("\nTransportation Wishes:")
bikes = ["Yamaha R15", "KTM Duke", "Royal Enfield", "Kawasaki Ninja"]
for bike in bikes:
    print(f"I would like to own a {bike} motorcycle.")
# Output:
# I would like to own a Yamaha R15...
# I would like to own a KTM Duke...
# etc.

# ----------------------------------
# Tuple Practice
# Why: Tuples are immutable (unchangeable) versions of lists
# Use: Define with parentheses () instead of []
# ----------------------------------
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dim in dimensions:
    print(dim)
# Output:
# 200
# 50

# Reassigning a new tuple
dimensions = (400, 100)
print("Modified dimensions:")
for dim in dimensions:
    print(dim)
# Output:
# 400
# 100

# ----------------------------------
# Difference between Tuple and Set
# Why: Sets do not allow duplicates, are unordered
# Use: Tuples = ordered + immutable, Sets = unordered + mutable + unique
# ----------------------------------
sample_tuple = (1, 2, 3, 4, 5, 6)
sample_set = {1, 2, 3, 4, 5, 6}

print("\nTuple:", sample_tuple, "Length:", len(sample_tuple))
# Output: Tuple: (1, 2, 3, 4, 5, 6) Length: 6

print("Set:", sample_set, "Length:", len(sample_set))
# Output: Set: {1, 2, 3, 4, 5, 6} Length: 6


# ----------------------------------
# ✅ Summary Table: Lists, Tuples, and Sets
# ----------------------------------

print("\nSummary:\n")
print("| Concept        | Keyword        | Syntax Example                | Why Use It                                |")
print("|----------------|----------------|-------------------------------|--------------------------------------------|")
print("| List           | `[]`           | list1 = [1, 2, 3]             | Store multiple ordered, changeable values  |")
print("| Tuple          | `()`           | t = (1, 2)                    | Immutable fixed-length group of values     |")
print("| Set            | `{}`           | s = {1, 2}                    | Unique, unordered values                   |")
print("| Indexing       | `list[0]`      | names[0]                      | Access individual elements                 |")
print("| Loop           | `for x in y:`  | for i in list:               | Iterate through items                      |")
print("| Append         | `.append(x)`   | list.append('value')         | Add item to end of list                    |")
print("| Insert         | `.insert(i,x)` | list.insert(0, 'value')      | Insert item at specific position           |")
print("| Remove         | `.pop()`       | list.pop()                   | Remove and return last item                |")
print("| Sort (temp)    | `sorted()`     | sorted(list)                 | Return a new sorted version                |")
print("| Sort (perm)    | `.sort()`      | list.sort()                  | Sort list in-place                         |")
print("| Reverse        | `.reverse()`   | list.reverse()               | Reverse list in-place                      |")
print("| Length         | `len()`        | len(list)                    | Count elements in list                     |")
