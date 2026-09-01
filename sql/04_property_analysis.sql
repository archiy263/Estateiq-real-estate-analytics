-- EstateIQ Property Analysis


-- Property type market overview

SELECT
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM estateiq_processed),
        2
    ) AS market_share_percent,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY PROPERTY_TYPE
ORDER BY property_count DESC;


-- Property type pricing using median PRICE_SQFT

WITH ranked_prices AS (
    SELECT
        PROPERTY_TYPE,
        PRICE_SQFT,
        ROW_NUMBER() OVER (
            PARTITION BY PROPERTY_TYPE
            ORDER BY PRICE_SQFT
        ) AS price_rank,
        COUNT(*) OVER (
            PARTITION BY PROPERTY_TYPE
        ) AS type_count
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
),

type_medians AS (
    SELECT
        PROPERTY_TYPE,
        type_count,
        AVG(
            CASE
                WHEN price_rank IN (
                    (type_count + 1) / 2,
                    (type_count + 2) / 2
                )
                THEN PRICE_SQFT
            END
        ) AS median_price_sqft
    FROM ranked_prices
    GROUP BY PROPERTY_TYPE
)

SELECT
    PROPERTY_TYPE,
    type_count AS property_count,
    ROUND(median_price_sqft, 2) AS median_price_sqft
FROM type_medians
ORDER BY median_price_sqft DESC;


-- Area profile by property type

SELECT
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(MIN(AREA), 0) AS minimum_area_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(MAX(AREA), 0) AS maximum_area_sqft
FROM estateiq_processed
WHERE AREA > 0
GROUP BY PROPERTY_TYPE
ORDER BY average_area_sqft DESC;


-- Bedroom distribution

SELECT
    BEDROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE BEDROOM_NUM IS NOT NULL
  AND BEDROOM_NUM > 0
GROUP BY BEDROOM_NUM
ORDER BY BEDROOM_NUM;


-- Bedroom-level market comparison

SELECT
    BEDROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE BEDROOM_NUM IS NOT NULL
  AND BEDROOM_NUM > 0
GROUP BY BEDROOM_NUM
HAVING COUNT(*) >= 50
ORDER BY property_count DESC;


-- Bathroom distribution

SELECT
    BATHROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE BATHROOM_NUM IS NOT NULL
GROUP BY BATHROOM_NUM
ORDER BY BATHROOM_NUM;


-- Balcony distribution

SELECT
    BALCONY_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE BALCONY_NUM IS NOT NULL
GROUP BY BALCONY_NUM
ORDER BY BALCONY_NUM;


-- Property type and bedroom combinations

SELECT
    PROPERTY_TYPE,
    BEDROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE BEDROOM_NUM IS NOT NULL
  AND BEDROOM_NUM > 0
  AND PRICE_SQFT > 0
GROUP BY PROPERTY_TYPE, BEDROOM_NUM
HAVING COUNT(*) >= 25
ORDER BY property_count DESC;


-- Property type and area relationship

SELECT
    PROPERTY_TYPE,
    CASE
        WHEN AREA < 500 THEN '< 500 sq.ft.'
        WHEN AREA < 1000 THEN '500–999 sq.ft.'
        WHEN AREA < 1500 THEN '1,000–1,499 sq.ft.'
        WHEN AREA < 2500 THEN '1,500–2,499 sq.ft.'
        WHEN AREA < 5000 THEN '2,500–4,999 sq.ft.'
        ELSE '5,000+ sq.ft.'
    END AS area_band,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE AREA > 0
  AND PRICE_SQFT > 0
GROUP BY PROPERTY_TYPE, area_band
HAVING COUNT(*) >= 10
ORDER BY PROPERTY_TYPE, property_count DESC;


-- Most common property configurations

SELECT
    PROPERTY_TYPE,
    BEDROOM_NUM,
    BATHROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE BEDROOM_NUM IS NOT NULL
  AND BATHROOM_NUM IS NOT NULL
  AND BEDROOM_NUM > 0
  AND BATHROOM_NUM >= 0
  AND PRICE_SQFT > 0
GROUP BY
    PROPERTY_TYPE,
    BEDROOM_NUM,
    BATHROOM_NUM
HAVING COUNT(*) >= 25
ORDER BY property_count DESC
LIMIT 25;