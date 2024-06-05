-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | user_id       | int     |
-- | session_id    | int     |
-- | activity_date | date    |
-- | activity_type | enum    |
-- +---------------+---------+
-- This table may have duplicate rows.
-- The activity_type column is an ENUM (category) of type ('open_session', 'end_session', 'scroll_down', 'send_message').
-- The table shows the user activities for a social media website. 
-- Note that each session belongs to exactly one user.
--  
-- 
-- Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.
-- 
-- Return the result table in any order.
-- 
-- The result format is in the following example.

select activity_date as day, count(distinct user_id) as active_users
from 30_days_activities
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date

-- ---------------------------------------------------
-- 
-- Input: 
-- Employees table:
-- +-------------+---------+------------+-----+ 
-- | employee_id | name    | reports_to | age |
-- |-------------|---------|------------|-----|
-- | 1           | Michael | null       | 45  |
-- | 2           | Alice   | 1          | 38  |
-- | 3           | Bob     | 1          | 42  |
-- | 4           | Charlie | 2          | 34  |
-- | 5           | David   | 2          | 40  |
-- | 6           | Eve     | 3          | 37  |
-- | 7           | Frank   | null       | 50  |
-- | 8           | Grace   | null       | 48  |
-- +-------------+---------+------------+-----+ 
-- Output: 
-- +-------------+---------+---------------+-------------+
-- | employee_id | name    | reports_count | average_age |
-- | ----------- | ------- | ------------- | ----------- |
-- | 1           | Michael | 2             | 40          |
-- | 2           | Alice   | 2             | 37          |
-- | 3           | Bob     | 1             | 37  

select e.employee_id, e.name, count(distinct e2.employee_id) as reports_count, avg(e2.age) as average_age
from employees e
left join employees e2 on e.employee_id = e2.reports_to
group by e.employee_id
having reports_count > 0
