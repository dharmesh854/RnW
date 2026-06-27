# 📊 Customer Churn Data Profiling Project Summary

## 🎯 Project Overview

This project focuses on analyzing a **Customer Churn Dataset** to understand customer behavior, identify important patterns, and prepare the data for future Machine Learning applications. The project covers the complete data analysis workflow, including data acquisition, cleaning, visualization, and exploratory data analysis (EDA).

---

## 📚 Part A: Fundamentals

### 📝 Data Analysis Concepts

* Learned the meaning and importance of **Data Analysis**.
* Explored the complete **Data Science Project Lifecycle**.
* Framed a **Machine Learning problem statement** to predict customer churn.
* Studied **Tensors** and their role in Data Science and Machine Learning using NumPy examples.

---

## 📥 Part B: Data Acquisition

Data was collected and imported from multiple sources:

✅ Loaded CSV data using **Pandas**

✅ Parsed and analyzed **JSON data**

✅ Connected to a **SQLite Database** and fetched records

✅ Retrieved data from a **REST API** using Requests

This demonstrated how data can be acquired from different real-world sources.

---

## 🧹 Part C: Data Understanding & Cleaning

### 🔍 Data Exploration

Performed initial dataset exploration using:

* `head()`
* `info()`
* `describe()`

### 🛠️ Data Cleaning

* Identified missing values
* Detected duplicate records
* Filled missing values using statistical methods
* Removed duplicate entries
* Dropped irrelevant columns
* Ensured data quality and consistency

This step improved the reliability of the dataset for analysis.

---

## 📊 Part D: Exploratory Data Analysis (EDA)

### 📈 Univariate Analysis

Analyzed individual variables such as:

👤 **Age**

💰 **Income**

🛒 **Purchases**

Visualizations used:

* Histogram
* KDE Plot
* Box Plot

Statistical measures:

* Mean
* Median
* Mode
* Skewness
* Kurtosis

These analyses helped understand data distribution, spread, and outliers.

---

### 👨‍👩‍👧‍👦 Categorical Analysis

Analyzed customer demographics using:

* Gender Distribution
* Countplots
* Bar Charts
* Percentage Distribution

This helped identify customer composition across categories.

---

### 🔗 Bivariate Analysis

Studied relationships between variables:

#### 👤 Gender vs Purchases

* Box Plot
* Violin Plot

#### 💰 Income vs Purchases

* Scatter Plot
* Regression Plot
* Pearson Correlation

These visualizations revealed trends and relationships between customer characteristics and purchasing behavior.

---

### 🌐 Multivariate Analysis

Performed advanced analysis involving multiple variables simultaneously.

#### 🔥 Pair Plot

Analyzed interactions between:

* Age
* Income
* Purchases
* Churn

#### 🌡️ Correlation Heatmap

Visualized correlations among numerical features to identify strong and weak relationships.

#### 🎨 Multi-Variable Scatter Plot

Displayed:

* Income (X-axis)
* Purchases (Y-axis)
* Age (Color)
* Tenure (Bubble Size)

This provided deeper insights into customer behavior patterns.

---

## 📋 Part E: Data Profiling *(Remaining)*

The final step will involve generating an automated profiling report using **YData Profiling / Pandas Profiling**.

The report will summarize:

✅ Missing Values

✅ Descriptive Statistics

✅ Correlations

✅ Data Quality Warnings

✅ Variable Distributions

✅ Dataset Overview

