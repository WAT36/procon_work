# Write your MySQL query statement below
select
e.employee_id,e.name,m.c as  reports_count,m.age  as average_age
from
(
select
reports_to,count(*) as c,round(avg(age)) as age
from
Employees
where
reports_to is not  null
group by
reports_to
) m
inner join
Employees e
on
m.reports_to = e.employee_id
order  by
e.employee_id