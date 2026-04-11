# Write your MySQL query statement below
select
machine_id,round(avg(timestamp),3) as processing_time
from
(
select
machine_id,process_id,sum(timestamp) as timestamp
from
(
select
machine_id,process_id,activity_type,timestamp*(-1) as timestamp
from Activity
where activity_type='start'
union
select
machine_id,process_id,activity_type,timestamp
from Activity
where activity_type='end'
) a
group by
machine_id,process_id
) aa
group by
machine_id