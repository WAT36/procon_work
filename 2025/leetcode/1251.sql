# Write your MySQL query statement below
select
product_id,coalesce(round(sum(price*units)/sum(units),2),0) as average_price
from
(
select
p.product_id,price,units
from
Prices p
left outer join
UnitsSold u
on
p.product_id=u.product_id
and
purchase_date between start_date and end_date
) pp
group by
product_id