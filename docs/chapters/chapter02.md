# Chapter 2: Data Structures

In this chapter, we’ll explore how to store and organize information in Python using **data structures**. Think of them like different boxes where you can store and arrange things you want to keep.

---

## What Are Data Structures?

In Python, we use **data structures** to organize and manage data. There are four basic types we'll look at:
1. **Variables** (like boxes that hold values)
2. **Lists** (like a to-do list)
3. **Tuples** (like a to-do list that never changes)
4. **Dictionaries** (like a list of names and their phone numbers)
5. **Sets** (a list, but without duplicates)

---

## Variables and Data Types

A **variable** is like a container where we can store a piece of information. That information can be a **number**, **string** (text), or **boolean** (True/False).

### Code Example: Variables in Action

```python
name = "Alice"  # String (text)
age = 16        # Integer (whole number)
is_student = True  # Boolean (True/False)
```

### Explanation:
- **`name`** stores a piece of text (called a **string**).
- **`age`** stores a whole number (an **integer**).
- **`is_student`** stores a true/false value (a **boolean**).

---

## Lists: Organizing a Collection of Items

A **list** is like a shopping list: you can store multiple things in it, and they don’t have to be the same type of thing. You can add to the list, remove things, or even change items in it.

### Code Example: A List of Your Favorite Foods

```python
favorite_foods = ["pizza", "burger", "ice cream"]
print(favorite_foods[0])  # Prints the first item: pizza

# Adding an item to the list
favorite_foods.append("pasta")
print(favorite_foods)
```

### Explanation:
- **`favorite_foods[0]`** refers to the first item in the list (Python starts counting from 0).
- **`.append()`** adds a new item to the list.

---

## Tuples: Lists that Can’t Be Changed

A **tuple** is like a list, but once you create it, you can’t change it. It’s great for things that should stay the same, like the coordinates of a point.

### Code Example: A Tuple of Coordinates

```python
point = (3, 4)  # A tuple representing a point on a graph
print(point[0])  # Prints 3
```

### Fun Fact:
- You can’t change **tuples** once they’re created, so they’re perfect for things that don’t need to be modified.

---

## Dictionaries: Storing Data in Key-Value Pairs

A **dictionary** stores data in pairs, like a real-life dictionary that has words (keys) and their meanings (values). This is perfect for storing related information, like names and phone numbers.

### Code Example: A Phone Book

```python
phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-8765"
}
print(phone_book["Alice"])  # Prints Alice's phone number
```

### Explanation:
- **`"Alice"`** is the key, and **`"555-1234"`** is the value.
- You can use the key to get the value, like looking up a word in a dictionary.

---

## Sets: Collections with No Duplicates

A **set** is like a list, but it automatically removes duplicates. If you add the same item twice, it’ll only keep one.

### Code Example: A Set of Unique Colors

```python
colors = {"red", "blue", "green", "red"}  # "red" appears twice
print(colors)  # Output will be: {'red', 'blue', 'green'}
```

### Explanation:
- Sets are great when you want to make sure there are no duplicates.

---

## Fun Example: Storing Your Friends’ Favorite Snacks

Let’s combine these data structures to store the names of your friends and their favorite snacks using a **dictionary** and a **list**.

### Code Example: Friends and Snacks

```python
friends_snacks = {
    "Alice": ["chips", "soda"],
    "Bob": ["pizza", "ice cream"],
    "Charlie": ["cookies", "juice"]
}

print(friends_snacks["Alice"])  # Prints Alice's favorite snacks
```

### What’s Happening Here?
- We’re using a dictionary to store friends’ names as keys and their favorite snacks as lists (values).

---

## Mini Project: Build a Contact Book

Let’s take what we’ve learned and build a **contact book** that stores names and phone numbers. You’ll be able to add, remove, and search for contacts!

### Code Example: Contact Book

```python
contacts = {}

# Adding contacts
contacts["Alice"] = "555-1234"
contacts["Bob"] = "555-5678"

# Searching for a contact
name = input("Enter a name to search: ")
if name in contacts:
    print(name + "'s phone number is " + contacts[name])
else:
    print("Contact not found.")
```

### Explanation:
- We’re using a dictionary to store names and phone numbers.
- The program lets you search for a contact by name.

---

## Quiz Time! :tada:

Test your knowledge with this quick quiz:

1. **What data structure allows duplicates?**  
    A. List  
    B. Tuple  
    C. Set  

1. **Which of these is a key-value pair data structure?**  
    A. List  
    B. Dictionary  
    C. Set  

1. **What does a tuple allow?**  
    A. Changing its values  
    B. Repeating values  
    C. Keeping data unchanged  

### Answers:
1. A
2. B
3. C

---

## Further Reading
If you want to learn more about Python’s data structures, check out:
- [Python Lists and Tuples](https://docs.python.org/3/tutorial/datastructures.html)

---

In the next chapter, we’ll learn about **conditions** and how to make decisions in Python programs. Stay tuned for some fun examples and another mini project!

---

How does this look? Ready to move on to Chapter 3?