# Write your MySQL query statement below
select
    w.id
from
    Weather w
inner join
(
select
    wa.recordDate as recordDate
    ,max(wb.temperature) as temperature
from
    Weather wa
inner join
    Weather wb
on
    wa.recordDate = DATE_ADD(wb.recordDate, INTERVAL 1 DAY)
group by
    wa.recordDate
) pastMaxTemp
on
w.recordDate = pastMaxTemp.recordDate
where
w.temperature > pastMaxTemp.temperature
order by w.id
;