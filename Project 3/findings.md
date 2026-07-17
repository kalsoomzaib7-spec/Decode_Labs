# Project 3: SQL Data Analysis — Key Findings

## Q1: High-value delivered orders (>$2000)
38 orders out of 1,200 meet this bar — the top one being a $3,456.40
Tablet order. This confirms the outliers identified back in Project 2's
EDA (the IQR method flagged 8 statistical outliers above ~$3,330; this
broader $2000 threshold naturally captures more "large but not extreme"
orders too).

## Q2: Order count per product
Fairly even spread across all 7 products (156–181 orders each), with
Printer (181) the most-ordered and Phone (156) the least. No single
product dominates order volume — consistent with the "evenly
distributed" pattern found in Project 2.

## Q3: Revenue and average order value per product
Chair generates the most total revenue ($195,620), narrowly ahead of
Printer ($195,613) and Laptop ($192,127). But Laptop has the highest
*average* order value ($1,110.56) — meaning Chair's revenue lead comes
from volume, not from individually bigger orders. This is the kind of
distinction a raw total alone would hide.

## Q4: Referral sources with 150+ orders (using HAVING)
All five referral sources clear this bar, led by Instagram (259 orders)
and Email (250). This demonstrates the key difference between `WHERE`
and `HAVING`: `WHERE` filters individual rows *before* grouping,
`HAVING` filters *after* grouping — you can't write
`WHERE COUNT(*) > 150` because `COUNT(*)` doesn't exist until the
groups are formed.

## Q5: Avg order value by payment method (delivered orders only)
Gift Card has the highest average order value among delivered orders
($1,099.54), Cash the lowest ($952.39) — a gap of about 15%. This query
combines `WHERE` (filter to Delivered only) with `GROUP BY` + `AVG` +
`COUNT`, run in the engine's actual execution order:
`FROM → WHERE → GROUP BY → SELECT → ORDER BY`.

## Bottom line
SQL confirms and sharpens what the Python/pandas EDA in Project 2
already suggested: this dataset is evenly distributed with no dominant
product or channel, but subtle differences do exist (Laptop's higher
average order value, Gift Card's edge in average spend) that only show
up once you group and aggregate rather than just eyeballing totals.
