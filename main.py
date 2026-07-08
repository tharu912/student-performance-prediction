import pandas as pd

# Load Dataset
df = pd.read_csv("student_performance_dataset.csv")

# Remove Student ID
df = df.drop("Student_ID", axis=1)

# Convert text columns to numbers
df = pd.get_dummies(df, drop_first=True)

# Features and Target
X = df.drop(["Final_Exam_Score", "Pass_Fail_Pass"], axis=1)
print(X.columns)
y = df["Final_Exam_Score"]

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Linear Regression
# ==========================
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

lr = LinearRegression()

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_score = r2_score(y_test, lr_pred)

print("\nLinear Regression R2 Score =", lr_score)

# ==========================
# Decision Tree
# ==========================
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

dt_score = r2_score(y_test, dt_pred)

print("Decision Tree R2 Score =", dt_score)

# ==========================
# Random Forest
# ==========================
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

rf_score = r2_score(y_test, rf_pred)

print("Random Forest R2 Score =", rf_score)
import joblib

joblib.dump(rf, "student_performance_model.pkl")

print("Model Saved Successfully")

# ==========================
# Actual vs Predicted
# ==========================

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "LinearRegression": lr_pred,
    "DecisionTree": dt_pred,
    "RandomForest": rf_pred
})

print("\nFirst 10 Predictions:")
print(comparison.head(10))
import matplotlib.pyplot as plt

importance = rf.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance_df)