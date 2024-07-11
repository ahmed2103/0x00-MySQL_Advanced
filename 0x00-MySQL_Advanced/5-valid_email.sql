-- Create the trigger to reset valid_email if the email has been changed
DROP TRIGGER IF EXISTS email_validation;
DELIMITER //

CREATE TRIGGER email_validation
BEFORE UPDATE ON users  -- AHAH! logic is the logoic Atomicity,consistency,va!
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; //

DELIMITER ;
