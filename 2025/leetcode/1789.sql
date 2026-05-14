# Write your MySQL query statement below
select
e.employee_id,e.department_id
from
Employee as e
inner join
(
select
employee_id,count(*) as count
from
Employee
group by
employee_id
) as c
on
e.employee_id = c.employee_id
where
(
    c.count = 1
    and e.primary_flag = 'N'
)
or
(
    c.count > 1
    and e.primary_flag = 'Y'
)