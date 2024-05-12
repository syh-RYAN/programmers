-- 코드를 작성해주세요
select i.item_id, item_name, rarity
from item_info i
left join item_tree t 
on i.item_id = t.parent_item_id
where parent_item_id is null
order by item_id desc;