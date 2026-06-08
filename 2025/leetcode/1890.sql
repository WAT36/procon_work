# Write your MySQL query statement below
select
user_id,max(time_stamp) as last_stamp
from
Logins
where time_stamp between "2020-01-01 00:00:00" and "2020-12-31 23:59:59" 
group by user_id