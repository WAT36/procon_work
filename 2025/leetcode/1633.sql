# Write your MySQL query statement below
with n as (
    select
        count(*) as c
    from
        Users
)
select
contest_id,round(100*count(*)/n.c,2) as percentage
from
Register r,n
group by
r.contest_id
order by
percentage desc,r.contest_id