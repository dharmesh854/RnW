# 📊 Customer Transaction Behavior Analysis Using Statistical Distributions

## 🎯 Project Overview

This project focused on analyzing customer transaction data using statistical distribution models, probability concepts, and data transformation techniques. The objective was to understand transaction patterns, evaluate the distribution of transaction amounts and frequencies, identify unusual transactions, and generate meaningful business insights for decision-making.

The dataset contained transaction details such as transaction ID, customer ID, transaction amount, transaction date, transaction count, region, and transaction status. Using Python and statistical analysis techniques, the project explored both discrete and continuous probability distributions to model customer transaction behavior accurately.

---

## 🛠️ Tools & Technologies Used

🐍 **Python** – Data Analysis & Statistical Modeling
📊 **Pandas & NumPy** – Data Cleaning and Manipulation
📈 **Matplotlib & Seaborn** – Data Visualization
📉 **SciPy** – Probability Distributions & Statistical Tests
📋 **Statsmodels** – Q-Q Plot Analysis and Statistical Modeling

---

## 📋 Project Tasks Performed

### 1️⃣ Bernoulli Distribution Analysis

* Modeled transaction success and failure outcomes using Bernoulli Distribution.
* Analyzed the probability of successful transactions based on transaction status.
* Evaluated transaction occurrence as a binary event (Success = 1, Failure = 0).

### 2️⃣ Binomial Distribution Analysis

* Analyzed weekly transaction counts.
* Estimated the probability of observing a specific number of transactions within a given week.
* Studied customer transaction behavior across multiple trials.

### 3️⃣ Poisson Distribution Modeling

* Modeled the number of transactions occurring per day.
* Determined the average transaction rate (λ).
* Evaluated whether transaction occurrences followed a random event pattern over time.

### 4️⃣ Log-Normal Distribution Analysis

* Examined transaction amounts to determine if they followed a log-normal distribution.
* Analyzed positively skewed transaction values.
* Studied spending behavior and high-value transaction patterns.

### 5️⃣ Power Law Distribution Analysis

* Investigated the presence of extreme transaction amounts.
* Evaluated heavy-tailed behavior within the dataset.
* Identified whether a small number of transactions contributed significantly to overall transaction volume.

### 6️⃣ Q-Q Plot Analysis

* Generated Quantile-Quantile (Q-Q) plots.
* Compared sample data against theoretical normal distributions.
* Assessed normality and identified deviations from expected patterns.

### 7️⃣ Box-Cox Transformation

* Applied Box-Cox Transformation to reduce skewness.
* Stabilized variance across transaction amounts.
* Improved data suitability for statistical modeling and analysis.

### 8️⃣ Z-Score Calculation & Probability Estimation

* Calculated Z-Scores for transaction amounts.
* Identified potential outliers and unusual transactions.
* Computed the probability of transactions exceeding ₹5000 using standard normal distribution techniques.

### 9️⃣ PDF and CDF Visualization

* Generated Probability Density Function (PDF) plots to understand transaction amount distribution.
* Created Cumulative Distribution Function (CDF) plots to analyze cumulative transaction probabilities.
* Interpreted distribution behavior and probability trends.

### 🔟 Best-Fit Distribution Evaluation

* Compared Bernoulli, Binomial, Poisson, Log-Normal, and Power Law distributions.
* Evaluated which statistical model best represented transaction behavior.
* Provided data-driven justification for the selected distribution.

