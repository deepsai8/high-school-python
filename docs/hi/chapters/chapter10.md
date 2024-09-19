# अध्याय 10: मज़ेदार प्रोजेक्ट्स

इस अध्याय में, हम Python के साथ बनाने के लिए कुछ रोमांचक और व्यावहारिक प्रोजेक्ट्स पर काम करेंगे! चाहे आपको गणित, गेम्स, डेटा विश्लेषण, या वेब विकास में दिलचस्पी हो, यहाँ हर किसी के लिए कुछ है। ये प्रोजेक्ट्स छोटे कैलकुलेटर से लेकर जटिल अनुप्रयोगों जैसे कि स्कूल प्रबंधन प्रणाली तक होंगे, जिन्हें समझना आसान और मजेदार बनाने के लिए डिज़ाइन किया गया है।

---

## 1. गणितीय कैलकुलेटर प्रोजेक्ट

सबसे पहले, हम एक **कैलकुलेटर** बनाएंगे जो जोड़, घटाव, गुणा, और भाग जैसे बुनियादी गणितीय कार्य कर सके। यह functions और control flow का अभ्यास करने के लिए एक शानदार तरीका है।

### कोड उदाहरण: बेसिक कैलकुलेटर

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "त्रुटि! शून्य से भाग नहीं किया जा सकता।"
    return x / y

# कैलकुलेटर के लिए मेनू
def calculator():
    print("Python कैलकुलेटर में आपका स्वागत है!")
    print("ऑपरेशन चुनें:")
    print("1. जोड़ें")
    print("2. घटाएं")
    print("3. गुणा करें")
    print("4. भाग करें")

    choice = input("चॉइस दर्ज करें (1/2/3/4): ")

    num1 = float(input("पहला नंबर दर्ज करें: "))
    num2 = float(input("दूसरा नंबर दर्ज करें: "))

    if choice == '1':
        print(f"परिणाम: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"परिणाम: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"परिणाम: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"परिणाम: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("अमान्य इनपुट")

calculator()
```

### व्याख्या:
- यह कैलकुलेटर आपको चार गणितीय ऑपरेशन्स चुनने और दो नंबर दर्ज करने की अनुमति देता है।
- प्रत्येक ऑपरेशन को उसकी खुद की फ़ंक्शन द्वारा नियंत्रित किया जाता है, और भाग फ़ंक्शन में शून्य से भाग की त्रुटि संभाली जाती है।

---

## 2. नंबर गेसिंग गेम

एक मज़ेदार **नंबर गेसिंग गेम** बनाएं, जहाँ कंप्यूटर एक यादृच्छिक नंबर चुनता है, और खिलाड़ी को इसका अनुमान लगाना होता है। प्रोग्राम यह बताता है कि अनुमान बहुत ऊँचा है या बहुत नीचा।

### कोड उदाहरण: नंबर गेसिंग गेम

```python
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("मैं 1 से 100 के बीच एक नंबर सोच रहा हूँ।")

    while True:
        guess = int(input("अपना अनुमान दर्ज करें: "))
        attempts += 1

        if guess < secret_number:
            print("बहुत कम!")
        elif guess > secret_number:
            print("बहुत ज़्यादा!")
        else:
            print(f"बधाई हो! आपने {attempts} प्रयासों में सही अनुमान लगाया!")
            break

guessing_game()
```

### व्याख्या:
- कंप्यूटर 1 से 100 के बीच एक यादृच्छिक संख्या चुनता है।
- खिलाड़ी सही संख्या का अनुमान लगाने तक प्रयास करता है, और प्रोग्राम संकेत देता है कि अनुमान ऊँचा है या नीचा।

---

## 3. रॉक, पेपर, सिज़र्स गेम

चलो एक साधारण गेम **रॉक, पेपर, सिज़र्स** बनाते हैं जहाँ खिलाड़ी कंप्यूटर के खिलाफ प्रतिस्पर्धा करता है।

### कोड उदाहरण: रॉक, पेपर, सिज़र्स

```python
import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("रॉक, पेपर, या सिज़र्स चुनें: ").lower()

    if player_choice not in choices:
        print("अमान्य चॉइस!")
    else:
        print(f"कंप्यूटर ने {computer_choice} चुना")
        if player_choice == computer_choice:
            print("यह एक टाई है!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("आप जीते!")
        else:
            print("आप हारे!")

rock_paper_scissors()
```

### व्याख्या:
- कंप्यूटर रैंडमली रॉक, पेपर, या सिज़र्स चुनता है।
- खिलाड़ी अपनी चाल चुनता है, और प्रोग्राम निर्धारित करता है कि कौन जीता।

---

## 4. पायथन का उपयोग करके स्नेक गेम

हम **Pygame** लाइब्रेरी का उपयोग करके एक साधारण **स्नेक गेम** बनाएंगे। इस गेम में, खिलाड़ी सांप को नियंत्रित करता है और खाना खाने की कोशिश करता है जबकि दीवारों और अपने शरीर से टकराने से बचता है।

### कोड उदाहरण: स्नेक गेम

```python
import pygame
import time
import random

pygame.init()

# स्क्रीन सेटिंग्स
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# रंग
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# स्नेक सेटिंग्स
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
            message = font_style.render("आप हार गए! Q-छोड़ें या C-फिर से खेलें दबाएँ", True, red)
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

### व्याख्या:
- **Pygame** लाइब्रेरी का उपयोग करके खेल की विंडो बनाई जाती है, और स्नेक को ड्रॉ और नियंत्रित किया जाता है।
- खिलाड़ी तीर कुंजियों का उपयोग करके सांप को नियंत्रित करता है और खाना खाने का प्रयास करता है बिना दीवारों से टकराए या अपने शरीर से टकराए।

---

## 5. डेटा विश्लेषण प्रोजेक्ट Pandas और Matplotlib के साथ

हम कुछ **छात्र अंकों** का विश्लेषण करेंगे और **Pandas** और **Matplotlib** का उपयोग करके डेटा को visualize करेंगे।

### कोड उदाहरण: छात्रों के स्कोर का डेटा विश्लेषण

```python
import pandas as pd
import matplotlib.pyplot as plt

# छात्र स्कोर का एक DataFrame बनाएं
data = {
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 92, 78, 90],
    "Science": [88, 95, 80, 85],
    "English": [75, 89, 95, 70]
}
df = pd.DataFrame(data)

# प्रत्येक छात्र के लिए औसत स्कोर की गणना करें
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# DataFrame प्रिंट करें
print(df)

# औसत स्कोर का प्लॉट करें
plt.bar(df["Student"], df["Average"])
plt.title("छात्रों के औसत स्कोर")
plt.xlabel("छात्र")
plt.ylabel("औसत स्कोर")
plt.show()
```

### व्याख्या:
- **Pandas** का उपयोग डेटा को DataFrame में स्टोर करने और औसत स्कोर की गणना करने के लिए किया जाता है।
- **Matplotlib** का उपयोग प्रत्येक छात्र के औसत स्कोर का एक बार चार्ट बनाने के लिए किया जाता है।

---

## 6. Tic-Tac-Toe गेम

एक **Tic-Tac-Toe** गेम बनाएं जहाँ दो खिलाड़ी बोर्ड पर निशान लगाते हैं जब तक कि कोई जीत न जाए या खेल ड्रॉ न हो जाए।

### कोड उदाहरण: Tic-Tac-Toe गेम

```python
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # पंक्तियों, स्तंभों, और विकर्णों की जाँच करें
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
        row = int(input(f"Player {current_player}, row (0-2) दर्ज करें: "))
        col = int(input(f"Player {current_player}, column (0-2) दर्ज करें: "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} जीत गया!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("अमान्य चाल! फिर से प्रयास करें।")

    print("यह एक टाई है!")

tic_tac_toe()
```

### व्याख्या:
- यह गेम दो खिलाड़ियों को बारी-बारी से 3x3 ग्रिड पर एक स्थिति चुनने की अनुमति देता है।
- `check_winner` फ़ंक्शन यह निर्धारित करता है कि क्या खिलाड़ियों में से कोई पंक्ति, स्तंभ, या विकर्ण पूरा करके जीत गया है।

---

## 7. मुद्रा कनवर्टर

एक **मुद्रा कनवर्टर** बनाएं जो विभिन्न मुद्राओं के बीच कनवर्ट करे।

### कोड उदाहरण: मुद्रा कनवर्टर

```python
def currency_converter(amount, from_currency, to_currency):
    conversion_rates = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 110.5,
        "GBP": 0.75
    }

    if from_currency not in conversion_rates or to_currency not in conversion_rates:
        return "अमान्य मुद्रा कोड!"

    converted_amount = amount * conversion_rates[to_currency] / conversion_rates[from_currency]
    return round(converted_amount, 2)

amount = float(input("राशि दर्ज करें: "))
from_currency = input("कौन सी मुद्रा से (USD, EUR, JPY, GBP): ").upper()
to_currency = input("कौन सी मुद्रा में (USD, EUR, JPY, GBP): ").upper()

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} बराबर है {result} {to_currency}")
```

### व्याख्या:
- यह प्रोग्राम एक शब्दकोश का उपयोग करके कनवर्ज़न दरों को संग्रहीत करता है और उपयोगकर्ता इनपुट के आधार पर कनवर्ट की गई राशि की गणना करता है।

---

## 8. स्कूल प्रबंधन प्रणाली (Flask वेब ऐप)

चलो एक साधारण **स्कूल प्रबंधन प्रणाली** बनाते हैं जो आपको छात्रों, कक्षाओं और ग्रेड्स को प्रबंधित करने की अनुमति देता है। यह प्रोजेक्ट **Flask** का उपयोग करता है, जो एक हल्का वेब framework है।

### कोड उदाहरण: साधारण Flask-आधारित स्कूल प्रबंधन प्रणाली

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

### व्याख्या:
- यह Flask एप्लिकेशन आपको छात्रों और उनके ग्रेड्स को जोड़ने, छात्रों की सूची प्रदर्शित करने और छात्रों को सूची से हटाने की अनुमति देता है।
- इस प्रोजेक्ट के लिए **HTML templates** का उपयोग करके front-end (UI) बनाया जा सकता है।

---

## 9. मौसम ऐप (API का उपयोग करके)

एक **मौसम ऐप** बनाएं जो **OpenWeatherMap API** का उपयोग करके किसी शहर के लिए वर्तमान मौसम प्राप्त करता है।

### कोड उदाहरण: मौसम ऐप

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
        print(f"शहर: {city}\nतापमान: {temp}°C\nमौसम: {weather_desc}\nआर्द्रता: {humidity}%")
    else:
        print("शहर नहीं मिला!")

city = input("शहर का नाम दर्ज करें: ")
get_weather(city)
```

### व्याख्या:
- यह प्रोजेक्ट **OpenWeatherMap API** से मौसम डेटा प्राप्त करता है और दिए गए शहर के लिए तापमान, मौसम विवरण और आर्द्रता प्रदर्शित करता है।

---

## 10. Quiz एप्लिकेशन

एक **quiz एप्लिकेशन** बनाएं जो बहुविकल्पीय प्रश्न पूछता है और खिलाड़ी के स्कोर का ट्रैक रखता है।

### कोड उदाहरण: Quiz ऐप

```python
def run_quiz():
    questions = {
        "फ्रांस की राजधानी क्या है?": {"options": ["A) पेरिस", "B) रोम", "C) मैड्रिड"], "answer": "A"},
        "2 + 2 कितना होता है?": {"options": ["A) 3", "B) 4", "C) 5"], "answer": "B"},
        "'1984' पुस्तक किसने लिखी?": {"options": ["A) जॉर्ज ऑरवेल", "B) जे.के. रोलिंग", "C) चार्ल्स डिकेन्स"], "answer": "A"}
    }

    score = 0
    for question

, data in questions.items():
        print(question)
        for option in data["options"]:
            print(option)
        answer = input("आपका उत्तर: ").upper()

        if answer == data["answer"]:
            print("सही!\n")
            score += 1
        else:
            print(f"गलत! सही उत्तर था {data['answer']}\n")

    print(f"आपने {len(questions)} में से {score} सही उत्तर दिए!")

run_quiz()
```

### व्याख्या:
- यह प्रोजेक्ट एक साधारण quiz बनाता है जिसमें बहुविकल्पीय प्रश्न होते हैं और खिलाड़ी के उत्तर सही हैं या नहीं, यह जाँचा जाता है।

---

# प्रोजेक्ट 11: स्कूल प्रबंधन प्रणाली (Flask-आधारित वेब ऐप)

यह प्रोजेक्ट एक **स्कूल प्रबंधन प्रणाली** को सिम्युलेट करेगा जहां आप छात्रों, उनकी कक्षाओं और ग्रेड्स को प्रबंधित कर सकते हैं। हम इसे कई Python फ़ाइलों में विभाजित करेंगे और वेब पेजों को रेंडर करने के लिए टेम्प्लेट भी शामिल करेंगे।

### प्रोजेक्ट संरचना:
```
school_management/
│
├── app.py  (मुख्य Flask एप्लिकेशन)
├── models.py  (छात्र, कक्षाएं और ग्रेड्स प्रबंधित करने के लिए डेटा संरचना)
├── templates/
│   ├── index.html  (होम पेज टेम्पलेट)
│   ├── add_student.html  (नए छात्रों को जोड़ने के लिए फॉर्म)
│   └── student_detail.html  (छात्र की जानकारी के साथ ग्रेड्स)
└── static/
    └── style.css  (वैकल्पिक: CSS स्टाइलिंग के लिए)
```

---

### **फ़ाइल 1: `models.py` (छात्र और कक्षा डेटा संरचना)**

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

### व्याख्या:
- इस फ़ाइल में `Student` क्लास है, जो छात्र डेटा जैसे नाम, आयु, और ग्रेड्स को प्रबंधित करता है।
- इसमें ग्रेड्स जोड़ने और छात्र का औसत ग्रेड गणना करने के लिए फ़ंक्शन हैं।

---

### **फ़ाइल 2: `app.py` (मुख्य Flask एप्लिकेशन)**

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
    return "छात्र नहीं मिला", 404

@app.route('/student/<name>/add_grade', methods=['POST'])
def add_grade(name):
    subject = request.form['subject']
    grade = int(request.form['grade'])
    for student in students:
        if student.name == name:
            student.add_grade(subject, grade)
            return redirect(url_for('student_detail', name=name))
    return "छात्र नहीं मिला", 404

if __name__ == '__main__':
    app.run(debug=True)
```

### व्याख्या:
- यह मुख्य Flask एप्लिकेशन है जो छात्रों को दिखाने, जोड़ने और उनके ग्रेड्स को प्रबंधित करने के लिए रूटिंग करता है।
- `add_student` रूट एक फॉर्म के माध्यम से नए छात्रों को जोड़ने की अनुमति देता है।
- `student_detail` रूट एक विशिष्ट छात्र की विस्तृत जानकारी दिखाता है।
- `add_grade` रूट POST अनुरोध है जो छात्र में नए ग्रेड जोड़ने की अनुमति देता है।

---

### **फ़ाइल 3: `index.html` (होम पेज टेम्पलेट)**

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>स्कूल प्रबंधन प्रणाली</title>
</head>
<body>
    <h1>स्कूल प्रबंधन प्रणाली</h1>
    <h2>छात्र सूची</h2>
    <ul>
        {% for student in students %}
            <li><a href="{{ url_for('student_detail', name=student.name) }}">{{ student.name }}</a> (आयु: {{ student.age }})</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('add_student') }}">नया छात्र जोड़ें</a>
</body>
</html>
```

### व्याख्या:
- यह होम पेज है जो छात्रों की सूची प्रदर्शित करता है। प्रत्येक छात्र का नाम लिंक है जो उनके विस्तृत दृश्य की ओर ले जाता है।
- एक लिंक भी है जो नए छात्रों को जोड़ने की अनुमति देता है।

---

### **फ़ाइल 4: `add_student.html` (छात्र जोड़ने के लिए फॉर्म)**

```html
<!-- templates/add_student.html -->
<!DOCTYPE html>
<html>
<head>
    <title>नया छात्र जोड़ें</title>
</head>
<body>
    <h1>नया छात्र जोड़ें</h1>
    <form method="POST">
        <label for="name">नाम:</label>
        <input type="text" name="name" required><br><br>
        <label for="age">आयु:</label>
        <input type="text" name="age" required><br><br>
        <input type="submit" value="छात्र जोड़ें">
    </form>
</body>
</html>
```

### व्याख्या:
- यह पेज एक साधारण फॉर्म प्रदान करता है जहां उपयोगकर्ता नाम और आयु दर्ज करके नया छात्र जोड़ सकते हैं।

---

### **फ़ाइल 5: `student_detail.html` (छात्र की जानकारी के साथ ग्रेड्स)**

```html
<!-- templates/student_detail.html -->
<!DOCTYPE html>
<html>
<head>
    <title>छात्र जानकारी</title>
</head>
<body>
    <h1>{{ student.name }} की जानकारी</h1>
    <p>आयु: {{ student.age }}</p>
    <h3>ग्रेड्स:</h3>
    <ul>
        {% for subject, grade in student.grades.items() %}
            <li>{{ subject }}: {{ grade }}</li>
        {% endfor %}
    </ul>
    <p>औसत ग्रेड: {{ student.get_average_grade() }}</p>

    <h3>ग्रेड जोड़ें</h3>
    <form method="POST" action="{{ url_for('add_grade', name=student.name) }}">
        <label for="subject">विषय:</label>
        <input type="text" name="subject" required><br><br>
        <label for="grade">ग्रेड:</label>
        <input type="number" name="grade" required><br><br>
        <input type="submit" value="ग्रेड जोड़ें">
    </form>

    <a href="{{ url_for('home') }}">होम पर वापस जाएं</a>
</body>
</html>
```

### व्याख्या:
- यह पेज एक छात्र की विस्तृत जानकारी दिखाता है, जिसमें उनके विषयों और ग्रेड्स की सूची होती है।
- यहां एक फॉर्म भी है जो विशेष छात्र के लिए नए ग्रेड जोड़ने की अनुमति देता है।

---

### **फ़ाइल 6: `style.css` (वैकल्पिक CSS स्टाइलिंग)**

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

### व्याख्या:
- आप इस वेब ऐप को सुंदर बनाने के लिए वैकल्पिक CSS जोड़ सकते हैं।

---

### प्रोजेक्ट को चलाने का तरीका:
1. **Flask** इंस्टॉल करें: `pip install flask` कमांड चलाएं।
2. प्रोजेक्ट संरचना और फाइलें बनाएं।
3. एप्लिकेशन को चलाएं: `python app.py` कमांड चलाएं।
4. अपने ब्राउज़र में `http://127.0.0.1:5000/` खोलें।

---

# प्रोजेक्ट 12: एडवांस्ड क्विज़ एप्लिकेशन

यह प्रोजेक्ट एक **क्विज़ गेम** है जहां उपयोगकर्ता बहुविकल्पीय प्रश्नों का उत्तर देता है। यह उनके स्कोर का ट्रैक रखता है और क्विज़ के बाद फीडबैक देता है।

### प्रोजेक्ट संरचना:
```
quiz_app/
│
├── app.py  (मुख्य क्विज़ एप्लिकेशन)
├── questions.py  (प्रश्न डेटा)
└── templates/
    ├── index.html  (स्टार्ट स्क्रीन)
    ├── quiz.html  (क्विज़ स्क्रीन)
    └── result.html  (रिजल्ट स्क्रीन)
```

---

### **फ़ाइल 1: `questions.py` (प्रश्न डेटा)**

```python
# questions.py
questions = [
    {
        "question": "फ्रांस की राजधानी क्या है?",
        "options": ["A) पेरिस", "B) लंदन", "C) बर्लिन"],
        "answer": "A"
    },
    {
        "question": "'1984' पुस्तक किसने लिखी?",
        "

options": ["A) जॉर्ज ऑरवेल", "B) मार्क ट्वेन", "C) जे.के. रोलिंग"],
        "answer": "A"
    },
    {
        "question": "2 + 2 क्या होता है?",
        "options": ["A) 3", "B) 4", "C) 5"],
        "answer": "B"
    }
]
```

### व्याख्या:
- यह फ़ाइल प्रश्नों की सूची है, जिसमें प्रत्येक प्रश्न में बहुविकल्पीय उत्तर और सही उत्तर शामिल हैं।

---

### **फ़ाइल 2: `app.py` (मुख्य क्विज़ एप्लिकेशन)**

```python
# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from questions import questions

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

@app.route('/')
def index():
    session['score'] = 0  # स्कोर रीसेट करें
    session['question_number'] = 0  # पहले प्रश्न से शुरुआत करें
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

### व्याख्या:
- क्विज़ की शुरुआत पहले प्रश्न से होती है।
- खिलाड़ी के स्कोर को session में संग्रहीत किया जाता है, और प्रत्येक उत्तर को सही उत्तर से मिलान किया जाता है।
- सभी प्रश्नों के उत्तर देने के बाद उपयोगकर्ता को रिजल्ट पेज पर भेजा जाता है जहां वे अपना स्कोर देख सकते हैं।

---

### **फ़ाइल 3: `index.html` (स्टार्ट स्क्रीन)**

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>क्विज़ गेम</title>
</head>
<body>
    <h1>क्विज़ गेम में आपका स्वागत है!</h1>
    <p>कुछ मजेदार प्रश्नों के साथ अपने ज्ञान का परीक्षण करें!</p>
    <a href="{{ url_for('quiz') }}">क्विज़ शुरू करें</a>
</body>
</html>
```

### व्याख्या:
- यह होम पेज है जहां उपयोगकर्ता **क्विज़ शुरू करें** बटन पर क्लिक करके क्विज़ शुरू कर सकते हैं।

---

### **फ़ाइल 4: `quiz.html` (क्विज़ स्क्रीन)**

```html
<!-- templates/quiz.html -->
<!DOCTYPE html>
<html>
<head>
    <title>क्विज़ गेम</title>
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
        <input type="submit" value="उत्तर दें">
    </form>
</body>
</html>
```

### व्याख्या:
- यह पेज प्रत्येक प्रश्न और इसके विकल्पों को डायनामिक रूप से दिखाता है।
- खिलाड़ी अपना उत्तर चुनते हैं और इसे सबमिट करते हैं।

---

### **फ़ाइल 5: `result.html` (रिजल्ट स्क्रीन)**

```html
<!-- templates/result.html -->
<!DOCTYPE html>
<html>
<head>
    <title>क्विज़ रिजल्ट</title>
</head>
<body>
    <h1>क्विज़ रिजल्ट</h1>
    <p>आपने {{ total_questions }} में से {{ score }} सही उत्तर दिए!</p>
    <a href="{{ url_for('index') }}">पुनः खेलें</a>
</body>
</html>
```

### व्याख्या:
- यह पेज अंतिम स्कोर को दिखाता है और खिलाड़ी को क्विज़ को फिर से खेलने का विकल्प देता है।

---

### प्रोजेक्ट को चलाने का तरीका:
1. **Flask** इंस्टॉल करें: `pip install flask` कमांड चलाएं।
2. प्रोजेक्ट संरचना और फाइलें बनाएं।
3. एप्लिकेशन को चलाएं: `python app.py` कमांड चलाएं।
4. अपने ब्राउज़र में `http://127.0.0.1:5000/` खोलें।

---

ये प्रोजेक्ट अधिक जटिल सिस्टम बनाने का अवसर प्रदान करते हैं जबकि उन्हें समझने और लागू करने में आसान बनाते हैं। यदि आपको और समायोजन या अतिरिक्त जानकारी की आवश्यकता है, तो मुझे बताएं!

---

### अंतिम विचार:

ये 10 प्रोजेक्ट गेम्स, एप्लिकेशन, और डेटा विश्लेषण उपकरणों का मिश्रण प्रदान करते हैं जो मज़ेदार, आकर्षक और शैक्षिक हैं। प्रत्येक प्रोजेक्ट छात्रों द्वारा सीखे गए कौशल को मजबूत करता है और Python सीखने को रोमांचक बनाने के लिए एक रचनात्मक तत्व जोड़ता है! 