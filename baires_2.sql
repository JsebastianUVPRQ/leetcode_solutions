-- given the following database tables:
-- users(id_User, Name)
-- logins_system(id_User, Date_time)

-- Write a stored procedure or MySQL query that creates a report for 
-- the current year with the following columns:

-- | Date (DD/MM/YYYY) | User name | Number of logins per day |
-- query:
SELECT DATE_FORMAT(ls.Date_Time, '%d%m%Y') AS Date, u.Name AS 'User name', COUNT(ls.Id_User) AS 'Number of logins per day'
FROM logins_system ls
JOIN users u ON ls.Id_User = u.Id_User
WHERE YEAR(ls.Date_Time) = YEAR(CURDATE())

SELECT DATE_FORMAT(ls.Date_Time, '%d%m%Y') AS Date,
       u.Name AS 'User name',
       COUNT(ls.Id_User) AS 'Number of logins per day'
       
FROM logins_system ls
JOIN users u ON ls.Id_User = u.Id_User
WHERE YEAR(ls.Date_Time) = YEAR(CURDATE())
GROUP BY DATE_FORMAT(ls.Date_Time, '%d%m%Y'), u.Name;
