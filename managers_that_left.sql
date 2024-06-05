-- Input:  
-- Employees table:
-- +-------------+-----------+------------+--------+
-- | employee_id | name      | manager_id | salary |
-- +-------------+-----------+------------+--------+
-- | 3           | Mila      | 9          | 60301  |
-- | 12          | Antonella | null       | 31000  |
-- | 13          | Emery     | null       | 67084  |
-- | 1           | Kalel     | 11         | 21241  |
-- | 9           | Mikaela   | null       | 50937  |
-- | 11          | Joziah    | 6          | 28485  |
-- +-------------+-----------+------------+--------+
-- Output: 
-- +-------------+
-- | employee_id |
-- +-------------+
-- | 11          |
-- +-------------+
-- 
-- Explanation: 
-- The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
-- Kalel's manager is employee 11, who is still in the company (Joziah).
-- Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | employee_id | int      |
-- | name        | varchar  |
-- | manager_id  | int      |
-- | salary      | int      |
-- +-------------+----------+
-- In SQL, employee_id is the primary key for this table.
-- This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 
--  
-- 
-- Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.
-- 
-- Return the result table ordered by employee_id.
-- 
-- The result format is in the following example.

SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM Employees);

-- Courses table:
-- +---------+----------+
-- | student | class    |
-- +---------+----------+
-- | A       | Math     |
-- | B       | English  |
-- | C       | Math     |
-- | D       | Biology  |
-- | E       | Math     |
-- | F       | Computer |
-- | G       | Math     |
-- | H       | Math     |
-- | I       | Math     |
-- +---------+----------+
-- Output: 
-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+
-- Explanation: 
-- - Math has 6 students, so we include it.
-- - English has 1 student, so we do not include it.
-- - Biology has 1 student, so we do not include it.
-- - Computer has 1 student, so we do not include it.
-- 

select class
from courses
group by class
having count(student) > 5;

-- ---------------------------------------------------
-- 
-- Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
-- 
-- "Low Salary": All the salaries strictly less than $20000.
-- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
-- "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no accounts in a category, return 0.
-- 
-- Return the result table in any order.
-- 
-- The result format is in the following example.
-- 
--  
-- 
-- Example 1:
-- 
-- Input: 
-- Accounts table:
-- +------------+--------+
-- | account_id | income |
-- +------------+--------+
-- | 3          | 108939 |
-- | 2          | 12747  |
-- | 8          | 87709  |
-- | 6          | 91796  |
-- +------------+--------+
-- Output: 
-- +----------------+----------------+
-- | category       | accounts_count |
-- +----------------+----------------+
-- | Low Salary     | 1              |
-- | Average Salary | 0              |
-- | High Salary    | 3              |
-- +----------------+----------------+
-- Explanation: 
-- Low Salary: Account 2.
-- Average Salary: No accounts.
-- High Salary: Accounts 3, 6, and 8.

select 'Low Salary' as category, count(account_id) as accounts_count
from accounts
where income < 20000
union
select 'Average Salary' as category, count(account_id) as accounts_count
from accounts
where income between 20000 and 50000
union
select 'High Salary' as category, count(account_id) as accounts_count
from accounts
where income > 50000;

