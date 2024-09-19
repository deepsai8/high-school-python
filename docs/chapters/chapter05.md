# Chapter 5: Object-Oriented Programming (OOP)

In this chapter, we’ll explore **Object-Oriented Programming (OOP)** in Python. OOP is a way to model real-world things in your code. You can think of it like creating blueprints for objects, like cars, animals, or even people!

---

## What is OOP?

In Python, **Object-Oriented Programming (OOP)** lets you structure your code in terms of **objects**. An **object** is something that contains both data (attributes) and functions (methods) that operate on the data.

At the core of OOP are:
- **Classes**: Blueprints for creating objects.
- **Objects**: Instances of a class.
- **Methods**: Functions that belong to a class.
- **Attributes**: Variables that belong to a class.

### Real-Life Analogy
Think of a **class** as a blueprint for a car. You can make multiple cars from the same blueprint, but each car is its own **object** (or instance). The blueprint (class) defines things like the number of doors, color, and engine type (attributes), as well as what the car can do, like drive or honk (methods).

---

## Creating Classes and Objects

Let’s create a simple class to represent a **Person**.

### Code Example: Defining a Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

# Creating an object (instance) of the Person class
person1 = Person("Alice", 16)
person1.introduce()
```

### Explanation:
- **`class Person:`** defines a class called **Person**.
- **`__init__()`** is a special method called a **constructor**. It runs when we create a new object and initializes its attributes.
- **`self.name`** and **`self.age`** are attributes that store the name and age of the person.
- **`introduce()`** is a method that prints a message introducing the person.

---

## Methods and Attributes

- **Attributes** are the data associated with an object (like a person’s name and age).
- **Methods** are functions that belong to an object (like introducing yourself).

### Code Example: Adding an Action (Method)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

    def celebrate_birthday(self):
        self.age += 1
        print("Happy Birthday! You are now " + str(self.age) + " years old.")

# Creating a new person
person2 = Person("Bob", 17)
person2.introduce()
person2.celebrate_birthday()  # Increases the age by 1 and prints a birthday message
```

### Explanation:
- **`celebrate_birthday()`** is a new method that increases the person’s age by 1 and prints a birthday message.
- You can call methods on objects to make them do things!

---

## Inheritance: Passing on Traits

In OOP, **inheritance** allows one class to inherit attributes and methods from another class. This lets you create specialized versions of existing classes without rewriting code.

### Code Example: Inheriting from the `Person` Class

```python
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Call the constructor of the Person class
        self.grade = grade

    def study(self):
        print(self.name + " is studying for a grade " + str(self.grade) + " exam.")

# Creating a Student object
student1 = Student("Charlie", 16, 10)
student1.introduce()
student1.study()
```

### Explanation:
- **`Student(Person)`**: The `Student` class **inherits** from the `Person` class.
- **`super().__init__(name, age)`** calls the constructor of the `Person` class to initialize the name and age attributes.
- The `Student` class has an extra attribute, **grade**, and a new method, **study()**.

---

## Fun Example: Modeling a Pet

Let’s create a simple program to model a **Pet** using OOP. You can feed your pet, play with it, and see how happy it is!

### Code Example: A Simple Pet Class

```python
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def feed(self):
        self.happiness += 10
        print(self.name + " is happy! Happiness level: " + str(self.happiness))

    def play(self):
        self.happiness += 20
        print(self.name + " is excited! Happiness level: " + str(self.happiness))

# Creating a pet object
my_pet = Pet("Buddy", "dog")
my_pet.feed()
my_pet.play()
```

### What’s Happening Here?
- The **Pet** class has attributes like **name**, **species**, and **happiness**.
- Methods like **feed()** and **play()** increase the pet’s happiness when called.

---

## Mini Project: Simple Banking System

Let’s apply what we’ve learned by building a **simple banking system** using OOP. We’ll create classes for a **BankAccount** and allow users to deposit, withdraw, and check their balance.

### Code Example: Banking System

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def check_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# Creating a bank account
account1 = BankAccount("Alice")
account1.deposit(100)
account1.withdraw(50)
account1.check_balance()
```

### Explanation:
- **`deposit()`** increases the account balance.
- **`withdraw()`** decreases the balance if enough funds are available.
- **`check_balance()`** shows the current balance.

---

## Quiz Time! :tada:

Test your knowledge of OOP with this quiz:

1. **What is a class in Python?**  
    A. A blueprint for creating objects  
    B. A list of functions  
    C. A type of loop  

2. **What is the special method called that initializes a class?**  
    A. `__init__`  
    B. `start`  
    C. `main`  

3. **What keyword is used to inherit from another class?**  
    A. extend  
    B. inherit  
    C. super  

### Answers:
1. A
2. A
3. C

---

## Further Reading
If you want to dive deeper into OOP in Python, check out:
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)

---

In the next chapter, we’ll explore **real-world applications** of Python, including how it’s used in **data science**, **automation**, and even **artificial intelligence**!

---

You're ready for **Chapter 6** on Python applications!