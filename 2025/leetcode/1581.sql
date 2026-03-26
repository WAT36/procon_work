# Write your MySQL query statement below
select
v2.customer_id,count(v2.customer_id) as count_no_trans
from
(
select
visit_id
from
Visits
except
select
visit_id
from
Transactions
group by
visit_id
) v1
inner join
Visits v2
on
v1.visit_id = v2.visit_id
group by
v2.customer_id