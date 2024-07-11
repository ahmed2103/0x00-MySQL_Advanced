-- Create the trigger to decrease the quantity of
-- an item after adding a new order
DROP TRIGGER IF EXISTS decrement_quant;
DELIMITER //

CREATE TRIGGER decrement_quant
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;
END; //

DELIMITER ;
