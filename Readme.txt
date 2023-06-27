# Codebase to test connect to various RDBMS and Data sources #

1. All the methods are tested and able to connect
2. In config file fill up the data source login details by removing the tags
3. Make sure that the values in config are not in string 
4. Assuming you have the respective ODBC databases and ready to connect
4. To test connect for Snowflake, free account is been created
6. Make sure your provide the proper snowflake account < account identifier > 
        Not the .snowflake.computing.com or the https endpoints
5. Using pyodbc package accessing of all the ODBC databases is done

NOTE ->>>>  Make sure all the necessary drivers are installed and databases up ready 
            Enter values between 1 to 4 to invoke each methods

Public free FTP soruce ->> https://www.filestash.app/free-ftp.html
Snowflake Free account ->> https://www.snowflake.com/login/

Drivers ->>>    Oracle      ->> https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html#ic_winx64_inst
                Snowflake   ->> https://docs.snowflake.com/en/developer-guide/odbc/odbc
                Teradata    ->> https://downloads.teradata.com/download/connectivity/odbc-driver/windows