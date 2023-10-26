-- 코드를 입력하세요
SELECT AI.ANIMAL_ID,
       AI.NAME
FROM ANIMAL_INS AS AI
INNER JOIN ANIMAL_OUTS AS AO
ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.DATETIME >= AO.DATETIME
ORDER BY AI.DATETIME ASC