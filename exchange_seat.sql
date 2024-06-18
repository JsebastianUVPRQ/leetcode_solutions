-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key (unique value) column for this table.
-- Each row of this table indicates the name and the ID of a student.
-- id is a continuous increment.
--  
-- 
-- Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.
-- 
-- Return the result table ordered by id in ascending order.
-- 
-- The result format is in the following example.
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |

WITH SeatWithRowNum AS (
    SELECT id, student, ROW_NUMBER() OVER (ORDER BY id) AS row_num
    FROM Seat
)
SELECT 
    S1.id,
    CASE 
        WHEN S1.row_num % 2 = 1 AND S2.student IS NOT NULL THEN S2.student
        WHEN S1.row_num % 2 = 0 THEN S2.student
        ELSE S1.student
    END AS student
FROM 
    SeatWithRowNum S1
LEFT JOIN 
    SeatWithRowNum S2
ON 
    (S1.row_num % 2 = 1 AND S1.row_num + 1 = S2.row_num) 
    OR (S1.row_num % 2 = 0 AND S1.row_num - 1 = S2.row_num)
ORDER BY 
    S1.id;

-- -------------------Agregate functions------------------

-- Table: Users
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | user_name   | varchar |
-- +-------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- Each row of this table contains the name and the id of a user.
--  
-- 
-- Table: Register
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | contest_id  | int     |
-- | user_id     | int     |
-- +-------------+---------+
-- (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table contains the id of a user and the contest they registered into.
--  
-- 
-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
-- 
-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.
-- 
-- The result format is in the following example.
-- 
--  
-- 
-- Example 1:
-- 
-- Input: 
-- Users table:
-- +---------+-----------+
-- | user_id | user_name |
-- +---------+-----------+
-- | 6       | Alice     |
-- | 2       | Bob       |
-- | 7       | Alex      |
-- +---------+-----------+
-- Register table:
-- +------------+---------+
-- | contest_id | user_id |
-- +------------+---------+
-- | 215        | 6       |
-- | 209        | 2       |
-- | 208        | 2       |
-- | 210        | 6       |
-- | 208        | 6       |
-- | 209        | 7       |
-- | 209        | 6       |
-- | 215        | 7       |
-- | 208        | 7       |
-- | 210        | 2       |
-- | 207        | 2       |
-- | 210        | 7       |
-- +------------+---------+
-- Output: 
-- +------------+------------+
-- | contest_id | percentage |
-- +------------+------------+
-- | 208        | 100.0      |
-- | 209        | 100.0      |
-- | 210        | 100.0      |
-- | 215        | 66.67      |
-- | 207        | 33.33      |
-- +------------+------------+
-- Explanation: 
-- All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
-- Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
-- Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%
select contest_id,round(count(distinct user_id)*100/(select count(user_id)from users),2)as percentage
from Register 
group by contest_id 
order by percentage desc,contest_id
