-- MySQL script that creates a stored procedure that
-- computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE user_id INT;
    DECLARE done INT DEFAULT 0;
    DECLARE cnt INT DEFAULT 0;
    DECLARE wighted_sum FLOAT DEFAULT 0;
    DECLARE w_avg FLOAT DEFAULT 0;

    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;

    cursor_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE cursor_loop;
        end if;

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
    END LOOP;

    CLOSE user_cursor;

END; //
DELIMITER ;
