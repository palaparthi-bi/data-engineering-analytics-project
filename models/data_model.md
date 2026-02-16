# Star Schema Data Model

## Fact Table: fact_sales
- sale_id (PK)
- product_id (FK)
- quantity
- price
- total_amount
- sale_date

## Dimension Table: dim_product
- product_id (PK)
- product_name
- category

## Grain
One row per sale transaction.

## Purpose
This model supports:
- Revenue analytics
- Product performance analysis
- Trend analysis
