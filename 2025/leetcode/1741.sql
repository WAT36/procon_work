# Write your MySQL query statement below
select
event_day as day,emp_id,sum(time)  as total_time
from
(
select
emp_id,event_day,out_time - in_time as time
from
Employees
) as e
group by
emp_id,event_day