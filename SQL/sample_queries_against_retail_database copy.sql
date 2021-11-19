/* -------------------------------------------------------------------------- */
/* Peek into main transactions table */
SELECT *
FROM customer_transactions
LIMIT 10
;
/* -------------------------------------------------------------------------- */
/* Get monthly units sold and revenue */
SELECT
    DATE_TRUNC('month', invoice_date)   AS year_month
    , SUM(quantity)                     AS units
    , ROUND(SUM(quantity * unit_price)) AS sales
FROM customer_transactions
GROUP BY
    DATE_TRUNC('month', invoice_date)
ORDER BY year_month ASC
;
/* -------------------------------------------------------------------------- */
/* Get min, max, and average price by country */
SELECT
    cntr.country_name
    , MIN(trans.unit_price) AS min_price
    , ROUND(AVG(trans.unit_price)::NUMERIC, 2) AS avg_price
    , MAX(trans.unit_price) AS max_price

FROM customer_transactions AS trans
INNER JOIN dim_countries AS cntr
  ON trans.country_name_id = cntr.country_name_id

GROUP BY
    cntr.country_name
ORDER BY avg_price DESC
;
/* -------------------------------------------------------------------------- */
/* Get top 5 and bottom 5 countries by # of invoices */
WITH invoice_count_by_country AS
(
    SELECT
        cntr.country_name
        , COUNT(DISTINCT trans.invoice_number_id) AS invoice_count

    FROM customer_transactions AS trans
    INNER JOIN dim_countries AS cntr
      ON trans.country_name_id = cntr.country_name_id

    GROUP BY
        cntr.country_name
)
, top5 AS
(
    SELECT *, 'top5' AS is_top_or_bottom
    FROM invoice_count_by_country
    ORDER BY invoice_count DESC
    LIMIT 5
)
, bottom5 AS
(
    SELECT *, 'bottom5' AS is_top_or_bottom
    FROM invoice_count_by_country
    ORDER BY invoice_count ASC
    LIMIT 5
)

SELECT *
FROM top5

UNION ALL

SELECT *
FROM bottom5

ORDER BY invoice_count DESC
;

/* --------------- */
/* Analytic functions for the same output */
WITH invoice_count_by_country AS
(
    SELECT
        cntr.country_name
        , COUNT(DISTINCT trans.invoice_number_id) AS invoice_count

    FROM customer_transactions AS trans
    INNER JOIN dim_countries AS cntr
      ON trans.country_name_id = cntr.country_name_id

    GROUP BY
        cntr.country_name
)
, ranks AS
(
    SELECT
        country_name
      , invoice_count
      , ROW_NUMBER() OVER(ORDER BY invoice_count  ASC) as bottom_rank
      , ROW_NUMBER() OVER(ORDER BY invoice_count DESC) as top_rank

    FROM invoice_count_by_country

)
SELECT
    country_name
  , invoice_count
  , top_rank
  , bottom_rank
  , CASE WHEN top_rank <= 5 THEN 'top5' ELSE 'bottom5' END AS is_top_or_bottom

FROM ranks

WHERE bottom_rank <= 6
   OR top_rank <= 6

ORDER BY invoice_count DESC
;
