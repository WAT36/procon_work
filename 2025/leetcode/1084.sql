# Write your MySQL query statement below
select
p.product_id,p.product_name
from
Product p
inner join
(
select
product_id
from
Sales
where
sale_date between '2019-01-01' and '2019-03-31'
group by
product_id
except
select
product_id
from
Sales
where
sale_date > '2019-03-31'
or
sale_date < '2019-01-01'
group by
product_id
) s
on
p.product_id = s.product_id