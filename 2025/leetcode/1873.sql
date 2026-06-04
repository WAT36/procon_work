# Write your MySQL query statement below
select
employee_id,
CASE
    WHEN MOD(employee_id,2) = 1 and LEFT(name,1) <> 'M'
    THEN salary
    ELSE 0 
END AS bonus
from
Employees
order by
employee_id