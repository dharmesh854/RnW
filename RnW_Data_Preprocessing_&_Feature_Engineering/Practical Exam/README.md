🚕 Ride Demand Forecasting Data Prep Engine
🎯 Project Objective

   - The objective of this project is to create a complete Data Preprocessing & Feature Engineering pipeline for real-world ride-hailing data.
   - The pipeline prepares raw rider, trip, and city-zone data for downstream analytics and predictive modeling.

📂 Datasets Used

   - The project uses three different datasets:

1️⃣ Riders Dataset — CSV

  - File: riders - riders.csv
  - Contains rider-level information such as:

    🆔 rider_id
    👤 name
    🎂 age
    ⚧️ gender
    🏙️ city
    📅 signup_date
    🚕 total_rides
    ❌ cancelled_rides
    ⭐ avg_rating

  - The notebook contains 300 rider records and 9 columns.

2️⃣ Trips Dataset — JSON

  - File: trips.json

  - Contains trip-level information:

    🆔 trip_id
    🧑 rider_id
    📍 zone
    📏 distance_km
    ⏱️ duration_min
    💰 fare_amount
    💳 payment_mode
    📅 ride_date
    🚨 surge_flag

  - The notebook's loaded dataset contains 2,000 trip records and 9 original columns.

3️⃣ City Zones Dataset — SQL

  - File: city_zones.sql
  - Contains zone-level information:

    📍 zone_name
    👥 population_density
    🚦 traffic_index
    🚗 avg_speed_kmph
    🏢 zone_type

  - The SQL data is loaded into SQLite and then converted into a Pandas DataFrame for preprocessing and merging.

🧹 Task 1 — Data Understanding & Loading

  The first stage loads the three different data sources:
  
    CSV → Riders
    JSON → Trips
    SQL → City Zones

  The datasets are inspected using:
  
    head()
    info()
    shape
    descriptive statistics
    missing-value checks
    duplicate checks
    invalid-entry checks
  
  This establishes the structure, data types, and quality of the raw datasets.

🧽 Task 2 — Data Cleaning

  The second stage focuses on improving data quality. The exam requires numeric missing values to be handled with SimpleImputer (mean), categorical missing values using the Most Frequent Strategy, and multivariate numeric missing values using KNN Imputer.
  
  🔢 Numeric Missing Values
  
    The project uses:
  
    SimpleImputer(strategy="mean")
  
    for numeric columns.
  
  🏷️ Categorical Missing Values
  
    Categorical columns are handled using the most frequent value.
  
  🤖 KNN Imputation
  
    KNN Imputer is applied to important trip-related numerical variables:
    
      ⏱️ Trip duration
      📏 Distance
      💰 Fare amount
      📅 Date Cleaning
  
  Inconsistent date formats are converted using:
  
    pd.to_datetime()
    🚫 Unrealistic Values
    
    The project checks for:
    
    Negative fares ❌
    Zero-distance rides that were billed ⚠️
    
    This makes the dataset more suitable for further analysis.

📊 Task 3 — Outlier Handling

  The project applies three different outlier-handling techniques, as required by the exam.

  1️⃣ Z-Score Method

    Z-score is used to detect anomalies in:
    
    💰 fare_amount
    📏 distance_km
    
    A threshold of:
    
    |Z| > 3
    
    is used to identify extreme observations.

  2️⃣ IQR Method

    The Interquartile Range (IQR) method is applied to:
    
    duration_min
    
    The project calculates:
    
    Q1
    Q3
    IQR
    Lower Fence
    Upper Fence
    
    and removes duration outliers.

  3️⃣ Winsorization

    Winsorization is performed using the 5th and 95th percentiles to limit extreme values.
    
    📈 Before vs After Comparison
    
    The project compares:
    
    Mean
    Minimum
    Maximum
    Number of rows
    Number of detected/removed outliers
    
    before and after cleaning.
    
    This helps demonstrate the effect of the preprocessing methods.

  🔄 Task 4 — Data Transformation

    The transformation stage converts and restructures the data for machine-learning use.
    
    🕐 Datetime Features
    
      Datetime information is transformed into:
      
      hour
      day_of_week
      month
      year
      
    🏷️ Categorical Encoding
      - Label Encoding
      
      gender is converted into numerical values:
      
      Female → encoded value
      Male → encoded value
      Other → encoded value
      - One-Hot Encoding
      
      The project applies One-Hot Encoding to:
      
      payment_mode
      zone
      
      This converts categorical values into separate binary columns.
      
      🚦 Ordinal Encoding
      
      Traffic levels are created from traffic_index:
      
      Low < Medium < High
      
      and encoded using:
      
      Low → 0
      Medium → 1
      High → 2
      
      📦 Binning
      
      Customer ride frequency is categorized into:
      
      Low
      Med
      High
      
      based on total_rides.
    
    📉 Skewness Transformation
    
    Three numerical transformations are performed:
    
    Column	Transformation
    fare_amount	Log transformation
    distance_km	Log transformation
    duration_min	Square-root transformation
    
    These transformations help reduce the effect of skewed distributions.

⚖️ Task 5 — Feature Scaling

  The project applies two scaling techniques to numerical trip features.
  
  The selected columns are:
  
  fare_amount
  distance_km
  duration_min
  📏 StandardScaler
  
    StandardScaler transforms numerical variables so that they are centered around a standardized scale.
  
  📐 MinMaxScaler
  
    MinMaxScaler transforms values into a normalized range.
    
    The project compares statistics such as:
    
    Mean
    Median
    Standard deviation
    Minimum
    Maximum
    
  before and after scaling.

🛠️ Task 6 — Feature Construction

  This is one of the most important parts of the project. The notebook creates ML-ready rider and trip features.
  
  🚕 1. avg_ride_distance
  total distance / total trips
  
  Measures the average distance covered per trip.
  
  💰 2. avg_ride_fare
  total fare / total rides
  
  Measures the average fare generated per ride.
  
  ⏰ 3. is_peak_hour
  1 → Peak hour
  0 → Non-peak hour
  
  Peak hours are:
  
  07–09
  18–21
  📅 4. days_since_signup
  
  Calculates the number of days between:
  
  Today − Signup Date
  ❌ 5. ride_cancellation_rate
  
  Calculated as:
  
  cancelled_rides / total_rides
  
  This represents the rider's cancellation ratio.
  
  🚨 6. surge_flag
  
  The project calculates:
  
  fare_per_km = fare_amount / distance_km
  
  Then the 90th percentile of fare_per_km is used as the threshold.
  
  If:
  
  fare_per_km > threshold
  
  then:
  
  surge_flag = 1
  
  otherwise:
  
  surge_flag = 0
  
🗃️ Task 7 — Final Dataset

  The final stage merges the cleaned and enriched datasets.
  
  🔗 Rider + Trip Data
  
  The rider features are merged with the trip data using:
  
  rider_id
  🔗 Trip + Zone Data
  
  Zone information is merged using:
  
  Trips: zone
         ↓
  Zones: zone_name
  
  The final dataset therefore combines:
  
  🚕 Trip information
  +
  👤 Rider information
  +
  📍 Zone information
  +
  ⚙️ Engineered features
  
  The final output is exported as:
  
  📁 final_prepared_rides_dataset.csv
  📊 Final Summary
  
  The project produces a summary comparing:
  
  Rows before vs after cleaning
  Missing values before vs after
  Outliers before vs after
  Number of newly engineered features

⭐ Task 8 — Bonus

  The notebook also includes an optional YData Profiling EDA report section.
  
  📋 Automated EDA Report
  
  The project generates:
  
  📄 rides_eda_report.html
  
  using: ProfileReport()
  
  The report provides automated information about the final dataset.
  
  📊 Visualizations
  
  Two visualizations are included:
  
  📈 Ride Demand by Hour
  🚨 Surge vs No-Surge Trip Patterns
  🧠 Overall Data Preprocessing Pipeline

📌 Key Technologies Used
Technology / Library	Purpose
🐍 Python	Main programming language
🐼 Pandas	Data manipulation
🔢 NumPy	Numerical operations
📊 Matplotlib	Visualization
🎨 Seaborn	Data visualization
📐 SciPy	Statistical operations
🗄️ SQLite	SQL dataset handling
🤖 Scikit-learn	Imputation, encoding & scaling
📋 YData Profiling	Automated EDA

Your notebook imports these core libraries, including NumPy, Pandas, Matplotlib, Seaborn, SciPy, sqlite3, and later Scikit-learn components.

🎯 Final Outcome

The project transforms raw ride-hailing data into a cleaned, transformed, scaled, enriched, and ML-ready dataset.

Final deliverables 📦
🐍 main.ipynb / Practical notebook
📊 final_prepared_rides_dataset.csv
📄 Summary Report
📖 README.md
⭐ Optional rides_eda_report.html
