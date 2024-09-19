# Chapter 6: Python in the Real World

Python isn't just a language for beginners—it's used by professionals across many industries for all sorts of exciting applications. In this chapter, we’ll explore how Python is used in **data science**, **automation**, **web scraping**, and even **artificial intelligence** (AI). Let’s dive into these fun and practical uses of Python!

---

## Python for Data Science

Data science is all about analyzing and visualizing data to gain insights. Python has powerful libraries like **Pandas** and **Matplotlib** that make working with data easy and fun!

---

### Using Pandas: Analyzing Data

The **Pandas** library is like a Swiss Army knife for data analysis. You can store data in **DataFrames** (think of them as Excel sheets) and easily manipulate them.

### Code Example: Analyzing School Grades

```python
import pandas as pd

# Creating a DataFrame of student grades
data = {
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 92, 78, 90],
    "Science": [88, 95, 80, 85]
}

grades = pd.DataFrame(data)
print(grades)

# Calculating the average grades
grades["Average"] = (grades["Math"] + grades["Science"]) / 2
print("\nAverage Grades:")
print(grades)
```

### Explanation:
- **`pandas.DataFrame`** lets you create tables of data.
- We calculate the average grades for each student and add that information to the DataFrame.

---

### Using Matplotlib: Visualizing Data

Data is often easier to understand when you visualize it. The **Matplotlib** library lets you create beautiful charts and graphs.

### Code Example: Plotting a Bar Chart of Grades

```python
import matplotlib.pyplot as plt

students = ["Alice", "Bob", "Charlie", "David"]
math_grades = [85, 92, 78, 90]

plt.bar(students, math_grades)
plt.xlabel("Students")
plt.ylabel("Math Grades")
plt.title("Math Grades of Students")
plt.show()
```

### Explanation:
- **`plt.bar()`** creates a bar chart showing the math grades of each student.
- We add labels for the x-axis, y-axis, and a title.

---

## Python for Web Automation

Python can also control the web for you. You can use it to automate repetitive tasks, like filling out forms or scraping data from websites.

---

### Using Selenium: Automating Web Browsing

**Selenium** is a Python library that lets you automate browser activities. It’s perfect for automating things like logging into websites or gathering information.

### Code Example: Automating Google Search (Simplified Example)

```python
from selenium import webdriver

# Setting up the browser
browser = webdriver.Chrome()

# Open Google's homepage
browser.get('http://www.google.com')

# Find the search box using its name attribute
search_box = browser.find_element("name", "q")

# Type in the search query and hit enter
search_box.send_keys('Python programming')
search_box.submit()

# The browser will now show search results for 'Python programming'
```

### What’s Happening Here?
- **Selenium** opens a browser and navigates to Google.
- It finds the search box, enters a search term, and submits the search.

---

## Python for Artificial Intelligence (AI)

Python is one of the most popular languages for **artificial intelligence**. Libraries like **TensorFlow** and **scikit-learn** allow you to build models that can recognize patterns, classify data, and even make decisions.

---

### Using Scikit-Learn: Building a Simple AI Model

Let’s use **scikit-learn**, a powerful library for machine learning, to create a simple model that predicts if a student passed or failed based on their grades.

### Code Example: Simple AI Model for Predicting Pass/Fail

```python
from sklearn.tree import DecisionTreeClassifier

# Data: grades in Math and Science
X = [[85, 88], [92, 95], [78, 80], [90, 85], [60, 55]]
# Labels: 1 for Pass, 0 for Fail
y = [1, 1, 1, 1, 0]

# Creating a decision tree classifier
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# Predicting pass/fail for a new student
new_student_grades = [[70, 75]]
prediction = clf.predict(new_student_grades)
if prediction == 1:
    print("The student passed!")
else:
    print("The student failed.")
```

### Explanation:
- **DecisionTreeClassifier** builds a simple model that predicts if a student passes or fails based on their grades.
- We use the model to predict whether a new student will pass.

---

## Fun Example: Sending Automated Emails

Let’s automate something fun—sending an email using Python! We’ll use the **smtplib** library to send an email through a Gmail account.

### Code Example: Sending an Email

```python
import smtplib

# Set up the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log into your Gmail account (replace with your actual credentials)
server.login("youremail@gmail.com", "yourpassword")

# Sending the email
subject = "Python Email Automation"
body = "Hi there! This email was sent using Python!"
msg = f"Subject: {subject}\n\n{body}"
server.sendmail("youremail@gmail.com", "receiveremail@gmail.com", msg)

print("Email sent!")
server.quit()
```

### What’s Happening Here?
- **`smtplib`** sets up an email server and sends an email with a subject and body.

*Note*: You need to enable **"Less secure app access"** in your Gmail account for this to work.

---

## Mini Project: Automating Birthday Reminders

For this project, we’ll create a simple script that reminds you of upcoming birthdays by sending an email. You can store your friends' birthdays in a file and check if there’s any upcoming birthday today.

---

### Code Example: Birthday Reminder System

```python
import smtplib
from datetime import datetime

birthdays = {
    "Alice": "03-25",
    "Bob": "09-18",
    "Charlie": "12-01"
}

today = datetime.today().strftime("%m-%d")

for friend, bday in birthdays.items():
    if bday == today:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("youremail@gmail.com", "yourpassword")

        subject = "Birthday Reminder"
        body = f"Hey, don't forget to wish {friend} a happy birthday today!"
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail("youremail@gmail.com", "youremail@gmail.com", msg)
        print(f"Reminder sent for {friend}'s birthday!")
        server.quit()
```

### Explanation:
- The script checks if today’s date matches a birthday and sends a reminder email.

---

## Quiz Time! :tada:

Check your understanding of Python’s real-world applications:

1. **What library is used for data analysis in Python?**  
    A. Selenium  
    B. Pandas  
    C. Scikit-learn  

2. **Which Python library is used to automate web browsing?**  
    A. Matplotlib  
    B. smtplib  
    C. Selenium  

3. **What is TensorFlow used for?**  
    A. Web Scraping  
    B. Artificial Intelligence  
    C. Data Visualization  

### Answers:
1. B
2. C
3. B

---

## Further Reading
If you want to dive deeper into these topics, check out:
- [Pandas Documentation](https://pandas.pydata.org/)
- [Selenium Documentation](https://www.selenium.dev/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

Next, we’ll wrap up with **Chapter 7: Final Projects** where you’ll get to build a full Python project from start to finish!

Let me know if you're ready to proceed with the final chapter!