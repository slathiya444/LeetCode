-- Write your PostgreSQL query statement below
select id
from(
select id, recordDate, temperature,
    LAG(temperature, 1, NULL) over(order by recordDate) as temp,
    LAG(recordDate, 1, NULL) over(order by recordDate) as prev_date
from Weather
) a
where temperature > temp and recorddate = prev_date + interval '1 day';
