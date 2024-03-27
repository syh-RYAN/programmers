-- 코드를 작성해주세요
select fi.id, fi_na.fish_name, fi.length
from fish_name_info as fi_na 
inner join fish_info as fi
on fi_na.fish_type = fi.fish_type
and fi.length = 
(select max(length) from fish_info where fish_type = fi.fish_type)