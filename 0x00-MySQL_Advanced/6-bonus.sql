-- MysSQL cript that creates a stored procedure AddBonus
-- that adds a new correction for a student.

DROP TRIGGER IF EXISTS AddBonus;
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT)
BEGIN
    DECLARE pro_id INT;

    SELECT id INTO pro_id
    FROM projects
    WHERE project_name = name;

    IF pro_id IS NULL THEN
        INSERT INTO projects (name) VALUE (project_name);
        SET pro_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, pro_id, score);
end; //
DELIMITER ;
