-- EstateIQ Business Insights


-- 1. Largest markets

SELECT
    CITY,
    COUNT(*) AS property_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM estateiq_processed),
        2
    ) AS market_share_percent
FROM estateiq_processed
GROUP BY CITY
ORDER BY property_count DESC
LIMIT 5;


-- 2. Highest-priced established markets

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
WHERE city_count >= 100
ORDER BY median_price_sqft DESC
LIMIT 10;


-- 3. Dominant property segments

SELECT
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM estateiq_processed),
        2
    ) AS market_share_percent,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
GROUP BY PROPERTY_TYPE
ORDER BY property_count DESC;


-- 4. High-volume city/property segments

SELECT
    CITY,
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY, PROPERTY_TYPE
HAVING COUNT(*) >= 100
ORDER BY property_count DESC
LIMIT 15;


-- 5. Premium established segments

SELECT
    CITY,
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY, PROPERTY_TYPE
HAVING COUNT(*) >= 50
   AND AVG(PRICE_SQFT) >= 15000
ORDER BY average_price_sqft DESC;


-- 6. Large-area property segments

SELECT
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE AREA > 0
  AND PRICE_SQFT > 0
GROUP BY PROPERTY_TYPE
HAVING COUNT(*) >= 25
ORDER BY average_area_sqft DESC;


-- 7. Most common bedroom segments

SELECT
    BEDROOM_NUM,
    COUNT(*) AS property_count,
    ROUND(
        COUNT(*) * 100.0 /
        (
            SELECT COUNT(*)
            FROM estateiq_processed
            WHERE BEDROOM_NUM IS NOT NULL
        ),
        2
    ) AS share_of_known_bedroom_records,
    ROUND(AVG(AREA), 0) AS average_area_sqft,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft
FROM estateiq_processed
WHERE BEDROOM_NUM IS NOT NULL
  AND BEDROOM_NUM > 0
GROUP BY BEDROOM_NUM
HAVING COUNT(*) >= 50
ORDER BY property_count DESC;


-- 8. Most common property configurations

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
  AND PRICE_SQFT > 0
GROUP BY
    PROPERTY_TYPE,
    BEDROOM_NUM,
    BATHROOM_NUM
HAVING COUNT(*) >= 50
ORDER BY property_count DESC
LIMIT 10;


-- 9. High-price, high-volume locations

SELECT
    CITY,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY
HAVING COUNT(*) >= 250
   AND AVG(PRICE_SQFT) >= 12000
ORDER BY average_price_sqft DESC;


-- 10. Market opportunity ranking

WITH city_metrics AS (
    SELECT
        CITY,
        COUNT(*) AS property_count,
        AVG(PRICE_SQFT) AS average_price_sqft
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
    GROUP BY CITY
),

filtered_markets AS (
    SELECT
        CITY,
        property_count,
        average_price_sqft
    FROM city_metrics
    WHERE property_count >= 50
),

ranked_markets AS (
    SELECT
        CITY,
        property_count,
        average_price_sqft,

        PERCENT_RANK() OVER (
            ORDER BY property_count
        ) AS volume_percentile,

        PERCENT_RANK() OVER (
            ORDER BY average_price_sqft
        ) AS price_percentile

    FROM filtered_markets
)

SELECT
    CITY,
    property_count,
    ROUND(average_price_sqft, 2) AS average_price_sqft,
    ROUND(
        (
            volume_percentile * 0.5 +
            price_percentile * 0.5
        ) * 100,
        2
    ) AS opportunity_score
FROM ranked_markets
ORDER BY opportunity_score DESC;


-- 11. Overall portfolio summary

SELECT
    COUNT(*) AS total_properties,
    COUNT(DISTINCT CITY) AS total_cities,
    COUNT(DISTINCT PROPERTY_TYPE) AS total_property_types,
    COUNT(DISTINCT PROP_ID) AS unique_properties,
    SUM(
        CASE
            WHEN AREA IS NOT NULL AND AREA > 0
            THEN 1
            ELSE 0
        END
    ) AS valid_area_records,
    SUM(
        CASE
            WHEN PRICE_SQFT IS NOT NULL AND PRICE_SQFT > 0
            THEN 1
            ELSE 0
        END
    ) AS valid_price_records
FROM estateiq_processed;