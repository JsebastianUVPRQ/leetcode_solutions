/*Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.

 

Example 1:

Input: 
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output: 
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation: 
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.


-- --------------------- MySql----------------------- */
WITH 
cte1 AS (
    SELECT requester_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY requester_id
),
cte2 AS (
    SELECT accepter_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
),
cte3 AS (
    SELECT id, num FROM cte1
    UNION ALL
    SELECT id, num FROM cte2
)

SELECT id, SUM(num) AS num
FROM cte3
GROUP BY id
ORDER BY num DESC

-- ----------------------------------- oracle ---------------------
WITH CombinedFriends AS (
    SELECT requester_id AS id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend_id
    FROM RequestAccepted
)
SELECT * FROM CombinedFriends;

WITH CombinedFriends AS (
    SELECT requester_id AS id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendCounts AS (
    SELECT id, COUNT(DISTINCT friend_id) AS num
    FROM CombinedFriends
    GROUP BY id
)
SELECT * FROM FriendCounts ORDER BY num DESC;

WITH CombinedFriends AS (
    SELECT requester_id AS id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendCounts AS (
    SELECT id, COUNT(DISTINCT friend_id) AS num
    FROM CombinedFriends
    GROUP BY id
),
RankedFriends AS (
    SELECT id, num
    FROM FriendCounts
    ORDER BY num DESC
)
SELECT id, num
FROM (
    SELECT id, num, ROWNUM AS r
    FROM RankedFriends
)
WHERE r = 1;
