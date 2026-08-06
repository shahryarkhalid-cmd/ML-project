# Iris Flower Classification — Logistic Regression

A simple machine learning project that classifies Iris flowers into their species using **Logistic Regression**.

## 📌 Overview

This project uses the classic **Iris dataset** to build a multi-class classification model. Logistic Regression is trained to predict the species of an Iris flower based on four features: sepal length, sepal width, petal length, and petal width.

## 📊 Dataset

The Iris dataset contains 150 samples across 3 species:
- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

**Features:**
| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal (cm) |
| Sepal Width | Width of the sepal (cm) |
| Petal Length | Length of the petal (cm) |
| Petal Width | Width of the petal (cm) |

**Target:** Species (setosa, versicolor, virginica)

## 🛠️ Tech Stack

- Python
- scikit-learn
- pandas
- NumPy
- Matplotlib / Seaborn (for visualization)

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python main.py
```

Or open the notebook:

```bash
jupyter notebook iris_logistic_regression.ipynb
```

## 🧠 Model

- **Algorithm:** Logistic Regression (multi-class, using `sklearn.linear_model.LogisticRegression`)
- **Train/Test Split:** 80/20
- **Evaluation Metrics:** Accuracy, Confusion Matrix, Classification Report

## 📈 Results

| Metric | Score |
|---|---|
| Accuracy | ~95–100% |
| Precision | High across all classes |
| Recall | High across all classes |

*(Update these numbers with your actual results.)*

## 📁 Project Structure

```
├── data/
│   └── iris.csv
├── notebooks/
│   └── iris_logistic_regression.ipynb
├── main.py
├── requirements.txt
└── README.md
```

## 📌 Future Improvements

- Try other models (SVM, Random Forest) for comparison
- Add hyperparameter tuning (GridSearchCV)
- Deploy as a simple API using FastAPI

## 👤 Author

**Shahryar Khalid**
Data Science & CS Student, Punjab University

## 📄 License

This project is licensed under the MIT License.
