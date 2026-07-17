# Project 3: SQL Data Analysis
**DecodeLabs Industrial Training Kit — Batch 2026**

## Goal
Use SQL to extract insights from the orders dataset: filtering,
grouping, and aggregating raw rows into business intelligence.

## Files
| File | Purpose |
|---|---|
| `Dataset_for_Data_Analytics__1_.xlsx` | Raw input data |
| `sql_analysis.py` | Loads data into SQLite, runs 5 SQL queries |
| `query_output.txt` | Captured output of every query, for proof |
| `findings.md` | Written business insights per query |

## How to run
```bash
pip install pandas openpyxl
python sql_analysis.py
```
This creates `orders.db` (a real SQLite database) and prints every
query + its results to the console.

## Queries covered (mapped to the brief's requirements)
1. **SELECT + WHERE + ORDER BY** — high-value delivered orders
2. **GROUP BY + COUNT** — order volume per product
3. **GROUP BY + SUM + AVG** — revenue and average order value per product
4. **HAVING** — referral sources with more than 150 orders
5. **WHERE + GROUP BY + AVG + COUNT combined** — payment method
   performance for delivered orders only

## Key SQL concept demonstrated
The database's **execution order** differs from how SQL is *written*:
```
Written:   SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
Executed:  FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```
This is why `WHERE` can't reference a `SELECT` alias, and why `HAVING`
(not `WHERE`) is required to filter on an aggregate like `COUNT(*)`.

## Key result
See `findings.md` for full write-up. Highlight: Chair leads in total
revenue, but Laptop has the highest average order value — a distinction
only visible once you aggregate by group instead of looking at raw
totals.
