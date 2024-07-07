-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
-- product_id is the primary key (column with unique values) for this table.
-- low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
-- recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
--  
-- 
-- Write a solution to find the ids of products that are both low fat and recyclable.
-- 
-- Return the result table in any order.

Select product_id
From low_fats
Where low_fats = 'Y' and recyclable = 'Y';

-- There is a factory website that hasseveral machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.
--
-- The time to complete a process is te 'end' timestamp minus the 'start' timestamp. 
-- The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.
--
-- The resulting table should have themachine_id along with the average time as processing_time, which should be rounded to 3 decimal places.
--
-- Return the result table in any orde.
-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | float   |
-- +----------------+---------+
Select machine_id, Round(Avg(timestamp), 3) as processing_time
From Activity
Group by machine_id;

-- | machine_id | process_id | activity_type | timestamp |
-- | ---------- | ---------- | ------------- | --------- |
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.52      |
-- | 0          | 1          | start         | 3.14      |
-- | 0          | 1          | end           | 4.12      |
-- | 1          | 0          | start         | 0.55      |
-- | 1          | 0          | end           | 1.55      |
-- Output: 
-- +------------+-----------------+
-- | machine_id | processing_time |
-- +------------+-----------------+
-- | 0          | 0.894           |
-- | 1          | 0.995           |
-- | 2          | 1.456           |
-- +------------+-----------------+--
-- solution to mysql 
Select machine_id, Round(Avg(timestamp), 3) as processing_time
From Activity
Group by machine_id;


------------------------------------------------
# Write your MySQL query statement below
/* Write your PL/SQL query statement below */

select t1.product_id, first_year, t1.quantity, t1.price  
from sales t1
join (
    select product_id, MIN(year) as first_year
    from Sales
    GROUP BY product_id
) t2 ON t1.product_id = t2.product_id AND t1.year = t2.first_year;
 