-- MySQL to create a division funcion that refuse 0 as divider.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
    RETURN a / b;
    END IF;
END;
DELIMITER ;
