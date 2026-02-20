# Write your MySQL query statement below
select
u.name,coalesce(r.distance,0) as travelled_distance
from
Users u
left outer join
(
select
user_id,sum(distance) as distance
from
Rides
group by
user_id
) r
on
u.id = r.user_id
order by
travelled_distance desc, name  asc