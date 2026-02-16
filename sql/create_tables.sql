-- Dimension table
CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

-- Fact table
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    total_amount DECIMAL(12,2),
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);

-- Indexes for performance
CREATE INDEX idx_product ON fact_sales(product_id);
CREATE INDEX idx_sale_date ON fact_sales(sale_date);
