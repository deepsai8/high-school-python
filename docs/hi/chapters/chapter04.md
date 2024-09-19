# अध्याय 4: Functions और Functional Programming

इस अध्याय में, हम सीखेंगे कि Python में **functions** कैसे लिखें ताकि आपका कोड अधिक संगठित और पुन: उपयोग योग्य हो सके। हम **functional programming** की भी एक झलक देखेंगे, जिसमें कुछ शानदार tools जैसे **lambda functions**, **map**, और **filter** का उपयोग करेंगे।

---

## Functions क्या हैं?

Functions आपके कोड के लिए **recipes** की तरह होते हैं। एक ही चीज़ को बार-बार लिखने के बजाय, आप एक function बना सकते हैं और जब भी आपको इसकी आवश्यकता हो, इसे फिर से उपयोग कर सकते हैं। Functions आपके कोड को पढ़ने और प्रबंधित करने में आसान बनाते हैं!

---

### कोड उदाहरण: एक Function को परिभाषित करना

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
```

### व्याख्या:
- **`def greet(name):`** एक function **`greet`** को परिभाषित करता है, जो एक **parameter** **`name`** लेता है।
- जब हम **`greet("Alice")`** कॉल करते हैं, तो function **"Hello, Alice!"** प्रिंट करता है।

### Functions का उपयोग क्यों करें?
Functions आपके कोड को छोटे, प्रबंधनीय हिस्सों में विभाजित करने में मदद करते हैं। कल्पना करें कि आप एक गेम लिख रहे हैं जहां हर एक्शन एक function के अंदर है, और आप जब चाहें उन्हें फिर से उपयोग कर सकते हैं!

---

## Parameters और Return Values

Functions **parameters** (inputs) और **return values** (outputs) ले सकते हैं। Parameters आपको जानकारी पास करने देते हैं, और return values आपको function से कुछ वापस पाने की सुविधा देते हैं।

### कोड उदाहरण: एक सर्कल का क्षेत्रफल निकालना

```python
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area

print(area_of_circle(5))  # 5 की त्रिज्या वाले सर्कल का क्षेत्रफल प्रिंट करता है
```

### व्याख्या:
- **`area_of_circle(radius)`** एक parameter लेता है: सर्कल की त्रिज्या।
- यह **πr²** का उपयोग करके क्षेत्रफल की गणना करता है और **`return`** के साथ परिणाम वापस करता है।

---

## मजेदार उदाहरण: तापमान कनवर्टर

आइए एक function लिखते हैं जो तापमान को Celsius से Fahrenheit में बदलता है।

### कोड उदाहरण: Celsius to Fahrenheit कनवर्टर

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = 25
print(str(temp_c) + "°C is " + str(celsius_to_fahrenheit(temp_c)) + "°F")
```

### यहां क्या हो रहा है?
- **`celsius_to_fahrenheit`** function Celsius को Fahrenheit में बदलता है और Fahrenheit value को return करता है।
- फिर हम परिणाम को प्रिंट करते हैं।

---

## Lambda Functions: Mini Functions ऑन-द-गो

एक **lambda function** एक मिनी-function की तरह होता है जिसे आप एक लाइन में परिभाषित कर सकते हैं। यह तेज़, एक बार के कैलकुलेशन के लिए उपयोगी होता है।

### कोड उदाहरण: एक तेज़ Lambda Function

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12 प्रिंट करता है
```

### व्याख्या:
- **`lambda x, y: x * y`** एक छोटा, अनाम function परिभाषित करता है जो दो संख्याओं को गुणा करता है।
- यह एक पूरा function लिखने के समान है, लेकिन अधिक कॉम्पैक्ट होता है।

---

## Functional Programming Tools: Map, Filter, Reduce

Python में डेटा के साथ काम करने के लिए कुछ शक्तिशाली tools उपलब्ध हैं जो functional programming शैली का उपयोग करते हैं।

### **Map**
**`map()`** function एक function को सूची के हर आइटम पर लागू करता है।

### कोड उदाहरण: `map()` का उपयोग करके संख्याओं का वर्ग करना

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16] प्रिंट करता है
```

### व्याख्या:
- **`map()`** lambda function **`x ** 2`** को सूची की हर संख्या पर लागू करता है।
- परिणाम एक नई सूची है जिसमें मूल संख्याओं के वर्ग होते हैं।

---

### **Filter**
**`filter()`** function सूची से आइटम्स को एक condition के आधार पर फ़िल्टर करता है।

### कोड उदाहरण: `filter()` का उपयोग करके सम संख्याएं प्राप्त करना

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6] प्रिंट करता है
```

### व्याख्या:
- **`filter()`** केवल उन संख्याओं को रखता है जो condition को पूरा करती हैं (इस मामले में, सम होना)।

---

### **Reduce**
**`reduce()`** function एक सूची को एक ही value में कम कर देता है, और इसके लिए आपको इसे **`functools`** मॉड्यूल से आयात करना होगा।

### कोड उदाहरण: `reduce()` का उपयोग करके सभी संख्याओं को गुणा करना

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24 (1*2*3*4) प्रिंट करता है
```

### व्याख्या:
- **`reduce()`** पहले दो संख्याओं को लेता है, उन्हें गुणा करता है, फिर परिणाम को अगली संख्या से गुणा करता है, और इसी तरह।

---

## मिनी प्रोजेक्ट: To-Do List App

अब, हम functions का उपयोग करके एक सरल **to-do list app** बनाएंगे। यह app उपयोगकर्ताओं को tasks जोड़ने, देखने और हटाने की अनुमति देगा।

### कोड उदाहरण: To-Do List App

```python
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

def view_tasks():
    print("आपके tasks:")
    for task in tasks:
        print("- " + task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task हटाया गया: " + task)
    else:
        print("Task नहीं मिला!")

# उदाहरण
add_task("Math टेस्ट की तैयारी")
add_task("किराने का सामान खरीदें")
view_tasks()
remove_task("किराने का सामान खरीदें")
view_tasks()
```

### यहां क्या हो रहा है?
- **`add_task()`** सूची में एक task जोड़ता है।
- **`view_tasks()`** सूची में सभी tasks को प्रिंट करता है।
- **`remove_task()`** यदि task सूची में है तो उसे हटाता है।

---

## क्विज़ टाइम! :tada:

आइए देखें कि आपको functions और functional programming के बारे में कितना समझ में आया:

1. **Python में function को परिभाषित करने के लिए कौन सा कीवर्ड उपयोग किया जाता है?**  
    A. define  
    B. function  
    C. def  

2. **Lambda function क्या करता है?**  
    A. एक पूरा function बनाता है।  
    B. एक मिनी function को एक लाइन में परिभाषित करता है।  
    C. एक function को हटाता है।  

3. **`map()` क्या करता है?**  
    A. दो सूचियों को एक साथ जोड़ता है।  
    B. एक function को सूची के प्रत्येक आइटम पर लागू करता है।  
    C. अनचाहे आइटम्स को फ़िल्टर करता है।  

### उत्तर:
1. C
2. B
3. B

---

## आगे पढ़ने के लिए
यदि आप Python में functions के बारे में और अधिक जानना चाहते हैं, तो इसे देखें:
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

अगले अध्याय में, हम Python में **Object-Oriented Programming (OOP)** पर ध्यान देंगे। आप सीखेंगे कि वास्तविक दुनिया की वस्तुओं को कोड में कैसे मॉडल किया जाता है और अधिक जटिल प्रोजेक्ट्स कैसे बनाए जाते हैं!

---