SELECT sensor_id, COUNT(DISTINCT event_type) AS types
-- columns as needed 
From events
Group by sensor_id
-- need the order
Order by sensor_id ASC;



SELECT 
g.name 
-- to account for corner cases use coalesce
,coalesce(count(c.id),0) as all_test_cases
,coalesce(sum(CASE when c.status ='OK' then 1 else 0 end),0) as passed_test_cases
,coalesce(sum(CASE when c.status ='OK' then g.test_value else 0 end),0) as total_value
-- brackets
from
test_groups g
left join 
-- note not join 
test_cases c
on g.name=c.group_name
group by
g.name
,g.test_value
order by
--note order
total_value desc
,g.name asc;