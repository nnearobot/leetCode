# 182. Duplicate Emails
# Easy
# https://leetcode.com/problems/duplicate-emails

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1

# SELECT p2.email
# FROM (SELECT p1.email, COUNT(*) as count FROM Person p1 GROUP BY p1.email) as p2
# WHERE p2.count > 1