WITH A AS(
SELECT 
    COUNT(DISTINCT ONLINE_SALE.USER_ID) AS COUNT_USER_ID,
    YEAR(ONLINE_SALE.SALES_DATE) AS YEAR,
    MONTH(ONLINE_SALE.SALES_DATE) AS MONTH
FROM USER_INFO
INNER JOIN ONLINE_SALE
ON USER_INFO.USER_ID = ONLINE_SALE.USER_ID
WHERE YEAR(USER_INFO.JOINED) = 2021
GROUP BY YEAR(ONLINE_SALE.SALES_DATE),MONTH(ONLINE_SALE.SALES_DATE)
),
B AS(
    SELECT 
    USER_ID,
    COUNT(DISTINCT USER_ID) AS COUNT_TOTAL
FROM USER_INFO
WHERE YEAR(USER_INFO.JOINED)=2021)

SELECT
    A.YEAR,
    A.MONTH,
    A.COUNT_USER_ID AS PUCHASED_USER,
    ROUND(A.COUNT_USER_ID / B.COUNT_TOTAL,1) AS PUCHASED_RATIO
FROM A
CROSS JOIN B
ORDER BY A.YEAR,A.MONTH;