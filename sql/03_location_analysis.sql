-- EstateIQ Location Analysis


-- Location market overview

SELECT
    CITY,
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
GROUP BY CITY
ORDER BY property_count DESC;


-- Location pricing using median PRICE_SQFT

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
ORDER BY median_price_sqft DESC;


-- Established locations

SELECT
    CITY,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY
HAVING COUNT(*) >= 500
ORDER BY property_count DESC;


-- Location price premium versus overall market

WITH market_average AS (
    SELECT
        AVG(PRICE_SQFT) AS overall_average_price
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
),

city_prices AS (
    SELECT
        CITY,
        COUNT(*) AS property_count,
        AVG(PRICE_SQFT) AS city_average_price
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
    GROUP BY CITY
)

SELECT
    CITY,
    property_count,
    ROUND(city_average_price, 2) AS average_price_sqft,
    ROUND(
        (
            city_average_price -
            market_average.overall_average_price
        ) /
        market_average.overall_average_price * 100,
        2
    ) AS price_premium_percent
FROM city_prices
CROSS JOIN market_average
WHERE property_count >= 50
ORDER BY price_premium_percent DESC;


-- Location and property-type opportunity

SELECT
    CITY,
    PROPERTY_TYPE,
    COUNT(*) AS property_count,
    ROUND(AVG(PRICE_SQFT), 2) AS average_price_sqft,
    ROUND(AVG(AREA), 0) AS average_area_sqft
FROM estateiq_processed
WHERE PRICE_SQFT > 0
GROUP BY CITY, PROPERTY_TYPE
HAVING COUNT(*) >= 25
ORDER BY property_count DESC;


-- High-volume locations with above-market pricing

WITH market_average AS (
    SELECT
        AVG(PRICE_SQFT) AS overall_average_price
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
),

city_metrics AS (
    SELECT
        CITY,
        COUNT(*) AS property_count,
        AVG(PRICE_SQFT) AS average_price_sqft
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
    GROUP BY CITY
)

SELECT
    CITY,
    property_count,
    ROUND(average_price_sqft, 2) AS average_price_sqft,
    ROUND(
        average_price_sqft /
        market_average.overall_average_price,
        2
    ) AS price_index
FROM city_metrics
CROSS JOIN market_average
WHERE property_count >= 100
  AND average_price_sqft > market_average.overall_average_price
ORDER BY property_count DESC;


-- Location opportunity score

WITH city_metrics AS (
    SELECT
        CITY,
        COUNT(*) AS property_count,
        AVG(PRICE_SQFT) AS average_price_sqft
    FROM estateiq_processed
    WHERE PRICE_SQFT > 0
    GROUP BY CITY
),

market_ranges AS (
    SELECT
        MIN(property_count) AS min_count,
        MAX(property_count) AS max_count,
        MIN(average_price_sqft) AS min_price,
        MAX(average_price_sqft) AS max_price
    FROM city_metrics
),

scored_locations AS (
    SELECT
        city_metrics.CITY,
        city_metrics.property_count,
        city_metrics.average_price_sqft,

        (
            (
                city_metrics.property_count -
                market_ranges.min_count
            ) * 1.0 /
            NULLIF(
                market_ranges.max_count -
                market_ranges.min_count,
                0
            )
        ) * 50

        +

        (
            (
                city_metrics.average_price_sqft -
                market_ranges.min_price
            ) * 1.0 /
            NULLIF(
                market_ranges.max_price -
                market_ranges.min_price,
                0
            )
        ) * 50 AS opportunity_score

    FROM city_metrics
    CROSS JOIN market_ranges
)

SELECT
    CITY,
    property_count,
    ROUND(average_price_sqft, 2) AS average_price_sqft,
    ROUND(opportunity_score, 2) AS opportunity_score
FROM scored_locations
WHERE property_count >= 50
ORDER BY opportunity_score DESC;


-- Most active location-property combinations

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
ORDER BY property_count DESC;