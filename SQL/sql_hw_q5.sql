-- 5
WITH male_data AS 
(
	SELECT 
		dcd.customer_country_name AS country
		, SUM(ct.unit_price * ct.quantity) AS male_revenue
	FROM
		customer_transactions AS ct
		, dim_customer_details AS dcd
	WHERE dcd.customer_id = ct.customer_id
		AND dcd.customer_gender IN ('MALE', 'male')
	GROUP BY dcd.customer_country_name
) 
, female_data AS
(
	SELECT 
		dcd.customer_country_name AS country
		,  SUM(ct.unit_price * ct.quantity) AS female_revenue
	FROM
		customer_transactions AS ct
		, dim_customer_details AS dcd
	WHERE  dcd.customer_id = ct.customer_id
		AND dcd.customer_gender IN ('FEMALE', 'female')
	GROUP BY dcd.customer_country_name
)
SELECT
	dc.country_name
	, md.male_revenue
	, fd.female_revenue
FROM
	dim_countries AS dc
LEFT OUTER JOIN male_data AS md
	ON dc.country_name = md.country
LEFT OUTER JOIN female_data AS fd
	ON dc.country_name = fd.country
ORDER BY dc.country_name
;
/* Output:
    country_name      |    male_revenue    |   female_revenue
----------------------+--------------------+--------------------
 Australia            | 154384.49007949233 |  6983.359974563122
 Austria              | 12526.300010919571 |   8277.67998829484
 Bahrain              |  947.6099910736084 |
 Belgium              | 25744.199904948473 | 30550.549952745438
 Brazil               | 268.26999916136265 | 1143.5999937057495
 Canada               | 1942.9999710321426 |  2940.039972729981
 Channel Islands      |  29577.67990374565 |  6166.299964904785
 Cyprus               | 10646.099956870079 | 10512.269942760468
 Czech Republic       |                    |  707.7199966907501
 Denmark              |  56611.48061367124 | 13766.329964578152
 EIRE                 |  308990.4484181404 | 270248.52859241515
 European Community   |                    | 1291.7500019073486
 Finland              |  27119.75996568799 |   2419.64999127388
 France               | 134346.47939690948 |  173907.5691279322
 Germany              | 198243.48030125897 |  212605.3988983035
 Greece               | 17055.589918613434 |  680.9899959564209
 Iceland              |                    |  5633.319988429546
 Israel               | 138.02999848127365 |  5181.809994220734
 Italy                | 14073.379966646433 | 14112.589931190014
 Japan                |   7503.86010068655 |  36272.71978700161
 Korea                |                  0 |  949.8199942708015
 Lebanon              |  1693.879989862442 |                   
 Lithuania            |  6553.739948391914 |                   
 Malta                |                    |  1853.969998061657
 Netherlands          | 13568.780009955168 |  534957.9685847461
 Nigeria              |                    |                   
 Norway               | 12309.629999160767 | 26933.399692684412
 Poland               |  2083.869993686676 |   8444.21999618411
 Portugal             | 16668.479956507683 |  36240.88976570964
 RSA                  | 1002.3099929094315 |  931.4300017356873
 Saudi Arabia         | 131.16999971866608 |                   
 Singapore            | 13158.159952044487 |                   
 Spain                |  26659.62990258634 |  41764.86991021037
 Sweden               |   58538.8096382916 | 28916.609752863646
 Switzerland          | 24701.629946649075 |  67323.84478342533
 Thailand             |  3070.539988040924 |                   
 United Arab Emirates |  7407.149944365025 | 1664.5600052773952
 United Kingdom       |   7131971.11071356 |  6332685.386299022
 Unspecified          |  6909.630038917065 |  264.1799980998039
 USA                  |  4710.859992176294 |  841.6999932825565
 West Indies          |                    |   536.409999102354
 */
 
 -- Extra Credit
WITH male_data AS 
(
	SELECT 
		dcd.customer_country_name AS country
		, SUM(ct.unit_price * ct.quantity) AS male_revenue
	FROM
		customer_transactions AS ct
		, dim_customer_details AS dcd
	WHERE dcd.customer_id = ct.customer_id
		AND dcd.customer_gender IN ('MALE', 'male')
	GROUP BY dcd.customer_country_name
) 
, female_data AS
(
	SELECT 
		dcd.customer_country_name AS country
		,  SUM(ct.unit_price * ct.quantity) AS female_revenue
	FROM
		customer_transactions AS ct
		, dim_customer_details AS dcd
	WHERE  dcd.customer_id = ct.customer_id
		AND dcd.customer_gender IN ('FEMALE', 'female')
	GROUP BY dcd.customer_country_name
)
SELECT
	dc.country_name AS country
	, md.male_revenue / fd.female_revenue AS parity
FROM
	dim_countries AS dc
LEFT OUTER JOIN male_data AS md
	ON dc.country_name = md.country
LEFT OUTER JOIN female_data AS fd
	ON dc.country_name = fd.country
ORDER BY ABS(md.male_revenue / fd.female_revenue - 1)
LIMIT 1
;
/* Output:
 country |       parity       
---------+--------------------
 Italy   | 0.9972216322634782
*/
