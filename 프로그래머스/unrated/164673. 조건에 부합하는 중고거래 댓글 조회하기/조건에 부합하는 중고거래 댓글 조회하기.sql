-- 코드를 입력하세요
SELECT  BOARD.TITLE
    ,   REPLY.BOARD_ID
    ,   REPLY.REPLY_ID
    ,   REPLY.WRITER_ID
    ,   REPLY.CONTENTS
    ,   DATE_FORMAT(REPLY.CREATED_DATE,'%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS BOARD
INNER JOIN USED_GOODS_REPLY AS REPLY
ON DATE_FORMAT(BOARD.CREATED_DATE,'%Y-%m') = '2022-10' and  
   BOARD.BOARD_ID = REPLY.BOARD_ID
ORDER BY DATE_FORMAT(REPLY.CREATED_DATE,'%Y-%m-%d') , BOARD.TITLE 
   