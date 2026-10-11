# Module 1: ML model - predict an employee's salary
# Input : domain, country, years of experience
# Output: predicted salary (USD per year)
# Run   : python ml_model.py

from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (mean_absolute_error, r2_score,
                             accuracy_score, precision_score, recall_score, f1_score)

HIGH_SALARY = 80000    # salary of 80000 or more = "high earner"

# Step 1: load the data
df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "employee_salaries.csv")
print("Step 1: loaded", len(df), "employees")
print(df.head(), "\n")

# Step 2: inputs (X) and answer (y). get_dummies turns words into numbers.
X = pd.get_dummies(df[["domain", "country", "experience_years"]])
y = df["salary_usd"]

# Step 3: split into training data (80%) and test data (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
print("Step 4: model trained\n")

# Step 5: predict the test salaries and compare with the real ones
predicted = model.predict(X_test)
print("Real salary vs predicted salary (first 5 test employees):")
for real, guess in list(zip(y_test, predicted))[:5]:
    print(f"  real: {real:>7}   predicted: {guess:>8.0f}")

# Step 6: regression scores
print("\nREGRESSION SCORES")
print("Average error (MAE):", round(mean_absolute_error(y_test, predicted)), "USD")
print("R2 score           :", round(r2_score(y_test, predicted), 2))

# Step 7: classification scores (is the person a high earner? yes / no)
real_label = y_test >= HIGH_SALARY
predicted_label = predicted >= HIGH_SALARY
print("\nCLASSIFICATION SCORES (high earner: yes / no)")
print("Accuracy :", round(accuracy_score(real_label, predicted_label), 2))
print("Precision:", round(precision_score(real_label, predicted_label, zero_division=0), 2))
print("Recall   :", round(recall_score(real_label, predicted_label, zero_division=0), 2))
print("F1 score :", round(f1_score(real_label, predicted_label, zero_division=0), 2))

# Step 8: same person (Engineering, 5 years) in every country
print("\nPredicted salary for an Engineering employee with 5 years of experience:")
for country in sorted(df["country"].unique()):
    person = pd.DataFrame([{"domain": "Engineering", "country": country, "experience_years": 5}])
    person = pd.get_dummies(person).reindex(columns=X.columns, fill_value=0)
    print(f"  {country:<8}: {model.predict(person)[0]:>8.0f} USD")
