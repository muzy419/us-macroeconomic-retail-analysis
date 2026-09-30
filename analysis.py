# ==============================================================================
# U.S. MACROECONOMIC RETAIL SALES & CONSUMER DEMAND ANALYSIS
# Domain: Quantitative Economics & Time-Series Data Analytics
# Tech Stack: Python (pandas, pandas_datareader, matplotlib, seaborn)
# ==============================================================================

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# ------------------------------------------------------------------------------
# 1. AUTOMATED DATA INGESTION (FRED API)
# ------------------------------------------------------------------------------
print("Fetching real-time macroeconomic indicators from St. Louis FRED...")

start_date = datetime.datetime(2018, 1, 1)
end_date = datetime.datetime.now()

# Map FRED Tickers to clean variable names
tickers = {
    'RSXFS': 'Retail_Sales',        # Advance Retail Sales ($ Millions)
    'CPIAUCNS': 'CPI_Inflation',     # Consumer Price Index (Inflation)
    'UNRATE': 'Unemployment_Rate',   # Civil Unemployment Rate (%)
    'UMCSENT': 'Consumer_Sentiment'  # Consumer Sentiment Index
}

# Fetch time-series data
df = web.DataReader(list(tickers.keys()), 'fred', start_date, end_date)
df.rename(columns=tickers, inplace=True)

# ------------------------------------------------------------------------------
# 2. FEATURE ENGINEERING & METRIC CALCULATION
# ------------------------------------------------------------------------------
print("Performing feature engineering (YoY % changes & moving averages)...")

# Calculate Year-over-Year (YoY) Percentage Growth Rates
df['Retail_YoY'] = df['Retail_Sales'].pct_change(12) * 100
df['CPI_YoY'] = df['CPI_Inflation'].pct_change(12) * 100

# Calculate 3-Month Moving Average for Trend Smoothing
df['Retail_3M_MA'] = df['Retail_YoY'].rolling(window=3).mean()

# Clean dataset
df_clean = df.dropna().copy()

# ------------------------------------------------------------------------------
# 3. STATISTICAL CORRELATION ANALYSIS
# ------------------------------------------------------------------------------
print("\n--- Correlation Matrix with Retail Sales YoY Growth ---")
correlations = df_clean[['Retail_YoY', 'CPI_YoY', 'Unemployment_Rate', 'Consumer_Sentiment']].corr()
print(correlations['Retail_YoY'])

# ------------------------------------------------------------------------------
# 4. MULTI-PANEL ANALYTICS DASHBOARD GENERATION
# ------------------------------------------------------------------------------
print("\nGenerating visual analytics dashboard...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10), dpi=300)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# Panel 1: Retail Sales YoY vs CPI Inflation YoY
axes[0, 0].plot(df_clean.index, df_clean['Retail_YoY'], label='Retail Sales YoY (%)', color='#005f73', linewidth=2)
axes[0, 0].plot(df_clean.index, df_clean['CPI_YoY'], label='CPI Inflation YoY (%)', color='#ca6702', linestyle='--', linewidth=2)
axes[0, 0].axhline(0, color='gray', linestyle=':', alpha=0.7)
axes[0, 0].set_title('Retail Sales vs. Inflation YoY Growth Trajectory', fontweight='bold')
axes[0, 0].set_ylabel('YoY % Change')
axes[0, 0].legend(loc='upper right')

# Panel 2: Consumer Sentiment Index
axes[0, 1].plot(df_clean.index, df_clean['Consumer_Sentiment'], label='Consumer Sentiment', color='#9b5de5', linewidth=2)
axes[0, 1].set_title('U.S. Consumer Sentiment Index (Leading Indicator)', fontweight='bold')
axes[0, 1].set_ylabel('Index Value')
axes[0, 1].legend(loc='upper right')

# Panel 3: Correlation Matrix Heatmap
sns.heatmap(correlations, annot=True, cmap='Blues', fmt=".2f", ax=axes[1, 0], cbar=False)
axes[1, 0].set_title('Macroeconomic Metric Correlation Matrix', fontweight='bold')

# Panel 4: Retail Sales 3-Month Moving Average Smoothing
axes[1, 1].plot(df_clean.index, df_clean['Retail_YoY'], label='Raw YoY', color='#e76f51', alpha=0.35)
axes[1, 1].plot(df_clean.index, df_clean['Retail_3M_MA'], label='3-Month Moving Avg', color='#2a9d8f', linewidth=2)
axes[1, 1].set_title('Retail Sales Trend Smoothing (3M Moving Average)', fontweight='bold')
axes[1, 1].set_ylabel('YoY % Change')
axes[1, 1].legend(loc='upper right')

plt.tight_layout()

# Save dashboard image for GitHub output display
plt.savefig('macro_dashboard.png', dpi=300)
plt.show()

print("\nPipeline execution complete! Image saved as 'macro_dashboard.png'.")
