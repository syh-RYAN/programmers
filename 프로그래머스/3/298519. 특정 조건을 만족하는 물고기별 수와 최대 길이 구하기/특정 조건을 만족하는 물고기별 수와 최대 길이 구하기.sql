-- 코드를 작성해주세요
select 
    count(*) as FISH_COUNT
    , case
        when max(length) <=10 then 10
        else max(length)
      end as MAX_LENGTH
    , FISH_TYPE
from fish_info
group by fish_type
having avg(length)>=33
ORDER BY fish_type