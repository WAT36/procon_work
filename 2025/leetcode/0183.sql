# Write your MySQL query statement below
select c.name as Customers from Customers c left outer join 
(select customerId,count(*) as count from Orders o group by customerId) o
on c.id = o.customerId
where o.count is null