# Project 2: Exploratory Data Analysis — Key Findings

## 1. Central Tendency (the "typical" order)
- **Mean order value:** $1,053.97
- **Median order value:** $823.62
- The mean is noticeably higher than the median, meaning a small number of
  large orders are pulling the average up — a classic **right-skewed**
  distribution. If asked "what does a typical order look like?", the
  median ($823.62) is the more honest answer.

## 2. Outliers
- Using the IQR method, only **8 out of 1,200 orders (0.7%)** fall outside
  the expected range ($-1,341 to $3,330 — the lower bound is negative
  because the data is skewed, so effectively only the *upper* bound matters
  here).
- This is a very low outlier rate. **Verdict: signal, not noise** — these
  are likely just legitimately large bulk orders (e.g., multiple laptops),
  not data entry errors, since Quantity × UnitPrice was already verified
  to be internally consistent in Project 1.

## 3. Correlation
- `UnitPrice` and `TotalPrice`: **r = 0.72** (strong positive) — expected,
  since price directly drives total.
- `Quantity` and `TotalPrice`: **r = 0.62** (moderate-strong positive) —
  also expected.
- `Quantity` and `ItemsInCart`: **r = 0.65** — customers who order more
  units also tend to have fuller carts.
- **No surprising or hidden relationships** were found. This is a
  reminder that not every dataset hides a dramatic secret — sometimes
  confirming the *expected* relationship IS the finding.

## 4. Segment Breakdown
- **By Product:** Laptop ($1,110 avg) and Chair ($1,099 avg) lead; Phone
  ($973 avg) is lowest — but the spread across all 7 products is narrow
  (within ~14% of each other), so no single product dominates revenue.
- **By Referral Source:** Facebook-referred orders have the highest
  average value ($1,098), Referral-sourced orders the lowest ($1,022) —
  again a narrow spread (~7%).
- **By Order Status:** Fairly evenly split across Cancelled, Returned,
  Pending, Shipped, and Delivered (231–250 each) — no status dominates.

## 5. Trend Over Time
- Monthly revenue fluctuates between ~$28K and ~$68K with no strong
  seasonal pattern (no clear holiday spike, no steady growth/decline
  trend) across Jan 2023 – Jun 2025.

## Bottom line ("So what?")
This dataset behaves like a **well-balanced, evenly-distributed synthetic
dataset** — every category (product, payment method, referral source,
order status) is close to uniformly represented, correlations match
what basic arithmetic would predict, and outliers are rare and
explainable. The honest professional conclusion: **there is no dramatic
hidden story here** — and reporting "the data is clean and evenly
distributed, with no red flags" is itself a valid and useful EDA finding,
not a failure to find something.
