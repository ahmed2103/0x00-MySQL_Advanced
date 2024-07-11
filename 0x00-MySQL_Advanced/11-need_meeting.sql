-- SQL script that creates a view need_meeting
 -- lists all students that have a score under 80 (strict) and
-- no last_meeting or more than 1 month.
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80
AND (last_meeting < SUBDATE(CURDATE(), INTERVAL 1 MONTH) OR students.last_meeting IS NULL);
