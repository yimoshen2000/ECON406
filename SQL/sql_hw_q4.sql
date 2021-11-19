-- 4
SELECT 
	dc.country_name
	, SUM(ct.unit_price * ct.quantity) AS revenue
FROM 
	customer_transactions AS ct
	, dim_countries AS dc
WHERE  ct.country_name_id = dc.country_name_id
	AND ct.invoice_date >= '2010-5-01'
	AND ct.invoice_date <= '2010-5-31'
GROUP BY dc.country_name
ORDER BY revenue DESC
LIMIT 1 OFFSET 3
;
/*Output: 
 country_name | revenue
--------------+--------------------
 France       | 13446.499947309494
*/
