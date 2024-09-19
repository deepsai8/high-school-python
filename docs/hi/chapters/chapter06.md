# अध्याय 6: Python का वास्तविक दुनिया में उपयोग

Python केवल शुरुआती लोगों के लिए ही नहीं है—इसे विभिन्न उद्योगों में पेशेवरों द्वारा कई रोमांचक अनुप्रयोगों के लिए उपयोग किया जाता है। इस अध्याय में, हम जानेंगे कि Python का उपयोग **data science**, **automation**, **web scraping**, और यहां तक कि **artificial intelligence (AI)** में कैसे किया जाता है। आइए Python के इन मजेदार और व्यावहारिक उपयोगों में गोता लगाते हैं!

---

## Data Science के लिए Python

Data science का मतलब डेटा का विश्लेषण और उसे विज़ुअलाइज़ करके insights प्राप्त करना होता है। Python में शक्तिशाली libraries जैसे **Pandas** और **Matplotlib** हैं जो डेटा के साथ काम करना आसान और मजेदार बनाती हैं!

---

### Pandas का उपयोग: Data का विश्लेषण

**Pandas** library डेटा विश्लेषण के लिए एक स्विस आर्मी नाइफ की तरह है। आप इसमें डेटा को **DataFrames** (इन्हें Excel sheets की तरह समझें) में संग्रहीत कर सकते हैं और आसानी से उनका हेरफेर कर सकते हैं।

### कोड उदाहरण: स्कूल ग्रेड्स का विश्लेषण

```python
import pandas as pd

# छात्रों के ग्रेड्स का एक DataFrame बनाना
data = {
    "Student": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 92, 78, 90],
    "Science": [88, 95, 80, 85]
}

grades = pd.DataFrame(data)
print(grades)

# औसत ग्रेड्स की गणना करना
grades["Average"] = (grades["Math"] + grades["Science"]) / 2
print("\nAverage Grades:")
print(grades)
```

### व्याख्या:
- **`pandas.DataFrame`** आपको डेटा की तालिका बनाने की अनुमति देता है।
- हम प्रत्येक छात्र के औसत ग्रेड्स की गणना करते हैं और उस जानकारी को DataFrame में जोड़ते हैं।

---

### Matplotlib का उपयोग: Data को विज़ुअलाइज़ करना

डेटा को समझना अक्सर तब आसान होता है जब आप इसे विज़ुअलाइज़ करते हैं। **Matplotlib** library आपको सुंदर चार्ट्स और ग्राफ़ बनाने की अनुमति देती है।

### कोड उदाहरण: ग्रेड्स का Bar Chart बनाना

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

### व्याख्या:
- **`plt.bar()`** एक bar chart बनाता है जो प्रत्येक छात्र के math ग्रेड्स को दिखाता है।
- हम x-axis और y-axis के लिए labels और एक शीर्षक जोड़ते हैं।

---

## Web Automation के लिए Python

Python आपके लिए वेब को नियंत्रित भी कर सकता है। आप इसका उपयोग दोहराए जाने वाले कार्यों को स्वचालित करने के लिए कर सकते हैं, जैसे फॉर्म भरना या वेबसाइटों से डेटा स्क्रैप करना।

---

### Selenium का उपयोग: Web Browsing को स्वचालित करना

**Selenium** एक Python library है जो आपको ब्राउज़र गतिविधियों को स्वचालित करने की अनुमति देती है। यह वेबसाइटों पर लॉगिन करने या जानकारी एकत्र करने जैसे कार्यों को स्वचालित करने के लिए परिपूर्ण है।

### कोड उदाहरण: Google सर्च को स्वचालित करना (सरल उदाहरण)

```python
from selenium import webdriver

# ब्राउज़र सेटअप करना
browser = webdriver.Chrome()

# Google का homepage खोलें
browser.get('http://www.google.com')

# Search बॉक्स को इसके name attribute से ढूंढें
search_box = browser.find_element("name", "q")

# सर्च क्वेरी टाइप करें और एंटर दबाएं
search_box.send_keys('Python programming')
search_box.submit()

# ब्राउज़र अब 'Python programming' के सर्च परिणाम दिखाएगा
```

### यहां क्या हो रहा है?
- **Selenium** एक ब्राउज़र खोलता है और Google पर जाता है।
- यह सर्च बॉक्स ढूंढता है, सर्च क्वेरी दर्ज करता है, और सर्च सबमिट करता है।

---

## Artificial Intelligence (AI) के लिए Python

Python **artificial intelligence** के लिए सबसे लोकप्रिय भाषाओं में से एक है। **TensorFlow** और **scikit-learn** जैसी libraries आपको ऐसे मॉडल बनाने की अनुमति देती हैं जो पैटर्न को पहचान सकते हैं, डेटा को वर्गीकृत कर सकते हैं, और यहां तक कि निर्णय भी ले सकते हैं।

---

### Scikit-Learn का उपयोग: एक सरल AI मॉडल बनाना

आइए **scikit-learn** का उपयोग करके एक सरल मॉडल बनाते हैं जो छात्र के ग्रेड्स के आधार पर यह अनुमान लगाता है कि वह पास होगा या फेल।

### कोड उदाहरण: पास/फेल की भविष्यवाणी के लिए सरल AI मॉडल

```python
from sklearn.tree import DecisionTreeClassifier

# डेटा: Math और Science में ग्रेड्स
X = [[85, 88], [92, 95], [78, 80], [90, 85], [60, 55]]
# लेबल्स: 1 पास के लिए, 0 फेल के लिए
y = [1, 1, 1, 1, 0]

# Decision Tree classifier बनाना
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# नए छात्र के लिए पास/फेल की भविष्यवाणी करना
new_student_grades = [[70, 75]]
prediction = clf.predict(new_student_grades)
if prediction == 1:
    print("छात्र पास हो गया!")
else:
    print("छात्र फेल हो गया।")
```

### व्याख्या:
- **DecisionTreeClassifier** एक सरल मॉडल बनाता है जो छात्र के ग्रेड्स के आधार पर पास या फेल की भविष्यवाणी करता है।
- हम इस मॉडल का उपयोग यह अनुमान लगाने के लिए करते हैं कि नया छात्र पास होगा या फेल।

---

## मजेदार उदाहरण: स्वचालित Emails भेजना

आइए कुछ मजेदार स्वचालित करें—Python का उपयोग करके एक email भेजें! हम **smtplib** library का उपयोग करके Gmail खाते से एक email भेजेंगे।

### कोड उदाहरण: एक Email भेजना

```python
import smtplib

# सर्वर सेट करें
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# अपने Gmail खाते में लॉगिन करें (अपने वास्तविक क्रेडेंशियल्स से बदलें)
server.login("youremail@gmail.com", "yourpassword")

# Email भेजना
subject = "Python Email Automation"
body = "नमस्ते! यह ईमेल Python का उपयोग करके भेजा गया है!"
msg = f"Subject: {subject}\n\n{body}"
server.sendmail("youremail@gmail.com", "receiveremail@gmail.com", msg)

print("Email भेजा गया!")
server.quit()
```

### यहां क्या हो रहा है?
- **`smtplib`** एक email सर्वर सेट करता है और एक email भेजता है जिसमें विषय और संदेश होता है।

*ध्यान दें*: इस काम के लिए आपको अपने Gmail खाते में **"कम सुरक्षित ऐप एक्सेस"** सक्षम करना होगा।

---

## मिनी प्रोजेक्ट: Birthday Reminders को स्वचालित करना

इस प्रोजेक्ट के लिए, हम एक सरल स्क्रिप्ट बनाएंगे जो आपको आने वाले जन्मदिनों की याद दिलाएगी। आप अपने दोस्तों के जन्मदिनों को एक फाइल में स्टोर कर सकते हैं और जांच सकते हैं कि आज कोई जन्मदिन है या नहीं।

---

### कोड उदाहरण: Birthday Reminder System

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
        body = f"अरे, आज {friend} को जन्मदिन की शुभकामनाएं देना मत भूलना!"
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail("youremail@gmail.com", "youremail@gmail.com", msg)
        print(f"{friend} के जन्मदिन के लिए Reminder भेजा गया!")
        server.quit()
```

### व्याख्या:
- यह स्क्रिप्ट जांचती है कि क्या आज की तारीख किसी जन्मदिन से मेल खाती है और फिर एक याद दिलाने वाला email भेजती है।

---

## क्विज़ टाइम! :tada:

Python के वास्तविक दुनिया के अनुप्रयोगों के बारे में अपनी समझ की जांच करें:

1. **Python में डेटा विश्लेषण के लिए कौन सी library का उपयोग किया जाता है?**  
    A. Selenium  
    B. Pandas  
    C. Scikit-learn  

2. **कौन सी Python library वेब ब्राउज़िंग को स्वचालित करने के लिए उपयोग की जाती है?**  
    A. Matplotlib  
    B. smtplib  
    C. Selenium  

3. **TensorFlow का उपयोग किसके लिए किया जाता है?**  
    A. Web Scraping  
    B. Artificial Intelligence  
    C. Data Visualization  

### उत्तर:
1. B
2. C
3. B

---

## आगे पढ़ने के लिए
यदि आप इन विषयों में और गहराई से जाना चाहते हैं, तो इसे देखें:
- [Pandas Documentation](https://pandas.pydata.org/)
- [Selenium Documentation](https://www.selenium.dev/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

अगले अध्याय में, हम **Chapter 7: Final Projects** में एक पूरा Python प्रोजेक्ट बनाने के लिए आपको चरण-दर-चरण मार्गदर्शन करेंगे!

---