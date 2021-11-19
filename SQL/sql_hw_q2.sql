 -- 2
SELECT
	dpd.product_description
	, SUM(ct.quantity) AS quant_sold
FROM 
	dim_product_descriptions AS dpd
	, customer_transactions AS ct
        , dim_countries AS dc
WHERE ct.product_description_id = dpd.product_description_id
	AND ct.country_name_id = dc.country_name_id
	AND dc.country_name = 'USA'
GROUP BY  dpd.product_description
ORDER BY quant_sold DESC
LIMIT 1
;
/* Output: 
 product_description     | quant_sold
-------------------------+--------------------
 TOAST ITS - I LOVE YOU  | 408
*/
