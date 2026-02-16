-- Total quantity and revenue per product
SELECT 
    product_id,
    SUM(quantity) AS total_qty,
    SUM(total_amount) AS total_revenue,
    AVG(price) AS avg_price
FROM fact_sales
GROUP BY product_id;

-- Monthly revenue trend
SELECT 
    DATE_TRUNC('month', sale_date) AS sale_month,
    SUM(total_amount) AS monthly_revenue
FROM fact_sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY sale_month;

-- Top 5 best-selling products
SELECT 
    product_id,
    SUM(quantity) AS total_qty
FROM fact_sales
GROUP BY product_id
ORDER BY total_qty DESC
LIMIT 5;
