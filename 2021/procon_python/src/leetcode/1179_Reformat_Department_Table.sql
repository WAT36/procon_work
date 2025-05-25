select
    d.id as id,
    jan.revenue as Jan_Revenue,
    feb.revenue as Feb_Revenue,
    mar.revenue as Mar_Revenue,
    apr.revenue as Apr_Revenue,
    may.revenue as May_Revenue,
    jun.revenue as Jun_Revenue,
    jul.revenue as Jul_Revenue,
    aug.revenue as Aug_Revenue,
    sep.revenue as Sep_Revenue,
    oct.revenue as Oct_Revenue,
    nov.revenue as Nov_Revenue,
    decem.revenue as Dec_Revenue
from
    (select distinct id from Department) as d
left outer join
    (select id,revenue from Department where month = "Jan") as jan
    on d.id = jan.id
left outer join
    (select id,revenue from Department where month = "Feb") as feb
    on d.id = feb.id
left outer join
    (select id,revenue from Department where month = "Mar") as mar
    on d.id = mar.id
left outer join
    (select id,revenue from Department where month = "Apr") as apr
    on d.id = apr.id
left outer join
    (select id,revenue from Department where month = "May") as may
    on d.id = may.id
left outer join
    (select id,revenue from Department where month = "Jun") as jun
    on d.id = jun.id
left outer join
    (select id,revenue from Department where month = "Jul") as jul
    on d.id = jul.id
left outer join
    (select id,revenue from Department where month = "Aug") as aug
    on d.id = aug.id
left outer join
    (select id,revenue from Department where month = "Sep") as sep
    on d.id = sep.id
left outer join
    (select id,revenue from Department where month = "Oct") as oct
    on d.id = oct.id
left outer join
    (select id,revenue from Department where month = "Nov") as nov
    on d.id = nov.id
left outer join
    (select id,revenue from Department where month = "Dec") as decem
    on d.id = decem.id
order by d.id