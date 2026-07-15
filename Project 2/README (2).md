# Project 2: Exploratory Data Analysis (EDA)
**DecodeLabs Industrial Training Kit — Batch 2026**

## Goal
Analyze the cleaned dataset (from Project 1) to uncover patterns, trends,
and outliers — without modifying the data itself.

## Files
| File | Purpose |
|---|---|
| `Cleaned_Dataset.xlsx` | Input (output of Project 1) |
| `eda_analysis.py` | Analysis script (Python + pandas + matplotlib) |
| `insights_summary.md` | Written findings — the "so what" |
| `chart_distribution.png` | Histogram of order values |
| `chart_boxplot.png` | Boxplot for outlier detection |
| `chart_correlation.png` | Correlation heatmap |
| `chart_by_product.png` | Average order value by product |
| `chart_monthly_trend.png` | Revenue over time |

## How to run
```bash
pip install pandas matplotlib openpyxl
python eda_analysis.py
```

## Method
1. **Descriptive statistics** — mean, median, quartiles for Quantity,
   UnitPrice, ItemsInCart, TotalPrice.
2. **Outlier detection** — IQR method: flag values outside
   `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`.
3. **Correlation analysis** — Pearson correlation coefficient between all
   numeric columns.
4. **Segmentation** — grouped by Product, Referral Source, and Order
   Status to compare averages.
5. **Trend analysis** — monthly revenue aggregation.

## Key result
Data is evenly distributed across categories, correlations match
arithmetic expectations, and only 0.7% of rows are statistical outliers.
Full write-up in `insights_summary.md`.
