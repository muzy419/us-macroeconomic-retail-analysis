# us-macroeconomic-retail-analysis
A quantitative Python project analyzing multi-variate economic indicators to forecast retail demand shifts and establish leading consumer metrics.
#  U.S. Macroeconomic Retail Sales & Consumer Demand Analysis

##  Project Overview
This project delivers a quantitative time-series analysis evaluating how macroeconomic forces—specifically inflation (`CPI`), unemployment rates (`UNRATE`), and consumer sentiment (`UMCSENT`)—impact U.S. advance retail sales (`RSXFS`). 

By building an end-to-end Python pipeline using live data from the **Federal Reserve Economic Data (FRED)** API, this analysis models consumer demand shifts, identifies leading consumer indicators, and evaluates purchasing power elasticity.

---

##  Tech Stack & Dependencies
* **Language:** Python
* **Data Source:** Federal Reserve Bank of St. Louis (FRED API)
* **Libraries:** `pandas`, `pandas-datareader`, `matplotlib`, `seaborn`

---

## Analytical Pipeline
1. **Automated Ingestion:** Live extraction of time-series macroeconomic indicators from FRED API.
2. **Feature Engineering:** Calculated Year-over-Year (YoY) percentage growth rates and 3-month rolling averages for trend smoothing.
3. **Correlation Analysis:** Generated parametric correlation matrices to evaluate elasticity between retail volume and macro variables.
4. **Data Visualization:** Built a multi-panel analytics dashboard displaying YoY trend trajectories, moving average comparisons, and correlation heatmaps.

---

## Macroeconomic Analytics Dashboard
![Macroeconomic Analytics Dashboard](macro_dashboard.png)

---

## Key Findings
* **Inflation Elasticity:** Retail sales growth shows distinct lag responses relative to CPI inflation spikes.
* **Sentiment Indicator:** The Consumer Sentiment Index serves as a strong leading indicator for non-essential retail expenditure shifts.
* **Labor Market Correlation:** Low unemployment strongly sustains nominal retail sales momentum even during periods of elevated consumer prices.

---
