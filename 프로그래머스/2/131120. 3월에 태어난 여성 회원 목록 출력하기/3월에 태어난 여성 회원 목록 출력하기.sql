-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where month(date_of_birth)='03' and gender='W' and tlno is not null
group by member_id