-- EstateIQ Data Quality Audit

-- 1. Total records
SELECT COUNT(*) AS total_records
FROM estateiq_processed;


-- 2. Check duplicate property IDs
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT PROP_ID) AS unique_properties,
    COUNT(*) - COUNT(DISTINCT PROP_ID) AS duplicate_records
FROM estateiq_processed;


-- 3. Check missing values in key analytical fields
SELECT
    SUM(CASE WHEN PROP_ID IS NULL THEN 1 ELSE 0 END) AS missing_prop_id,
    SUM(CASE WHEN CITY IS NULL OR TRIM(CITY) = '' THEN 1 ELSE 0 END) AS missing_city,
    SUM(CASE WHEN PROPERTY_TYPE IS NULL OR TRIM(PROPERTY_TYPE) = '' THEN 1 ELSE 0 END) AS missing_property_type,
    SUM(CASE WHEN AREA IS NULL THEN 1 ELSE 0 END) AS missing_area,
    SUM(CASE WHEN PRICE_SQFT IS NULL THEN 1 ELSE 0 END) AS missing_price_sqft,
    SUM(CASE WHEN BEDROOM_NUM IS NULL THEN 1 ELSE 0 END) AS missing_bedrooms,
    SUM(CASE WHEN BATHROOM_NUM IS NULL THEN 1 ELSE 0 END) AS missing_bathrooms
FROM estateiq_processed;


-- 4. Validate numeric ranges
SELECT
    MIN(AREA) AS minimum_area,
    MAX(AREA) AS maximum_area,
    MIN(PRICE_SQFT) AS minimum_price_sqft,
    MAX(PRICE_SQFT) AS maximum_price_sqft,
    MIN(BEDROOM_NUM) AS minimum_bedrooms,
    MAX(BEDROOM_NUM) AS maximum_bedrooms,
    MIN(BATHROOM_NUM) AS minimum_bathrooms,
    MAX(BATHROOM_NUM) AS maximum_bathrooms
FROM estateiq_processed;


-- 5. Check invalid or non-positive area
SELECT COUNT(*) AS invalid_area_records
FROM estateiq_processed
WHERE AREA IS NULL
   OR AREA <= 0;


-- 6. Check invalid or non-positive price
SELECT COUNT(*) AS invalid_price_records
FROM estateiq_processed
WHERE PRICE_SQFT IS NULL
   OR PRICE_SQFT <= 0;


-- 7. City-level record distribution
SELECT
    CITY,
    COUNT(*) AS property_count
FROM estateiq_processed
GROUP BY CITY
ORDER BY property_count DESC;


-- 8. Property-type distribution
SELECT
    PROPERTY_TYPE,
    COUNT(*) AS property_count
FROM estateiq_processed
GROUP BY PROPERTY_TYPE
ORDER BY property_count DESC;


-- 9. Identify extreme area values
SELECT
    PROP_ID,
    CITY,
    PROPERTY_TYPE,
    AREA,
    PRICE_SQFT
FROM estateiq_processed
WHERE AREA > 10000
ORDER BY AREA DESC
LIMIT 20;