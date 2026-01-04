# Write your MySQL query statement below
select
activity_date as day, count(user_id) as active_users
from
(
select
activity_date,user_id
from
Activity
where
activity_date <= '2019-07-27' and
activity_date > '2019-06-27' 
group by 
activity_date,user_id
) a
group by
activity_date
order by
activity_date
