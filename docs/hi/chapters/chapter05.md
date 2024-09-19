# अध्याय 5: Object-Oriented Programming (OOP)

इस अध्याय में, हम Python में **Object-Oriented Programming (OOP)** का अन्वेषण करेंगे। OOP आपके कोड में वास्तविक दुनिया की चीज़ों को मॉडल करने का एक तरीका है। इसे ऐसे समझें जैसे आप वस्तुओं (जैसे कार, जानवर, या लोग) के लिए ब्लूप्रिंट बना रहे हैं!

---

## OOP क्या है?

Python में, **Object-Oriented Programming (OOP)** आपको अपने कोड को **objects** के रूप में संरचित करने की अनुमति देता है। एक **object** वह होता है जिसमें डेटा (attributes) और उस डेटा पर काम करने वाले functions (methods) होते हैं।

OOP के मूल में हैं:
- **Classes**: Objects बनाने के लिए ब्लूप्रिंट।
- **Objects**: किसी class के उदाहरण।
- **Methods**: वे functions जो किसी class से संबंधित होते हैं।
- **Attributes**: वे variables जो किसी class से संबंधित होते हैं।

### वास्तविक जीवन उदाहरण
एक **class** को कार के लिए ब्लूप्रिंट के रूप में सोचें। आप एक ही ब्लूप्रिंट से कई कारें बना सकते हैं, लेकिन प्रत्येक कार एक अलग **object** होती है। ब्लूप्रिंट (class) यह परिभाषित करता है कि दरवाजों की संख्या, रंग, और इंजन का प्रकार क्या होगा (attributes), साथ ही कार क्या कर सकती है, जैसे ड्राइव करना या हॉर्न बजाना (methods)।

---

## Classes और Objects बनाना

आइए एक सरल class बनाते हैं जो एक **Person** का प्रतिनिधित्व करती है।

### कोड उदाहरण: एक Class परिभाषित करना

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, मेरा नाम " + self.name + " है और मैं " + str(self.age) + " साल का/की हूँ।")

# Person class का एक object (instance) बनाना
person1 = Person("Alice", 16)
person1.introduce()
```

### व्याख्या:
- **`class Person:`** एक class **Person** को परिभाषित करता है।
- **`__init__()`** एक विशेष method है जिसे **constructor** कहा जाता है। जब हम एक नया object बनाते हैं, तो यह चालू होता है और attributes को initialize करता है।
- **`self.name`** और **`self.age`** वे attributes हैं जो व्यक्ति के नाम और उम्र को संग्रहीत करते हैं।
- **`introduce()`** एक method है जो व्यक्ति का परिचय देता है।

---

## Methods और Attributes

- **Attributes** object के साथ जुड़े हुए डेटा होते हैं (जैसे किसी व्यक्ति का नाम और उम्र)।
- **Methods** वे functions होते हैं जो किसी object से संबंधित होते हैं (जैसे अपना परिचय देना)।

### कोड उदाहरण: एक Action (Method) जोड़ना

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, मेरा नाम " + self.name + " है और मैं " + str(self.age) + " साल का/की हूँ।")

    def celebrate_birthday(self):
        self.age += 1
        print("जन्मदिन मुबारक हो! अब आप " + str(self.age) + " साल के हो गए हैं।")

# एक नया व्यक्ति बनाना
person2 = Person("Bob", 17)
person2.introduce()
person2.celebrate_birthday()  # उम्र को 1 से बढ़ाता है और जन्मदिन का संदेश प्रिंट करता है
```

### व्याख्या:
- **`celebrate_birthday()`** एक नया method है जो व्यक्ति की उम्र को 1 से बढ़ाता है और जन्मदिन का संदेश प्रिंट करता है।
- आप objects पर methods को कॉल कर सकते हैं ताकि वे कुछ कार्य करें!

---

## Inheritance: Traits पास करना

OOP में, **inheritance** आपको एक class को दूसरी class से attributes और methods विरासत में प्राप्त करने की अनुमति देता है। यह आपको मौजूदा classes का विशेष संस्करण बनाने देता है बिना कोड को फिर से लिखे।

### कोड उदाहरण: `Person` Class से Inherit करना

```python
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Person class के constructor को कॉल करें
        self.grade = grade

    def study(self):
        print(self.name + " कक्षा " + str(self.grade) + " की परीक्षा की तैयारी कर रहे हैं।")

# एक Student object बनाना
student1 = Student("Charlie", 16, 10)
student1.introduce()
student1.study()
```

### व्याख्या:
- **`Student(Person)`**: `Student` class **`Person`** class से **inherit** करता है।
- **`super().__init__(name, age)`** `Person` class के constructor को कॉल करता है ताकि नाम और उम्र को initialize किया जा सके।
- `Student` class में एक अतिरिक्त attribute **grade** और एक नया method **study()** है।

---

## मजेदार उदाहरण: एक Pet को मॉडल करना

आइए एक सरल प्रोग्राम बनाते हैं जो OOP का उपयोग करके एक **Pet** को मॉडल करता है। आप अपने पालतू जानवर को खिलाने, उसके साथ खेलने और उसकी खुशी के स्तर को देख सकते हैं!

### कोड उदाहरण: एक सरल Pet Class

```python
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def feed(self):
        self.happiness += 10
        print(self.name + " खुश हैं! खुशी का स्तर: " + str(self.happiness))

    def play(self):
        self.happiness += 20
        print(self.name + " उत्साहित हैं! खुशी का स्तर: " + str(self.happiness))

# एक Pet object बनाना
my_pet = Pet("Buddy", "dog")
my_pet.feed()
my_pet.play()
```

### यहां क्या हो रहा है?
- **Pet** class में attributes हैं जैसे **name**, **species**, और **happiness**।
- Methods जैसे **feed()** और **play()** पालतू जानवर की खुशी बढ़ाते हैं जब उन्हें कॉल किया जाता है।

---

## मिनी प्रोजेक्ट: सरल Banking System

अब तक हमने जो सीखा है उसका उपयोग करके हम एक **सरल banking system** बनाएंगे। हम एक **BankAccount** class बनाएंगे और उपयोगकर्ताओं को जमा, निकासी और उनके बैलेंस की जांच करने की अनुमति देंगे।

### कोड उदाहरण: Banking System

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} जमा किए गए। नया बैलेंस: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("पर्याप्त धनराशि नहीं है!")
        else:
            self.balance -= amount
            print(f"${amount} निकाले गए। नया बैलेंस: ${self.balance}")

    def check_balance(self):
        print(f"{self.owner} का बैलेंस: ${self.balance}")

# एक बैंक खाता बनाना
account1 = BankAccount("Alice")
account1.deposit(100)
account1.withdraw(50)
account1.check_balance()
```

### व्याख्या:
- **`deposit()`** खाते के बैलेंस को बढ़ाता है।
- **`withdraw()`** बैलेंस को घटाता है यदि पर्याप्त धनराशि उपलब्ध है।
- **`check_balance()`** वर्तमान बैलेंस को दिखाता है।

---

## क्विज़ टाइम! :tada:

अपने OOP ज्ञान की जांच करने के लिए यह क्विज़ आज़माएं:

1. **Python में class क्या है?**  
    A. Objects बनाने के लिए ब्लूप्रिंट  
    B. Functions की एक सूची  
    C. एक प्रकार का loop  

2. **वह विशेष method क्या कहलाता है जो class को initialize करता है?**  
    A. `__init__`  
    B. `start`  
    C. `main`  

3. **किस कीवर्ड का उपयोग दूसरी class से inherit करने के लिए किया जाता है?**  
    A. extend  
    B. inherit  
    C. super  

### उत्तर:
1. A
2. A
3. C

---

## आगे पढ़ने के लिए
यदि आप Python में OOP के बारे में और अधिक जानना चाहते हैं, तो इसे देखें:
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)

---

अगले अध्याय में, हम Python के **वास्तविक दुनिया में अनुप्रयोगों** का अन्वेषण करेंगे, जिसमें यह **data science**, **automation**, और यहां तक कि **artificial intelligence** में कैसे उपयोग किया जाता है, यह जानेंगे!

---