-- Script que crea la función SafeDiv
-- Divide el primer número por el segundo o devuelve 0 si el segundo es 0
DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
