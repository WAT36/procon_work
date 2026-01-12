# Write your MySQL query statement below
select
q1.query_name,q1.quality as quality,round(coalesce(q3.c,0)/q2.c*100,2) as poor_query_percentage
from
(
select
query_name, round(avg(rating/position),2) as quality
from
Queries
group by
query_name
)  q1
inner join
(
select
query_name, count(*) as c
from
Queries
group by
query_name
)  q2
on
q1.query_name = q2.query_name 
left outer join
(
select
query_name, count(*) as c
from
Queries
where
rating < 3
group by
query_name
)  q3
on
q1.query_name = q3.query_name 
