 /*
 +-------------+------+
 | Column Name | Type |
 +-------------+------+
 | teacher_id  | int  |
 | subject_id  | int  |
 | dept_id     | int  |
 +-------------+------+
 (subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
 Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
  
 
 Write a solution to calculate the number of unique subjects each teacher teaches in the university.
 
 Return the result table in any order.
 
 The result format is shown in the following example.
*/ 
Select teacher_id, count(distinct subject_id) as subject_count
from subjects_by_teacher
group by teacher_id


-- -------------------------------------------------------

-- --------------------------------------------------  --------------------------------------

/* -------------------------------------------------------
Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
 

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
 

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
*/

SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id