-- MySQL  script that creates a stored procedure that computes and
-- store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE cnt INT DEFAULT 0;
    DECLARE wighted_sum FLOAT DEFAULT 0;
    DECLARE w_avg FLOAT DEFAULT 0;
    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    INTO wighted_sum, cnt
    FROM corrections
    JOIN projects on projects.id = corrections.project_id
    WHERE corrections.user_id = user_id;
    IF cnt > 0 THEN
        SET w_avg = wighted_sum / cnt;
    ELSE
        SET w_avg = 0;
    END IF;
    update users
    SET average_score = w_avg
    WHERE users.id = user_id;
END; //
DELIMITER ;
