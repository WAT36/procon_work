# Write your MySQL query statement below
select
u.name as NAME,t1.amount as BALANCE
from
(
select
account,sum(amount) as amount
from
Transactions t
group by
account
having
sum(amount)>10000
) t1
inner join
Users u
on
u.account = t1.account