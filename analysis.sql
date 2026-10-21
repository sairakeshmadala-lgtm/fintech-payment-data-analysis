-- SQL practice queries for the fictional transactions.csv dataset.
-- Load the CSV into a table named transactions before running these queries.

-- 1. Overall transaction metrics
SELECT
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN status = 'Success' THEN 1 ELSE 0 END) AS successful_transactions,
    ROUND(100.0 * SUM(CASE WHEN status = 'Success' THEN 1 ELSE 0 END) / COUNT(*), 2) AS success_rate_pct
FROM transactions;

-- 2. Successful payment value
SELECT SUM(amount_inr) AS successful_payment_value_inr
FROM transactions
WHERE status = 'Success';

-- 3. Payment method and status breakdown
SELECT payment_method, status, COUNT(*) AS transaction_count
FROM transactions
GROUP BY payment_method, status
ORDER BY payment_method, transaction_count DESC;

-- 4. Daily successful payment value
SELECT transaction_date, SUM(amount_inr) AS successful_value_inr
FROM transactions
WHERE status = 'Success'
GROUP BY transaction_date
ORDER BY transaction_date;

-- 5. Categories ranked by successful payment value
SELECT category, SUM(amount_inr) AS successful_value_inr
FROM transactions
WHERE status = 'Success'
GROUP BY category
ORDER BY successful_value_inr DESC;
