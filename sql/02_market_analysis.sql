-- EstateIQ Market Analysis


-- Overall market summary

SELECT
    COUNT(*) AS total_properties,
    COUNT(DISTINCT CITY) AS cities,
    COUNT(DISTINCT PROPERTY_TYPE) AS property_types,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(MIN(PRICE_SQFT), 2) AS minimum_price_sqft,
    ROUND(MAX(PRICE_SQFT), 2) AS maximum_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
  AND AREA > 0;


-- City-level market size and pricing

WITH ranked_prices AS (
    SELECT
        CITY,
        PRICE_SQFT,
        ROW_NUMBER() OVER (
            PARTITION BY CITY
            ORDER BY PRICE_SQFT
        ) AS price_rank,
        COUNT(*) OVER (
            PARTITION BY CITY
        ) AS city_count
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
)

SELECT
    CITY,
    city_count AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(
        AVG(
            CASE
                WHEN price_rank IN (
                    (city_count + 1) / 2,
                    (city_count + 2) / 2
                )
                THEN PRICE_SQFT
            END
        ),
        2
    ) AS median_price_sqft
FROM ranked_prices
GROUP BY CITY
ORDER BY property_count DESC;


-- City ranking by median price
-- Minimum sample size prevents tiny markets from dominating the ranking

WITH ranked_prices AS (
    SELECT
        CITY,
        PRICE_SQFT,
        ROW_NUMBER() OVER (
            PARTITION BY CITY
            ORDER BY PRICE_SQFT
        ) AS price_rank,
        COUNT(*) OVER (
            PARTITION BY CITY
        ) AS city_count
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
),

city_medians AS (
    SELECT
        CITY,
        city_count,
        AVG(
            CASE
                WHEN price_rank IN (
                    (city_count + 1) / 2,
                    (city_count + 2) / 2
                )
                THEN PRICE_SQFT
            END
        ) AS median_price_sqft
    FROM ranked_prices
    GROUP BY CITY
)

SELECT
    CITY,
    city_count AS property_count,
    ROUND(median_price_sqft, 2) AS median_price_sqft
FROM city_medians
WHERE city_count >= 50
ORDER BY median_price_sqft DESC;


-- Property-type market comparison

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
    ROUND(median_price_sqft, 2) AS median_price_sqft,
    ROUND(
        (
            SELECT AVG(e.AREA)
            FROM estateiq_processed e
            WHERE e.PROPERTY_TYPE = type_medians.PROPERTY_TYPE
              AND e.AREA > 0
        ),
        0
    ) AS average_area_sqft
FROM type_medians
ORDER BY property_count DESC;


-- City and property-type pricing matrix

WITH ranked_prices AS (
    SELECT
        CITY,
        PROPERTY_TYPE,
        PRICE_SQFT,
        ROW_NUMBER() OVER (
            PARTITION BY CITY, PROPERTY_TYPE
            ORDER BY PRICE_SQFT
        ) AS price_rank,
        COUNT(*) OVER (
            PARTITION BY CITY, PROPERTY_TYPE
        ) AS group_count
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
),

group_medians AS (
    SELECT
        CITY,
        PROPERTY_TYPE,
        group_count,
        AVG(
            CASE
                WHEN price_rank IN (
                    (group_count + 1) / 2,
                    (group_count + 2) / 2
                )
                THEN PRICE_SQFT
            END
        ) AS median_price_sqft
    FROM ranked_prices
    GROUP BY CITY, PROPERTY_TYPE
)

SELECT
    CITY,
    PROPERTY_TYPE,
    group_count AS property_count,
    ROUND(median_price_sqft, 2) AS median_price_sqft
FROM group_medians
WHERE group_count >= 20
ORDER BY median_price_sqft DESC;


-- Market concentration by city

WITH city_counts AS (
    SELECT
        CITY,
        COUNT(*) AS property_count
    FROM estateiq_processed
    GROUP BY CITY
),

total_market AS (
    SELECT
        SUM(property_count) AS total_properties
    FROM city_counts
)

SELECT
    CITY,
    property_count,
    ROUND(
        property_count * 100.0 /
        total_market.total_properties,
        2
    ) AS market_share_percent
FROM city_counts
CROSS JOIN total_market
ORDER BY market_share_percent DESC;


-- Large and established markets

SELECT
    CITY,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY
HAVING COUNT(*) >= 100
ORDER BY property_count DESC;