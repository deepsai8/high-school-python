# Chapter 4: Functions and Functional Programming

In this chapter, we’ll learn how to write **functions** in Python to make your code more organized and reusable. We’ll also take a peek into **functional programming** with some cool tools like **lambda functions**, **map**, and **filter**.

---

## What Are Functions?

Functions are like **recipes** for your code. Instead of writing the same thing over and over again, you can create a function and reuse it whenever you need it. Functions make your code easier to read and manage!

---

### Code Example: Defining a Function

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
```

### Explanation:
- **`def greet(name):`** defines a function named **`greet`** that takes a **parameter** called **`name`**.
- When we call **`greet("Alice")`**, the function prints **"Hello, Alice!"**.

### Why Use Functions?
Functions help you break down your code into smaller, manageable pieces. Imagine writing a game where every action is inside a function, and you can reuse them whenever you need!

---

## Parameters and Return Values

Functions can take **parameters** (inputs) and **return values** (outputs). Parameters let you pass in information, and return values let you get something back from the function.

### Code Example: Calculating the Area of a Circle

```python
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

print(area_of_circle(5))  # Prints the area of a circle with radius 5
```

### Explanation:
- **`area_of_circle(radius)`** takes one parameter: the radius of the circle.
- It calculates the area using the formula **πr²** and returns the result with **`return`**.

---

## Fun Example: Temperature Converter

Let’s write a function that converts temperatures from Celsius to Fahrenheit.

### Code Example: Celsius to Fahrenheit Converter

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
print(str(temp_c) + "°C is " + str(celsius_to_fahrenheit(temp_c)) + "°F")
```

### What’s Happening Here?
- The function **`celsius_to_fahrenheit`** converts Celsius to Fahrenheit using the formula and returns the Fahrenheit value.
- We then print the result.

---

## Lambda Functions: Mini Functions on the Go

A **lambda function** is like a mini-function that you can define in one line. It’s useful for quick, one-time calculations.

### Code Example: A Quick Lambda Function

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Prints 12
```

### Explanation:
- **`lambda x, y: x * y`** defines a small, anonymous function that multiplies two numbers.
- It’s similar to writing a full function, but more compact.

---

## Functional Programming Tools: Map, Filter, Reduce

Python provides some powerful tools for working with data in a functional programming style.

### **Map**
The **`map()`** function applies a function to every item in a list.

### Code Example: Using `map()` to Square Numbers

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Prints [1, 4, 9, 16]
```

### Explanation:
- **`map()`** applies the lambda function **`x ** 2`** to every number in the list.
- The result is a new list with the squares of the original numbers.

---

### **Filter**
The **`filter()`** function filters items from a list based on a condition.

### Code Example: Using `filter()` to Get Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Prints [2, 4, 6]
```

### Explanation:
- **`filter()`** keeps only the numbers that satisfy the condition (in this case, being even).

---

### **Reduce**
The **`reduce()`** function reduces a list to a single value by applying a function. You need to import it from the **`functools`** module.

### Code Example: Using `reduce()` to Multiply All Numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Prints 24 (1*2*3*4)
```

### Explanation:
- **`reduce()`** takes the first two numbers, multiplies them, then multiplies the result by the next number, and so on.

---

## Mini Project: To-Do List App

Now, let’s use functions to create a simple **to-do list app**. The app will allow users to add, view, and delete tasks.

### Code Example: To-Do List App

```python
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

def view_tasks():
    print("Your tasks:")
    for task in tasks:
        print("- " + task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed: " + task)
    else:
        print("Task not found!")

# Sample usage
add_task("Study for math test")
add_task("Buy groceries")
view_tasks()
remove_task("Buy groceries")
view_tasks()
```

### What’s Happening Here?
- **`add_task()`** adds a task to the list.
- **`view_tasks()`** prints all the tasks in the list.
- **`remove_task()`** removes a task if it exists in the list.

---

## Quiz Time! :tada:

Let’s see how well you understand functions and functional programming:

1. **What keyword is used to define a function in Python?**  
    A. define  
    B. function  
    C. def  

2. **What does a lambda function do?**  
    A. Creates a full function.  
    B. Defines a mini function in one line.  
    C. Deletes a function.  

3. **What does `map()` do?**  
    A. Maps two lists together.  
    B. Applies a function to each item in a list.  
    C. Filters out unwanted items.  

### Answers:
1. C
2. B
3. B

---

## Further Reading
If you want to explore more about functions in Python, check out:
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

Next, we’ll dive into **Object-Oriented Programming (OOP)** in Python. You’ll learn how to model real-world objects in code and build more complex projects!

---

Let me know when you're ready for **Chapter 5** on Object-Oriented Programming!