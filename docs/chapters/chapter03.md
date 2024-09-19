# Chapter 3: Conditions and Control Flow

In this chapter, we’ll learn how to make decisions in our programs using conditions and control flow. Think of it like choosing your own adventure story—your program will behave differently depending on the choices you make!

---

## Making Decisions with Conditions

Sometimes, your program needs to make a choice. That’s where **conditions** come in. Python uses the following keywords to make decisions:
- **if**: If something is true, do this.
- **else**: If it’s not true, do something else.
- **elif**: If the first condition isn’t true, check another condition.

### Code Example: Deciding What to Wear Based on the Weather

```python
weather = input("What’s the weather like? (sunny/rainy/cold): ")

if weather == "sunny":
    print("Wear sunglasses and a hat!")
elif weather == "rainy":
    print("Take an umbrella!")
else:
    print("Wear a warm jacket!")
```

### Explanation:
- **if weather == "sunny"**: If the weather is sunny, the program will tell you to wear sunglasses and a hat.
- **elif** checks another condition.
- **else** catches everything else if none of the conditions are true.

---

## Loops: Doing Things Over and Over

Loops are used when you want your program to repeat something multiple times. There are two types of loops in Python:
1. **For Loop**: Runs a block of code a specific number of times.
2. **While Loop**: Repeats as long as a condition is true.

---

### For Loops

A **for loop** allows you to iterate over a collection of items (like a list) or repeat something a set number of times.

### Code Example: Counting Down for a Rocket Launch

```python
for countdown in range(10, 0, -1):
    print(countdown)
print("Blast off!")
```

### Explanation:
- **range(10, 0, -1)** means we start counting from 10 and stop at 1, going down by 1 each time.
- After the countdown finishes, we print **"Blast off!"**.

---

### While Loops

A **while loop** keeps repeating as long as a certain condition is true. Be careful with while loops—you need to make sure the condition eventually becomes false, or the loop will go on forever!

### Code Example: Asking for the Correct Password

```python
password = ""
while password != "letmein":
    password = input("Enter the password: ")

print("Access granted!")
```

### Explanation:
- The loop keeps asking for the password until you type **"letmein"**. Once you do, it breaks out of the loop and prints **"Access granted!"**.

---

## Fun Example: A Number Guessing Game

Let’s create a simple guessing game where the computer picks a random number, and the player has to guess it.

### Code Example: Number Guessing Game

```python
import random

secret_number = random.randint(1, 10)  # Picks a random number between 1 and 10
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You guessed it!")
```

### What’s Happening Here?
- The computer picks a random number using **`random.randint()`**.
- The player keeps guessing until they get it right, with hints if their guess is too high or too low.

---

## Mini Project: A Simple Text Adventure Game

Now, let’s take everything we’ve learned so far and build a simple text-based adventure game. The game will present choices, and depending on the player’s input, different things will happen!

### Code Example: Text Adventure Game

```python
print("Welcome to the adventure game!")

choice1 = input("You are in a dark forest. Do you go left or right? (left/right): ")

if choice1 == "left":
    print("You meet a friendly dragon who helps you find treasure!")
    choice2 = input("Do you take the treasure or leave it? (take/leave): ")

    if choice2 == "take":
        print("The treasure is cursed! You turn into a frog!")
    else:
        print("You walk away and live happily ever after.")

elif choice1 == "right":
    print("You fall into a river and have to swim to safety!")
    choice3 = input("Do you swim fast or slow? (fast/slow): ")

    if choice3 == "fast":
        print("You safely reach the shore!")
    else:
        print("You get swept away by the current!")
else:
    print("You stand still and a squirrel steals your lunch.")
```

### Explanation:
- This is a simple text adventure game with multiple choices.
- The player’s input determines the story’s outcome!

---

## Quiz Time! :tada:

Check your understanding with this short quiz:

1. **What keyword is used for checking additional conditions in Python?**  
    A. elif  
    B. loop  
    C. case  

2. **What does a `while` loop do?**  
    A. Run a block of code a certain number of times.  
    B. Run a block of code while a condition is true.  
    C. Run a block of code forever.  

3. **What function is used to generate a random number in Python?**  
    A. randint  
    B. random.pick  
    C. choose  

### Answers:
1. A
2. B
3. A

---

## Further Reading
To dive deeper into conditions and loops, check out:
- [Python Conditions and Loops](https://docs.python.org/3/tutorial/controlflow.html)

---

In the next chapter, we’ll explore **functions** and how you can make your code more reusable and organized. You’ll also get to create a cool to-do list app using functions!

---

Time to move on to **Chapter 4**!