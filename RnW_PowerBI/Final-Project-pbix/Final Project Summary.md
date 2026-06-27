# 📊 Power BI Sales Dashboard — Complete Project Summary

---

## 🎯 Objectives
1. Build a robust **data model** with **star schema**
2. Use a variety of **DAX formulas and patterns** for measures and KPIs
3. Apply **Time Intelligence**, filtering, and formatting techniques
4. Create a fully interactive **multi-page Power BI report**
5. Ensure **mobile compatibility** and enhanced user experience

---

## 🗄️ Dataset Overview
Tables imported from Excel files:

| Table | Type |
|---|---|
| `Sales_Fact` | Fact Table |
| `Returns_Fact` | Fact Table |
| `Customer_Dim` | Dimension Table |
| `Product_Dim` | Dimension Table |
| `Date_Dim` | Dimension Table |
| `Region_Dim` | Dimension Table |

---

## ✅ Tasks Completed

### 1️⃣ Data Loading & Modeling
- Loaded all tables into Power BI via **Excel file**
- Created relationships using **Primary & Foreign Keys**:
  - `Sales_Fact` → `Customer_Dim` via **CustomerID**
  - `Sales_Fact` → `Returns_Fact` via **OrderID**
  - `Sales_Fact` → `Date_Dim` via **Date**
- Ensured clean **Star Schema** layout and consistent naming conventions
- Hidden unnecessary fields from the report view

---

### 2️⃣ Calculated Columns
| Column | Logic |
|---|---|
| Profit | `SalesAmount - Cost` |
| ReturnFlag | `1 = Returned, 0 = Not Returned` |
| Customer Full Name | `FirstName & " " & LastName` |
| Profit Margin Class | High / Medium / Low classification |
| Year-Month | Formatted date column for sorting |
| Customer Details | Fetched via `RELATED()` |

---

### 3️⃣ DAX Measures
- Total Sales
- Total Cost
- Total Profit
- Return Rate *(using ReturnFlag)*
- Average Sales

**Functions used:** `CALCULATE`, `FILTER`, `ALL`, `SUMX`, `COUNTX`, `AVERAGEX`, `SWITCH`, `RELATED`, `DISTINCTCOUNT`, `SUM`

> 📁 All measures stored in a dedicated **`_Measures`** table for clean organization

---

### 4️⃣ Time Intelligence
- **YTD** Sales
- **YOY** (Year-over-Year) Sales
- **MOM** (Month-over-Month) Sales
- Last Year Sales
- Previous Month Sales & Difference
- Running Total
- Seasonal trend identification

---

### 5️⃣ Dashboard Layout
- **4 Pages:** 1 Main + 2 Detail + 1 Drillthrough
- Visuals used:
  - Cards & KPI Cards
  - Line Charts, Bar Charts, Donut Charts
  - Matrix Visual with Conditional Formatting
  - Trend lines and forecasts
- **Matrix Visual:**
  - Rows: Region, Product Category
  - Columns: Month
  - Values: Total Sales, Profit, Return Rate, Avg Sales
- Top N Products by Sales & Top N Customers by Profit

---

### 6️⃣ Filtering & Interaction
- **Slicers** for: Product, Customer Segment, Region, Date
- Drill Up/Down and **Drillthrough** filters
- **Numeric Range Parameters** for custom filtering
- `ALL()` to remove filters | `FILTER()` for conditional calculations

---

### 7️⃣ Navigation & UX
- **Custom Buttons & Bookmarks** for page navigation
- Collapsible **Slicer Panel**
- **Tooltips** with mini visual summaries
- **Advanced Conditional Formatting** in Matrix/Table views

---

### 8️⃣ Mobile Layout
- Optimized key pages for **mobile viewing**
- Prioritized **KPI Cards** and **Top N visuals**

---

## 🏁 Conclusion
Built a complete, production-ready Power BI model covering proper **data modeling**, **DAX calculations**, **time intelligence**, and **interactive multi-page reporting** — demonstrating a strong and comprehensive understanding of Power BI concepts.
