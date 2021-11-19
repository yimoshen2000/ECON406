-- 3
SELECT 
	di.invoice_status
	, COUNT(DISTINCT di.invoice_number_id) AS orders
FROM
	dim_invoices AS di
	, customer_transactions AS ct
	, dim_countries AS dc
WHERE ct.invoice_number_id = di.invoice_number_id
	AND ct.country_name_id = dc.country_name_id
	AND dc.country_name = 'United Kingdom'
	AND di.invoice_status = 
	CASE
		WHEN di.invoice_status IN('NAN', 'null', ' ')
			OR di.invoice_status IS NULL THEN 'Unknown'
		ELSE di.invoice_status
	END
GROUP BY di.invoice_status
;
/*
output:
 invoice_status | orders 
----------------+--------
 canceled       |   1596
 returned       |   2069
 shipped        |  34446
 unknown        |   2394
*/
