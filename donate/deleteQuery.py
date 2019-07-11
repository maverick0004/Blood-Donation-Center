def delete_query(request):
    procedure_py1="""CREATE PROCEDURE delete(IN tab_name VARCHAR(40),IN a VARCHAR(40), IN b varchar(40))
    BEGIN
        SET @t1 =CONCAT("delete from table ",tab_name," where ",a,"=",c);
        PREPARE stmt3 FROM @t1;
        EXECUTE stmt3;
        DEALLOCATE PREPARE stmt3;
    END"""
    return procedure_py1