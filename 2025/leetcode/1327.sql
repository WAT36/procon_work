# Write your MySQL query statement below
select
p.product_name,o.unit
from
Products p
inner join
(
select
product_id,sum(unit) as unit
from
Orders
where
order_date between '2020-02-01' and '2020-02-29'
group by
product_id
) o
on
p.product_id = o.product_id
where
o.unit >= 100
