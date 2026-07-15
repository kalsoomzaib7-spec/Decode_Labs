"""
Project 2 - Exploratory Data Analysis (EDA)
DecodeLabs Internship

Uses the cleaned dataset from Project 1. This script does NOT modify data
(that's Project 1's job) -- it only investigates and summarizes it.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# 1. LOAD (the already-cleaned data)
# ------------------------------------------------------------------
df = pd.read_excel("Cleaned_Dataset.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
print(f"Loaded {len(df)} clean rows")

# ------------------------------------------------------------------
# 2. DESCRIPTIVE STATISTICS (mean, median, count, five-number summary)
# ------------------------------------------------------------------
summary = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe().round(2)
print("\n--- Five-number summary ---")
print(summary)

# ------------------------------------------------------------------
# 3. OUTLIER DETECTION -- IQR method
#    Formula: Outlier if value < Q1 - 1.5*IQR  OR  value > Q3 + 1.5*IQR
# ------------------------------------------------------------------
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower_bound) | (df["TotalPrice"] > upper_bound)]
print(f"\nIQR bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Outliers found: {len(outliers)} out of {len(df)} rows ({len(outliers)/len(df)*100:.1f}%)")

# ------------------------------------------------------------------
# 4. CORRELATION ANALYSIS
#    Pearson correlation coefficient (r): -1 to +1
# ------------------------------------------------------------------
corr = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr().round(2)
print("\n--- Correlation matrix ---")
print(corr)

# ------------------------------------------------------------------
# 5. GROUP-BY BREAKDOWNS (business segmentation)
# ------------------------------------------------------------------
by_product = df.groupby("Product")["TotalPrice"].agg(["mean", "count"]).round(2).sort_values("mean", ascending=False)
by_referral = df.groupby("ReferralSource")["TotalPrice"].agg(["mean", "count"]).round(2).sort_values("mean", ascending=False)
by_status = df["OrderStatus"].value_counts()

print("\n--- Avg order value by Product ---")
print(by_product)
print("\n--- Avg order value by Referral Source ---")
print(by_referral)
print("\n--- Orders by Status ---")
print(by_status)

# ------------------------------------------------------------------
# 6. MONTHLY TREND
# ------------------------------------------------------------------
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month")["TotalPrice"].sum()

# ------------------------------------------------------------------
# 7. VISUALIZATIONS
# ------------------------------------------------------------------
plt.style.use("seaborn-v0_8-whitegrid")

# Chart 1: Distribution of TotalPrice
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["TotalPrice"], bins=30, color="#4C72B0", edgecolor="white")
ax.set_title("Distribution of Order Value (TotalPrice)")
ax.set_xlabel("Total Price ($)")
ax.set_ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("chart_distribution.png", dpi=150)
plt.close()

# Chart 2: Boxplot for outliers
fig, ax = plt.subplots(figsize=(6, 5))
ax.boxplot(df["TotalPrice"], vert=True)
ax.set_title("Boxplot of Order Value (Outlier Check)")
ax.set_ylabel("Total Price ($)")
plt.tight_layout()
plt.savefig("chart_boxplot.png", dpi=150)
plt.close()

# Chart 3: Correlation heatmap
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, corr.iloc[i, j], ha="center", va="center", color="black")
ax.set_title("Correlation Matrix")
fig.colorbar(im)
plt.tight_layout()
plt.savefig("chart_correlation.png", dpi=150)
plt.close()

# Chart 4: Avg order value by product
fig, ax = plt.subplots(figsize=(8, 5))
by_product["mean"].plot(kind="barh", ax=ax, color="#55A868")
ax.set_title("Average Order Value by Product")
ax.set_xlabel("Average Total Price ($)")
plt.tight_layout()
plt.savefig("chart_by_product.png", dpi=150)
plt.close()

# Chart 5: Monthly revenue trend
fig, ax = plt.subplots(figsize=(10, 5))
monthly.plot(ax=ax, marker="o", color="#C44E52")
ax.set_title("Monthly Revenue Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Total Revenue ($)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("chart_monthly_trend.png", dpi=150)
plt.close()

print("\nSaved 5 charts: distribution, boxplot, correlation, by_product, monthly_trend")
