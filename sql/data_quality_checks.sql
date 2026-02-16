-- Check for missing product IDs
SELECT * 
FROM fact_sales
WHERE product_id IS NULL;

-- Check for negative quantities or prices
SELECT *
FROM fact_sales
WHERE quantity < 0 OR price < 0;

-- Check for duplicate sale IDs
SELECT sale_id, COUNT(*)
FROM fact_sales
GROUP BY sale_id
HAVING COUNT(*) > 1;

-- Check referential integrity
SELECT fs.product_id
FROM fact_sales fs
LEFT JOIN dim_product dp ON fs.product_id = dp.product_id
WHERE dp.product_id IS NULL;
