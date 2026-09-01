-- EstateIQ PRICE_SQFT Quality Investigation


-- Overall PRICE_SQFT distribution

SELECT
    COUNT(*) AS total_records,
    COUNT(PRICE_SQFT) AS valid_price_records,
    SUM(
        CASE
            WHEN PRICE_SQFT <= 0 THEN 1
            ELSE 0
        END
    ) AS non_positive_records,
    MIN(PRICE_SQFT) AS minimum_price_sqft,
    MAX(PRICE_SQFT) AS maximum_price_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed;


-- Very low PRICE_SQFT values

SELECT
    PRICE_SQFT,
    COUNT(*) AS property_count
FROM estateiq_processed
WHERE PRICE_SQFT <= 1000
GROUP BY PRICE_SQFT
ORDER BY PRICE_SQFT;


-- Price bands

SELECT
    CASE
        WHEN PRICE_SQFT < 1000 THEN '< ₹1,000'
        WHEN PRICE_SQFT < 5000 THEN '₹1,000–₹4,999'
        WHEN PRICE_SQFT < 10000 THEN '₹5,000–₹9,999'
        WHEN PRICE_SQFT < 15000 THEN '₹10,000–₹14,999'
        WHEN PRICE_SQFT < 20000 THEN '₹15,000–₹19,999'
        WHEN PRICE_SQFT < 30000 THEN '₹20,000–₹29,999'
        ELSE '₹30,000+'
    END AS price_band,
    COUNT(*) AS property_count
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY price_band
ORDER BY
    CASE price_band
        WHEN '< ₹1,000' THEN 1
        WHEN '₹1,000–₹4,999' THEN 2
        WHEN '₹5,000–₹9,999' THEN 3
        WHEN '₹10,000–₹14,999' THEN 4
        WHEN '₹15,000–₹19,999' THEN 5
        WHEN '₹20,000–₹29,999' THEN 6
        WHEN '₹30,000+' THEN 7
    END;


-- Very low prices by property type

SELECT
    PROPERTY_TYPE,
    COUNT(*) AS low_price_records,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE PRICE_SQFT <= 1000
GROUP BY PROPERTY_TYPE
ORDER BY low_price_records DESC;


-- Very low prices by city

SELECT
    CITY,
    COUNT(*) AS low_price_records,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE PRICE_SQFT <= 1000
GROUP BY CITY
ORDER BY low_price_records DESC;


-- Extreme high-price records

SELECT
    PROP_ID,
    CITY,
    PROPERTY_TYPE,
    AREA,
    PRICE_SQFT
FROM estateiq_processed
WHERE PRICE_SQFT >= 30000
ORDER BY PRICE_SQFT DESC
LIMIT 20;


-- Lowest-price records

SELECT
    PROP_ID,
    CITY,
    PROPERTY_TYPE,
    AREA,
    PRICE_SQFT
FROM estateiq_processed
WHERE PRICE_SQFT > 0
ORDER BY PRICE_SQFT ASC
LIMIT 20;