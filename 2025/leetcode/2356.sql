# Write your MySQL query statement below
select
teacher_id,count(*) as cnt
from
(
select
teacher_id,subject_id
from
Teacher
group by
teacher_id,subject_id
) t
group by 
t.teacher_id