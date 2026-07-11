# Project 1: Data Cleaning & Preparation
**DecodeLabs Industrial Training Kit — Batch 2026**

## Goal
Clean a raw e-commerce orders dataset (1,200 rows) by identifying missing
values, removing duplicates, and standardizing formats — proving the data
is reliable enough to build analysis on top of.

## Files
| File | Purpose |
|---|---|
| `Dataset_for_Data_Analytics.xlsx` | Raw input data |
| `clean_data.py` | Cleaning script (Python + pandas) |
| `Cleaned_Dataset.xlsx` | Final cleaned output |
| `change_log.csv` | Audit trail of every change made and why |

## How to run
```bash
pip install pandas openpyxl
python clean_data.py
```

## Process
1. **Profiled the data** — checked null counts per column, duplicate IDs,
   duplicate rows, date validity, and category spelling consistency.
2. **Handled missing values** — `CouponCode` was blank on 309 orders. This
   wasn't corrupted data; it meant no coupon was used. Filled with an
   explicit `"No Coupon"` label instead of a statistical guess (mean/median
   would have invented a coupon that was never applied).
3. **Checked duplicates** — 0 duplicate `OrderID`s, 0 duplicate rows found.
4. **Standardized formats** — dates converted to ISO 8601 (`YYYY-MM-DD`),
   text columns trimmed, prices rounded to 2 decimals.
5. **Validated business logic** — confirmed `TotalPrice = Quantity x
   UnitPrice` holds for all 1,200 rows (0 mismatches).
6. **Verified** — re-ran all checks after cleaning to confirm 0% error rate
   on unique identifiers and date formats, per the project's pass criteria.

## Result
- 1,200 / 1,200 rows retained (no data lost)
- 0 duplicate IDs
- 0 invalid dates
- 0 remaining nulls
- Full change log included for accountability
- Done
