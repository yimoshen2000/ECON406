-- 1.1
SELECT
    COUNT(DISTINCT Product_Code)
FROM dim_product_codes
;
-- output: 4646

-- 1.2
SELECT
	COUNT(DISTINCT ct.product_code_id)
FROM
	customer_transactions AS ct
	, dim_countries AS dc
WHERE ct.country_name_ID = dc.country_name_id
	AND dc.country_name = 'Germany'
;
-- output: 2176
    
-- 1.3
SELECT 
	COUNT(DISTINCT ct.product_code_id)
FROM
	customer_transactions AS ct
WHERE ct.invoice_date >= '2011-07-01'
	AND ct.invoice_date <= '2011-07-31'
;
-- output: 2340
