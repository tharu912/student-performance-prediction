# 🎓 Student Performance Prediction System

## 📌 Project Overview

The Student Performance Prediction System is a Machine Learning web application that predicts a student's final exam performance and pass/fail status based on academic and demographic factors.

The project helps identify students who may be at academic risk and enables early intervention through data-driven insights.

---

## 🚀 Features

* Predicts Final Exam Score
* Predicts Pass/Fail Status
* User-friendly Web Interface using Flask
* Real-time Predictions
* PDF Report Generation
* Prediction History Storage using SQLite
* Data Visualization and Analysis
* Machine Learning Model Integration

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib

### Web Framework

* Flask

### Database

* SQLite

### Frontend

* HTML
* CSS
* Bootstrap

---

## 📊 Dataset Information

The dataset contains 708 student records and 10 attributes:

| Feature                    | Description                 |
| -------------------------- | --------------------------- |
| Student_ID                 | Unique student identifier   |
| Gender                     | Male/Female                 |
| Study_Hours_per_Week       | Weekly study hours          |
| Attendance_Rate            | Attendance percentage       |
| Past_Exam_Scores           | Previous exam scores        |
| Parental_Education_Level   | Parent education level      |
| Internet_Access_at_Home    | Internet availability       |
| Extracurricular_Activities | Participation in activities |
| Final_Exam_Score           | Target score                |
| Pass_Fail                  | Pass or Fail                |

---

## 🤖 Machine Learning Models Evaluated

### Regression Models

| Model                   | R² Score |
| ----------------------- | -------- |
| Linear Regression       | 0.652    |
| Decision Tree Regressor | 0.662    |
| Random Forest Regressor | 0.797    |

### Classification Model

* Random Forest Classifier
* Accuracy: 91.5%

### Confusion Matrix

|             | Predicted Fail | Predicted Pass |
| ----------- | -------------- | -------------- |
| Actual Fail | 61             | 10             |
| Actual Pass | 2              | 69             |

---

## 📈 Model Performance

The Random Forest model was selected as the final model because it achieved the highest prediction accuracy and better generalization compared to other models.

* Regression R² Score: 0.80
* Classification Accuracy: 91.5%

---

## 📂 Project Structure

```text
Student_Performance_Project/
│
├── app.py
├── train_model.py
├── student_performance_model.pkl
├── prediction_history.db
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── reports/
│   └── pdf_reports/
│
├── dataset/
│   └── student_performance.csv
│
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/student-performance-prediction.git
```

### Navigate to Project Folder

```bash
cd student-performance-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🌐 Application Workflow

1. User enters student details.
2. Data is processed and validated.
3. Machine Learning model predicts:

   * Final Exam Score
   * Pass/Fail Status
4. Results are displayed instantly.
5. Prediction details are stored in SQLite database.
6. PDF report is generated for download.

---

## 💡 Future Enhancements

* Student Dashboard
* Admin Login System
* Data Analytics Dashboard
* Email Notification System
* Cloud Deployment
* Advanced Performance Reports

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Data Preprocessing
* Exploratory Data Analysis
* Machine Learning Model Development
* Model Evaluation
* Flask Web Development
* Database Management using SQLite
* PDF Report Generation
* Deployment and Version Control using Git & GitHub

---

## 👨‍💻 Author

**Tharani M**

B.E. Computer Science Engineering

VV College of Engineering

Aspiring Python & Django Developer

GitHub: https://github.com/Tharu912

---

## 📜 License

This project is created for educational and learning purposes.

