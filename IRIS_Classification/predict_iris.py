import joblib
import numpy as np

# Load trained model
model = joblib.load("iris_logistic_model.pkl")

# Species mapping
species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

print("Enter Iris flower measurements:")

sepal_length = float(input("Sepal length (cm): "))
sepal_width  = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))
petal_width  = float(input("Petal width (cm): "))

# Prepare input
X_new = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict
prediction = model.predict(X_new)[0]

print("\nPredicted Species:",prediction)
