-- ---------------------MySql-----------------------
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

-- -----------------------------------oracle ---------------------
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
