
def update_queries():
    procedure_py1="""CREATE
        PROCEDURE
        updatetables(IN
        tab_name
        VARCHAR(40), IN a VARCHAR(40), IN b varchar(40), c varchar(40), d varchar(40))
        BEGIN
            SET @ t1 = CONCAT("update table ", tab_name, " set ", b, "=", d, " where ", a, "=", c);
        PREPARE
            stmt3 FROM @ t1;
        EXECUTE stmt3;
        DEALLOCATE
        PREPARE
        stmt3;
        END$$"""
    return procedure_py1
