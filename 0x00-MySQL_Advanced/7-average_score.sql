-- MysSQL script that creates a stored procedure
-- computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;

    SELECT SUM(score) INTO total
    FROM corrections
    WHERE corrections.user_id = user_id;

    SELECT COUNT(*) INTO cnt
    FROM corrections
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = IF(cnt = 0,0, total / cnt)
    WHERE id = user_id;
END; //
DELIMITER ;
