# 🏛️ EstateIQ

### Real Estate Analytics & Property Valuation Platform

<p align="center">
  <strong>From raw property listings to market intelligence and ML-powered valuation.</strong>
</p>

<p align="center">
  <a href="https://estateiq-real-estate-analytics-aygg3xukbui6tevqxrrts3.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DASHBOARD-Visit%20EstateIQ-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Dashboard">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQL-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQL">
  <img src="https://img.shields.io/badge/ML-Random%20Forest-2F6BFF?style=flat-square" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Visualization-Plotly%20%7C%20Seaborn-4B8BBE?style=flat-square" alt="Visualization">
</p>

---

## ✦ Overview

**EstateIQ** is an end-to-end real-estate analytics and machine-learning project built around **22,139 property records across 17 locations and 8 property categories**.

The project goes beyond simply training a prediction model. It combines **data cleaning, exploratory analysis, SQL market intelligence, statistical analysis, machine learning, model interpretation, and an interactive Streamlit dashboard** into one complete workflow.

> **Data Quality → EDA → SQL → Business Insights → ML → Valuation → Dashboard**

---

## 🚀 Live Application

### Explore EstateIQ in the browser

<p align="center">
  <a href="https://estateiq-real-estate-analytics-aygg3xukbui6tevqxrrts3.streamlit.app/">
    <img src="https://img.shields.io/badge/OPEN%20LIVE%20APPLICATION-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Open Live Application">
  </a>
</p>

The deployed dashboard brings the project's analytical and machine-learning components together in one interface.

**Available in the dashboard:**

- Market overview and supply analysis
- City-level pricing
- Property-type analysis
- Area and price relationships
- Bedroom-level analysis
- EDA-driven market insights
- Interactive property valuation
- Model performance
- Feature importance

**[→ Launch EstateIQ Live Dashboard](https://estateiq-real-estate-analytics-aygg3xukbui6tevqxrrts3.streamlit.app/)**

---

## 📊 Project at a Glance

| Dataset | Market Coverage | Model | Validation |
|:---|:---|:---|:---|
| **22,139** listings | **17** locations | **Random Forest** | **R² 0.6132** |
| **8** property types | Multi-city | Regression | **MAE ₹2,593.72** |
| **0** duplicate IDs | Property-level data | Price / sq.ft. | **RMSE ₹3,948.72** |

---

## 🎯 What the Project Answers

EstateIQ is designed around practical real-estate questions:

- Where is property supply concentrated?
- Which locations have the highest observed price per sq.ft.?
- Which property categories dominate the market?
- How does property size relate to price?
- How does bedroom configuration relate to pricing?
- How does pricing vary across city and property type?
- Which features provide the strongest signals to the valuation model?
- Can property characteristics be used to estimate indicative price per sq.ft.?

---

# 🔎 Key Market Insights

### Supply

**Gurgaon** leads the dataset with **8,486 listings**, followed by **Hyderabad with 5,884**.

### Market Composition

**Residential Apartment** is the dominant category with **16,226 listings**, representing approximately **73.29%** of the dataset.

### Pricing

The dataset shows substantially higher observed median price/sq.ft. levels in several **Mumbai locations** compared with the analyzed **Kolkata markets**.

### Typical Listing

The dataset has a median observed price of approximately **₹9,333/sq.ft.** and a median property area of approximately **1,585 sq.ft.**

---

# 📈 Visual Market Analysis

The project includes a focused collection of presentation-ready visualizations. Each chart is generated independently and stored as a PNG for documentation, portfolio presentation, and README use.

### 01 · Market Supply by City

<p align="center">
  <img src="notebooks/assets/charts/01_market_supply_by_city.png" width="900" alt="Market Supply by City">
</p>

Shows how property listings are distributed across the analyzed locations.

---

### 02 · Median Property Price by City

<p align="center">
  <img src="notebooks/assets/charts/02_median_price_by_city.png" width="900" alt="Median Property Price by City">
</p>

Compares observed median price per square foot across locations.

---

### 03 · Property Market Composition

<p align="center">
  <img src="notebooks/assets/charts/03_property_market_composition.png" width="900" alt="Property Market Composition">
</p>

Highlights the relative size of each property category within the dataset.

---

### 04 · Property Price Distribution

<p align="center">
  <img src="notebooks/assets/charts/04_price_distribution.png" width="900" alt="Property Price Distribution">
</p>

Shows how observed price per square foot is distributed across the dataset.

---

### 05 · Area vs. Price

<p align="center">
  <img src="notebooks/assets/charts/05_area_price_density.png" width="900" alt="Area versus Price">
</p>

Explores the relationship between property area and observed price per square foot.

---

### 06 · Bedroom-Level Market Comparison

<p align="center">
  <img src="notebooks/assets/charts/06_bedroom_market_comparison.png" width="900" alt="Bedroom Market Comparison">
</p>

Compares listing volume and observed median pricing across bedroom configurations.

---

### 07 · City × Property Type Pricing Matrix

<p align="center">
  <img src="notebooks/assets/charts/07_city_property_type_matrix.png" width="900" alt="City Property Type Pricing Matrix">
</p>

Combines location and property category to reveal differences in observed pricing.

---

### 08 · Model Feature Importance

<p align="center">
  <img src="notebooks/assets/charts/08_model_feature_importance.png" width="900" alt="Model Feature Importance">
</p>

Shows the relative contribution of features used by the Random Forest valuation pipeline.

---

# 🧠 Exploratory Data Analysis

The EDA is organized around questions and decisions rather than isolated visualizations.

### Market Structure

**Which location has the largest supply?**

Gurgaon leads the dataset with **8,486 listings**, representing approximately **38.33%** of all observations.

**Which property type dominates?**

Residential Apartment leads with **16,226 listings**, representing approximately **73.29%** of the dataset.

### Pricing

**Where is pricing most expensive?**

Mumbai South West has the highest observed city median at approximately **₹31,111/sq.ft.**, while Kolkata West is the lowest at approximately **₹2,700/sq.ft.**

### Property Configuration

**What is the most common known bedroom configuration?**

**3 BHK** is the largest known bedroom segment, accounting for approximately **46.4%** of records with known bedroom counts.

### Relationship Analysis

**Does larger area automatically mean a higher ₹/sq.ft.?**

Not necessarily. The raw area-price relationship is limited, with a Pearson correlation of approximately **0.11**. This supports using additional property and location features rather than relying on area alone.

---

# 🤖 Machine Learning

## Random Forest Property Valuation

EstateIQ uses a **Random Forest regression pipeline** to estimate an indicative **price per square foot**.

### Model Features

| Feature | Role |
|:---|:---|
| City | Location signal |
| Property Type | Property-category signal |
| Area | Property-size signal |
| Bedrooms | Configuration signal |
| Bathrooms | Configuration signal |
| Balconies | Property attribute |
| Floor | Position signal |
| Total Floors | Building structure signal |

### Valuation Logic

```text
Predicted Price / sq.ft.
            ×
       Property Area
            =
Estimated Property Value
```

### Model Benchmark

| Metric | Result |
|:---|---:|
| Model | **Random Forest** |
| R² | **0.6132** |
| Validation MAE | **₹2,593.72** |
| Validation RMSE | **₹3,948.72** |

These metrics describe model performance on validation data and are not a guarantee of actual market value.

---

# 💡 Model Intelligence

The feature-importance analysis provides an interpretable view of the signals used by the valuation model.

The current model indicates that **location and property structure** are important contributors to predicted price/sq.ft., with **City, Total Floors, Area, and Property Type** among the stronger model signals.

---

# 🗄️ SQL Market Intelligence

EstateIQ uses SQLite to turn the processed dataset into reusable analytical queries.

### Analysis Areas

- Data quality checks
- Price quality checks
- Market analysis
- Location analysis
- Property analysis
- Business insights

### Database

```text
data/estateiq.db
```

### Main Table

```text
estateiq_processed
```

### SQL Modules

```text
sql/
├── 01_data_quality.sql
├── 01b_price_quality.sql
├── 02_market_analysis.sql
├── 03_location_analysis.sql
├── 04_property_analysis.sql
└── 05_business_insights.sql
```

Run an analysis with:

```powershell
python run_sql.py 02_market_analysis.sql
```

---

# 🧹 Data Quality & Preparation

The data preparation stage validates:

- Record counts
- Duplicate property IDs
- Missing analytical fields
- Numeric ranges
- Area validity
- Price validity
- City distribution
- Property-type distribution
- Extreme observations

### Final Validation

```text
22,139 valid AREA records
22,139 valid PRICE_SQFT records
0 duplicate property IDs
```

Area outliers are handled during the cleaning stage. The cleaned `AREA` is then passed into the ML workflow without a second clipping operation.

---

# 🖥️ Interactive Dashboard

The Streamlit application brings market analytics and property valuation together in a single interface.

### Market Analytics

- City-level market supply
- City-level pricing
- Property-type comparison
- Area vs. price analysis
- Bedroom-level analysis
- Price-band analysis
- Interactive Plotly visualizations

### Property Valuation

Users can enter:

```text
City
Property Type
Area
Bedrooms
Bathrooms
Balconies
Floor
Total Floors
```

The model then produces an indicative:

```text
Predicted Price / sq.ft.
          ×
     Property Area
          =
Estimated Property Value
```

### Model Intelligence

The dashboard presents:

- Model performance metrics
- Validation MAE and RMSE
- Explained variation
- Feature importance
- Major model signals

### Try It Live

**[Open the EstateIQ Dashboard →](https://estateiq-real-estate-analytics-aygg3xukbui6tevqxrrts3.streamlit.app/)**

---

# 🔄 End-to-End Workflow

```text
                    RAW PROPERTY DATA
                           │
                           ▼
                DATA CLEANING & VALIDATION
                           │
                           ▼
                 FEATURE PREPARATION
                           │
                           ▼
                  EXPLORATORY ANALYSIS
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
          SQL ANALYTICS        VISUAL ANALYTICS
                │                     │
                └──────────┬──────────┘
                           ▼
                    BUSINESS INSIGHTS
                           │
                           ▼
                  RANDOM FOREST MODEL
                           │
                           ▼
                   PRICE / SQ.FT.
                           │
                           ▼
                  PROPERTY VALUATION
                           │
                           ▼
                 STREAMLIT DASHBOARD
```

---

# 📂 Project Structure

```text
EstateIQ-real-estate-analytics/
│
├── app.py
├── README.md
├── requirements.txt
├── run_sql.py
├── estateiq_database.py
│
├── data/
│   ├── processed/
│   │   └── estateiq_processed.csv
│   └── estateiq.db
│
├── models/
│   └── property_valuation_rf.pkl
│
├── notebooks/
│   ├── estateiq_analysis.ipynb
│   └── assets/
│       └── charts/
│           ├── 01_market_supply_by_city.png
│           ├── 02_median_price_by_city.png
│           ├── 03_property_market_composition.png
│           ├── 04_price_distribution.png
│           ├── 05_area_price_density.png
│           ├── 06_bedroom_market_comparison.png
│           ├── 07_city_property_type_matrix.png
│           └── 08_model_feature_importance.png
│
└── sql/
    ├── 01_data_quality.sql
    ├── 01b_price_quality.sql
    ├── 02_market_analysis.sql
    ├── 03_location_analysis.sql
    ├── 04_property_analysis.sql
    └── 05_business_insights.sql
```

---

# ⚙️ Getting Started

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EstateIQ-real-estate-analytics
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Launch the application

```bash
streamlit run app.py
```

---

# 🗃️ Rebuild the Database

After updating the processed dataset:

```bash
python estateiq_database.py
```

The SQLite database will be created at:

```text
data/estateiq.db
```

---

# 🧰 Technology Stack

| Layer | Technologies |
|:---|:---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Statistics | SciPy, Statsmodels |
| Machine Learning | Scikit-learn, XGBoost |
| Explainability | SHAP |
| Model Persistence | Joblib |
| Database | SQLite |
| Dashboard | Streamlit |
| Notebook | Jupyter |
| Spreadsheet Processing | OpenPyXL |

---

# 📦 Requirements

```text
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
scipy
statsmodels
xgboost
shap
joblib
streamlit
jupyter
openpyxl
```

Install with:

```bash
pip install -r requirements.txt
```

---

# ⚠️ Valuation Disclaimer

EstateIQ is an **analytics and portfolio project**, not a certified property appraisal system.

The model learns patterns from the analyzed dataset and produces an indicative estimate. Actual property prices can vary based on:

- Exact locality
- Building quality
- Property condition
- Amenities
- Road access
- Legal status
- Developer reputation
- Market timing
- Negotiation
- Other micro-location factors

The valuation should therefore be treated as an **analytical estimate**, not a guaranteed transaction price.

---

# 🏁 Project Outcome

EstateIQ demonstrates how real-estate data can be transformed into a complete analytical product:

> **Raw Data → Data Quality → EDA → SQL → Insights → ML → Model Interpretation → Valuation → Dashboard**

The project focuses not only on prediction, but also on **understanding the market, validating the data, communicating findings visually, and delivering an interactive analytical application**.

---

## 👤 Author

### Archi Yadav

**Data Analytics · Python · SQL · Machine Learning · Data Visualization**

---

<p align="center">
  <a href="https://estateiq-real-estate-analytics-aygg3xukbui6tevqxrrts3.streamlit.app/">
    <strong>🚀 Explore the Live EstateIQ Dashboard</strong>
  </a>
</p>

<p align="center">
  Built as a portfolio project focused on practical real-estate analytics and machine learning.
</p>
