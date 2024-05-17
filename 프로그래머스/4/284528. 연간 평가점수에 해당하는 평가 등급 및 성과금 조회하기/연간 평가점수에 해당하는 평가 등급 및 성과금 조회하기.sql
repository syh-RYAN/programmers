-- 코드를 작성해주세요
SELECT  HE.EMP_NO
    ,   HE.EMP_NAME
    ,   CASE 
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    ,   CASE
            WHEN AVG(SCORE) >= 96 THEN SAL * 0.2
            WHEN AVG(SCORE) >= 90 THEN SAL * 0.15
            WHEN AVG(SCORE) >= 80 THEN SAL * 0.1
            ELSE SAL * 0
        END AS BONUS
FROM HR_GRADE AS HG
INNER JOIN HR_EMPLOYEES AS HE
ON HE.EMP_NO = HG.EMP_NO
GROUP BY HE.EMP_NO
ORDER BY EMP_NO;