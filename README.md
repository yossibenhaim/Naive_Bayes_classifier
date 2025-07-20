# Naive Bayes Classifier Web App

מערכת אינטראקטיבית לסיווג נתונים מבוססת אלגוריתם Naive Bayes. הפרויקט בנוי כיישום אינטרנט מבוסס FastAPI בצד השרת וממשק שורת פקודה (CLI) בצד הלקוח. המערכת מאפשרת טעינת נתונים, עיבודם, אימון מודל הסתברותי, בדיקת רמת הדיוק שלו, וביצוע חיזוי לסיווג שורות חדשות.

---

## 📦 מבנה הפרויקט

```

📁 Naive_Bayes_classifier
├── 📁 client
│   ├── manager.py # Handles user interaction with the server
│   └── menu.py # CLI menu system to access model features
│
├── 📁 server
│   ├── 📁 api
│   │   ├── server.py # FastAPI application with endpoints
│   │   └── init.py
│   │
│   ├── 📁 data
│   │   ├── Cleaning_data.py # Set index column
│   │   ├── load_csv.py # Load, save and read CSV and probability files
│   │   └── init.py
│   │
│   ├── 📁 model
│   │   ├── Probability_Classifier.py # Training: builds probability dict
│   │   ├── Test_for_classifier.py # Testing: checks and evaluates prediction
│   │   └── init.py
│   │
│   └── init.py
│
├── 📁 storage
│   ├── data.csv # Stored CSV data
│   └── probability.json # Saved probability dictionary
│
└── README.md (you are here)
```

---

## 🎯 תכונות עיקריות

- טעינת קובץ CSV ישירות מהמשתמש.
- בחירת עמודה שתהיה העמודה המנבאת (index).
- יצירת מודל הסתברותי מסוג Naive Bayes.
- בדיקת דיוק המודל על הדאטה הקיים.
- חיזוי וסיווג שורות חדשות לפי המודל.
- ממשק שורת פקודה ידידותי.
- שימוש ב־FastAPI כשרת אינטרנט קל ויעיל.

---

## ⚙️ איך מפעילים?

### 1. התקנת דרישות:
```bash
pip install -r requirements.txt
```
אם אין לך `requirements.txt`, תוכל גם כך:
```bash
pip install fastapi pandas uvicorn requests
```

### 2. הרצת השרת (בתוך תיקיית `server/` או מהפרויקט הראשי):
```bash
uvicorn server.server:app --reload
```

### 3. הרצת צד הלקוח (תפריט):
```bash
python menu.py
```

---

## 🗂 קבצים הנשמרים אוטומטית

- `data.csv`: הנתונים לאחר טעינה/עיבוד.
- `probability.json`: מילון הסתברויות מאימון המודל.

---

## 🧪 דוגמת שימוש

1. בחר "Load CSV file" והזן את הנתיב לקובץ שלך.
2. בחר "Clean data" ובחר את עמודת הסיווג.
3. בחר "Train classifier" כדי לאמן את המודל.
4. בחר "Test classification" לצורך חישוב דיוק.
5. בחר "Check classification" לסיווג שורה חדשה שתזין.

---

## 👨‍💻 נבנה על ידי

- יוסי בן חיים
- פרויקט לימודי - Naive Bayes Python + FastAPI

---

## ✅ רעיונות להמשך פיתוח

- ממשק גרפי עם Streamlit.
- תמיכה ב־multiple CSVs.
- שמירת לוג תחזיות ודיוקים.
- תמיכה בפרמטרי smoothing.

בהצלחה! 🚀
