# Chapter 10: Fun Projects

In this chapter, we’re diving into cool, hands-on projects that you can build with Python! Whether you’re into math, games, data analysis, or web development, there’s something for everyone. These projects range from small calculators to more complex applications like a school management system, all designed to be easy to grasp and fun to create.

---

## 1. Mathematical Calculator Project

Let’s start simple with a **calculator** that can perform basic operations like addition, subtraction, multiplication, and division. This is a great way to practice using functions and control flow in Python.

### Code Example: Basic Calculator

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Menu for the calculator
def calculator():
    print("Welcome to the Python Calculator!")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

calculator()
```

### Explanation:
- This calculator lets you choose from four operations and input two numbers.
- Each operation is handled by its own function, and division handles the special case of dividing by zero.

---

## 2. Number Guessing Game

Create a fun **number guessing game** where the computer picks a random number, and the player has to guess it. The program gives feedback if the guess is too high or too low.

### Code Example: Number Guessing Game

```python
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed it in {attempts} attempts!")
            break

guessing_game()
```

### Explanation:
- The computer picks a random number between 1 and 100 using the `random` module.
- The player guesses until they find the correct number, and the program provides hints.

---

## 3. Rock, Paper, Scissors Game

Let’s build a simple game of **Rock, Paper, Scissors** where the player competes against the computer.

### Code Example: Rock, Paper, Scissors

```python
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice!")
    else:
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()
```

### Explanation:
- The computer randomly picks rock, paper, or scissors.
- The player chooses their move, and the program checks who wins based on the rules of the game.

---

## 4. Simple Snake Game with Pygame

Let’s create a simple **Snake Game** using the **Pygame** library. In this game, the player controls the snake and tries to eat food while avoiding the walls and the snake’s own body.

### Code Example: Snake Game

```python
import pygame
import time
import random

pygame.init()

# Screen settings
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
```

### Explanation:
- The **Pygame** library is used to create the window, draw the snake, and control the game.
- The player moves the snake with the arrow keys, trying to eat the food without hitting the walls or itself.

---

## 5. Data Analysis Project Using Pandas and Matplotlib

Let’s analyze some **student scores** and visualize the data using **Pandas** and **Matplotlib**.

### Code Example: Data Analysis of Student Scores

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame of student scores
data = {
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 92, 78, 90],
    "Science": [88, 95, 80, 85],
    "English": [75, 89, 95, 70]
}
df = pd.DataFrame(data)

# Calculate the average score for each

 student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Print the DataFrame
print(df)

# Plot the average scores
plt.bar(df["Student"], df["Average"])
plt.title("Average Scores of Students")
plt.xlabel("Student")
plt.ylabel("Average Score")
plt.show()
```

### Explanation:
- **Pandas** is used to store the data in a DataFrame and calculate average scores.
- **Matplotlib** is used to create a bar chart showing the average scores of each student.

---

## 6. Tic-Tac-Toe Game

Create a **Tic-Tac-Toe** game where two players take turns marking the board until someone wins or the game ends in a draw.

### Code Example: Tic-Tac-Toe Game

```python
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move! Try again.")

    print("It's a tie!")

tic_tac_toe()
```

### Explanation:
- This game allows two players to take turns choosing a position on the grid.
- The `check_winner` function determines if one of the players has won by completing a row, column, or diagonal.

---

## 7. Currency Converter

Build a **currency converter** that converts between different currencies using a fixed conversion rate.

### Code Example: Currency Converter

```python
def currency_converter(amount, from_currency, to_currency):
    conversion_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.5,
        "GBP": 0.75
    }

    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return "Invalid currency code!"

    converted_amount = amount * conversion_rates[to_currency] / conversion_rates[from_currency]
    return round(converted_amount, 2)

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD, EUR, JPY, GBP): ").upper()
to_currency = input("To currency (USD, EUR, JPY, GBP): ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
```

### Explanation:
- This program uses a dictionary to store conversion rates and calculates the converted amount based on user input.

---

## 8. School Management System (Flask Web App)

Let’s build a simple **school management system** that allows you to manage students, classes, and grades. This project uses **Flask**, a lightweight web framework.

### Code Example: Simple Flask-Based School Management System

```python
from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    grade = request.form['grade']
    students.append({"name": name, "grade": grade})
    return home()

@app.route('/delete_student/<name>')
def delete_student(name):
    global students
    students = [s for s in students if s["name"] != name]
    return home()

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
- This Flask application allows you to add students and their grades, display the list of students, and delete students from the list.
- **HTML templates** can be used to create the front-end (UI) for this project.

---

## 9. Weather App (Using API)

Create a **Weather App** that fetches the current weather for a city using the **OpenWeatherMap API**.

### Code Example: Weather App

```python
import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]
        print(f"City: {city}\nTemperature: {temp}°C\nWeather: {weather_desc}\nHumidity: {humidity}%")
    else:
        print("City not found!")

city = input("Enter city name: ")
get_weather(city)
```

### Explanation:
- This project fetches weather data from the **OpenWeatherMap API** and displays the temperature, weather description, and humidity for the given city.

---

## 10. Quiz Application

Build a **quiz application** that asks multiple-choice questions and keeps track of the player’s score.

### Code Example: Quiz App

```python
def run_quiz():
    questions = {
        "What is the capital of France?": {"options": ["A) Paris", "B) Rome", "C) Madrid"], "answer": "A"},
        "What is 2 + 2?": {"options": ["A) 3", "B) 4", "C) 5"], "answer": "B"},
        "Who wrote '1984'?": {"options": ["A) George Orwell", "B) J.K. Rowling", "C) Charles Dickens"], "answer": "A"}
    }

    score = 0
    for question, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        answer = input("Your answer: ").upper()

        if answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {data['answer']}\n")

    print(f"You got {score}/{len(questions)} correct!")

run_quiz()
```

### Explanation:
- This project creates a simple quiz with multiple-choice questions and checks if the player’s answer is correct.

---

#**Advanced Projects**

# Project 11: School Management System (Flask-Based Web App)

This project will simulate a **school management system** where you can manage students, their classes, and grades. We'll split it into multiple Python files and also include templates for rendering web pages.

### Project Structure:
```
school_management/
│
├── app.py  (Main Flask application)
├── models.py  (Data structure to manage students, classes, and grades)
├── templates/
│   ├── index.html  (Home page template)
│   ├── add_student.html  (Form to add new students)
│   └── student_detail.html  (Student detail view with grades)
└── static/
    └── style.css  (Optional: CSS for styling)
```

---

### **File 1: `models.py` (Student and Class Data Structure)**

```python
# models.py
students = []

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0
```

### Explanation:
- This file contains the `Student` class, which manages student data, including their name, age, and grades.
- It has methods to add grades and calculate the student’s average grade.

---

### **File 2: `app.py` (Main Flask Application)**

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import students, Student

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_student = Student(name, age)
        students.append(new_student)
        return redirect(url_for('home'))
    return render_template('add_student.html')

@app.route('/student/<name>')
def student_detail(name):
    for student in students:
        if student.name == name:
            return render_template('student_detail.html', student=student)
    return "Student not found", 404

@app.route('/student/<name>/add_grade', methods=['POST'])
def add_grade(name):
    subject = request.form['subject']
    grade = int(request.form['grade'])
    for student in students:
        if student.name == name:
            student.add_grade(subject, grade)
            return redirect(url_for('student_detail', name=name))
    return "Student not found", 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
- This is the main Flask application. It manages routing, displaying students, and adding new students and grades.
- The `add_student` route allows for adding new students via a form.
- The `student_detail` route shows detailed information about a specific student.
- The `add_grade` route is a POST request that allows the addition of grades to a student.

---

### **File 3: `index.html` (Home Page Template)**

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>School Management System</title>
</head>
<body>
    <h1>School Management System</h1>
    <h2>Student List</h2>
    <ul>
        {% for student in students %}
            <li><a href="{{ url_for('student_detail', name=student.name) }}">{{ student.name }}</a> (Age: {{ student.age }})</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_student') }}">Add New Student</a>
</body>
</html>
```

### Explanation:
- This is the homepage that displays a list of students. Each student’s name links to their detailed view.
- There’s also a link to add a new student.

---

### **File 4: `add_student.html` (Form to Add Students)**

```html
<!-- templates/add_student.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Add New Student</title>
</head>
<body>
    <h1>Add New Student</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" name="name" required><br><br>
        <label for="age">Age:</label>
        <input type="text" name="age" required><br><br>
        <input type="submit" value="Add Student">
    </form>
</body>
</html>
```

### Explanation:
- This page provides a simple form to add a new student by entering their name and age.

---

### **File 5: `student_detail.html` (Student Detail with Grades)**

```html
<!-- templates/student_detail.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>
    <h1>Details for {{ student.name }}</h1>
    <p>Age: {{ student.age }}</p>
    <h3>Grades:</h3>
    <ul>
        {% for subject, grade in student.grades.items() %}
            <li>{{ subject }}: {{ grade }}</li>
        {% endfor %}
    </ul>
    <p>Average Grade: {{ student.get_average_grade() }}</p>

    <h3>Add Grade</h3>
    <form method="POST" action="{{ url_for('add_grade', name=student.name) }}">
        <label for="subject">Subject:</label>
        <input type="text" name="subject" required><br><br>
        <label for="grade">Grade:</label>
        <input type="number" name="grade" required><br><br>
        <input type="submit" value="Add Grade">
    </form>

    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Explanation:
- This page shows detailed information about a student, including their grades.
- There’s also a form to add new grades for a specific student.

---

### **File 6: `style.css` (Optional CSS for Styling)**

```css
/* static/style.css */
body {
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}

ul {
    list-style-type: none;
}

a {
    text-decoration: none;
    color: blue;
}
```

### Explanation:
- You can optionally include some CSS to make the web app look nicer.

---

### How to Run the Project:
1. Install **Flask** by running `pip install flask`.
2. Create the project structure and files.
3. Run the application by executing `python app.py`.
4. Open your browser and go to `http://127.0.0.1:5000/`.

---

# Project 12: Advanced Quiz Application

This project is a **Quiz Game** where the user answers multiple-choice questions. It tracks their score and provides feedback after the quiz.

### Project Structure:
```
quiz_app/
│
├── app.py  (Main Quiz Application)
├── questions.py  (Questions data)
└── templates/
    ├── index.html  (Start screen)
    ├── quiz.html  (Quiz screen)
    └── result.html  (Result screen)
```

---

### **File 1: `questions.py` (Questions Data)**

```python
# questions.py
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin"],
        "answer": "A"
    },
    {
        "question": "Who wrote '1984'?",
        "options": ["A) George Orwell", "B) Mark Twain", "C) J.K. Rowling"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5"],
        "answer": "B"
    }
]
```

### Explanation:
- This file contains a list of dictionaries, where each dictionary represents a quiz question with its options and the correct answer.

---

### **File 2: `app.py` (Main Quiz Application)**

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from questions import questions

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

@app.route('/')
def index():
    session['score'] = 0  # Reset score
    session['question_number'] = 0  # Start with the first question
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected_option = request.form.get('option')
        correct_answer = questions[session['question_number']]["answer"]

        if selected_option == correct_answer:
            session['score'] += 1

        session['question_number'] += 1

        if session['question_number'] >= len(questions):


 return redirect(url_for('result'))

    question = questions[session['question_number']]
    return render_template('quiz.html', question=question)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total_questions = len(questions)
    return render_template('result.html', score=score, total_questions=total_questions)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
- The quiz starts by showing the first question.
- The player’s score is stored in the session, and each answer is checked against the correct answer.
- Once all questions are answered, the user is redirected to the result page, where they can see their score.

---

### **File 3: `index.html` (Start Screen)**

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Game</title>
</head>
<body>
    <h1>Welcome to the Quiz Game!</h1>
    <p>Test your knowledge with some fun questions!</p>
    <a href="{{ url_for('quiz') }}">Start Quiz</a>
</body>
</html>
```

### Explanation:
- This is the home page where the user can start the quiz by clicking the **Start Quiz** button.

---

### **File 4: `quiz.html` (Quiz Screen)**

```html
<!-- templates/quiz.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Game</title>
</head>
<body>
    <h1>{{ question['question'] }}</h1>
    <form method="POST">
        {% for option in question['options'] %}
            <label>
                <input type="radio" name="option" value="{{ option[0] }}" required>
                {{ option }}
            </label><br><br>
        {% endfor %}
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### Explanation:
- This page dynamically displays each question and its multiple-choice options.
- The player selects their answer and submits it.

---

### **File 5: `result.html` (Result Screen)**

```html
<!-- templates/result.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Result</title>
</head>
<body>
    <h1>Quiz Result</h1>
    <p>You scored {{ score }} out of {{ total_questions }}!</p>
    <a href="{{ url_for('index') }}">Play Again</a>
</body>
</html>
```

### Explanation:
- This page displays the final score after all questions have been answered and offers an option to restart the quiz.

---

### How to Run the Project:
1. Install **Flask** by running `pip install flask`.
2. Create the project structure and files.
3. Run the application by executing `python app.py`.
4. Open your browser and go to `http://127.0.0.1:5000/`.

---

These projects provide an opportunity to build more complex systems while keeping the concepts easy to understand and fun to implement. Let me know if you need further adjustments or additions!

### Final Thoughts:

These 10 projects provide a mix of games, applications, and data analysis tools that are fun, engaging, and educational. Each project builds on the skills students have learned and adds a creative element to make learning Python exciting!