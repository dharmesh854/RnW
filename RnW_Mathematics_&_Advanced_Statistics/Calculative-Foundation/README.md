# 📊 Calculative Foundation – Linear Algebra on Student Performance Dataset 🎓

## 🎯 Project Overview

This project applies **Linear Algebra concepts** to a real-world student performance dataset containing scores in **Math, Physics, Chemistry, English, and Computer Science**. The goal was to understand how mathematical foundations such as vectors, matrices, decompositions, and dimensionality reduction can be used for data analysis and machine learning.

---

📂 Dataset Information

The project uses a Student Performance Dataset containing academic scores of students across multiple subjects. Each row represents a student, while each column represents a subject score.

📊 Dataset Features
🆔 Student_ID
➗ Math
⚛️ Physics
🧪 Chemistry
📖 English
💻 Computer Science

---

## 🔹 Part A: Vector & Matrix Fundamentals

### 📌 Student Scores as Vectors

* Represented each student's subject scores as a **5-dimensional vector**.
* Visualized score vectors to understand student performance patterns.

### 📏 Vector Operations

Performed:

* ✅ Norm-1 (Manhattan Distance)
* ✅ Norm-2 (Euclidean Distance)
* ✅ Dot Product
* ✅ Angle Between Vectors
* ✅ Cross Product (3 selected subjects)

**Insight:** Similar-performing students produced smaller angles and higher dot products.

### 🎯 Vector Projection

* Projected one student's score vector onto another.
* Measured how much one student's performance aligned with another student's performance pattern.

---

## 🔹 Part B: Matrix Operations

### 🔢 Student–Subject Matrix

Performed:

* ✅ Matrix Addition
* ✅ Matrix Multiplication
* ✅ Matrix Transpose
* ✅ Matrix Inverse
* ✅ Determinant Calculation

**Insight:** Matrix operations provide the foundation for advanced data transformations and machine learning algorithms.

---

## 🔹 Part C: Linear Transformations & Geometry

### 📈 Line, Plane & Hyperplane

Explored geometric representations of the dataset:

* **Line (2D)** ➜ Relationship between two variables.
* **Plane (3D)** ➜ Relationship among three subjects.
* **Hyperplane (5D)** ➜ Represents decision boundaries in higher-dimensional student data.

### 🚀 Dimensionality Growth

Visualized how data evolves:

**2D Line → 3D Plane → 5D Hyperplane**

This demonstrated how increasing the number of features increases data dimensionality.

---

## 🔹 Part D: Eigenvalues & Matrix Decomposition

### 🧮 Eigenvalues & Eigenvectors

Computed:

* ✅ Eigenvalues
* ✅ Eigenvectors

**Insight:** They reveal the principal directions of variance within student scores.

### 🔧 LU Decomposition

Decomposed matrices into:

* L (Lower Triangular Matrix)
* U (Upper Triangular Matrix)

Used for efficient matrix computations.

### ✨ Singular Value Decomposition (SVD)

Performed SVD:

**A = UΣVᵀ**

**Insight:** Identified the most important information within the dataset while reducing complexity.

---

## 🔹 Part E: Dimensionality Reduction

### 📉 Principal Component Analysis (PCA)

Reduced the dataset from multiple subject dimensions to **2 principal components**.

Benefits:

* ✅ Reduced dimensionality
* ✅ Preserved maximum variance
* ✅ Easier visualization

### 🤖 Linear Discriminant Analysis (LDA)

Classified students into:

* 🟢 Above Average
* 🔴 Below Average

**Insight:** LDA found the best linear separation between student performance groups.

---

# 📌 Key Learnings

✅ Represented real-world data using vectors and matrices

✅ Applied norms, dot products, projections, and cross products

✅ Understood matrix transformations and decompositions

✅ Explored eigenvalues and eigenvectors

✅ Implemented LU Decomposition and SVD

✅ Reduced dimensions using PCA

✅ Classified students using LDA

✅ Connected Linear Algebra concepts with Data Science and Machine Learning

---

# 🏆 Conclusion

This project successfully demonstrated how **Linear Algebra serves as the backbone of Data Analytics and Machine Learning**. By transforming student performance data into vectors and matrices, performing mathematical operations, and applying PCA and LDA, meaningful insights were extracted while reducing data complexity. The project bridged theoretical concepts with practical implementation using Python, making abstract mathematical ideas easier to understand and apply in real-world analytics. 🚀📊🎓
