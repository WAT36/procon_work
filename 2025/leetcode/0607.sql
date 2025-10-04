# Write your MySQL query statement below
select
s.name
from
SalesPerson s
left outer join
(
select 
s.sales_id
from SalesPerson as s 
left outer join Orders as o 
on 
s.sales_id = o.sales_id
left outer join Company as c
on
o.com_id = c.com_id
and c.name = "RED"
where c.com_id is not null
group by s.sales_id
) s2
on
s.sales_id = s2.sales_id
where
s2.sales_id is null