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


