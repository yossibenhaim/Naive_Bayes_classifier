# Naive Bayes Classifier Web App

מערכת אינטראקטיבית לסיווג נתונים מבוססת אלגוריתם Naive Bayes. הפרויקט בנוי כיישום אינטרנט מבוסס FastAPI בצד השרת וממשק
שורת פקודה (CLI) בצד הלקוח. המערכת מאפשרת טעינת נתונים, עיבודם, אימון מודל הסתברותי, בדיקת רמת הדיוק שלו, וביצוע חיזוי
לסיווג שורות חדשות.

---

## 📦 מבנה הפרויקט

```
Naive_Bayes_classifier1/
📁 client/
│   ├── manager.py            # ניהול תקשורת עם השרת והלוגיקה של הלקוח
│   └── menu.py               # תפריט אינטראקטיבי למשתמש
│
📁 probability_server/
│   ├── __init__.py
│   📁 probability_api/
│   │   ├── __init__.py
│   │   └── probability_server.py     # API של שרת המודל לסיווג
│   📁 probability_model/
│       ├── __init__.py
│       └── classified_probability.py # לוגיקה של המודל ומחלקות הסיווג
│
📁 server/
│   ├── __init__.py
│   📁 api/
│   │   ├── __init__.py
│   │   └── server.py                   # API ראשי לניהול הנתונים והמודל
│   📁 data/
│   │   ├── __init__.py
│   │   ├── Cleaning_data.py           # מודול לניקוי ועיבוד נתונים
│   │   ├── load_csv.py                # טעינת קבצי CSV וקריאות לשרת
│   │   📁 storage/
│   │       └── __init__.py
│   📁 model/
│       ├── __init__.py
│       ├── Probability_Classifier.py # מודול המממש את אלגוריתם Naive Bayes
│       └── Test_for_classifier.py    # בדיקות לאלגוריתם הסיווג
│
📁 logs/
│   ├── client.log                    # קובץ לוג של הלקוח
│   ├── classifier_server.log         # קובץ לוג של שרת הסיווג
│   └── main_server.log               # קובץ לוג של השרת הראשי
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
