# Codebase to test connect to various ODBC/JDBC and Data sources #

import pyodbc
import ftplib
import configparser
import pandas as pd
import snowflake as sf
from snowflake import connector

# To set the configparser to read login credientials from config files #
config = configparser.ConfigParser()
config.read("config.ini")

# 1. Method to test connect to teradata #
def teradata():
    print("Teradata Test Connect")
    conn = "DRIVER={drivername};DBCNAME={host};port={port};UID={username};PWD={password}".format(
                        drivername = config['teradata']['drivername'],
                        host = config['teradata']['host'],
                        port = config['teradata']['port'],
                        username = config['teradata']['username'],
                        password = config['teradata']['password'])                                                     
    try:
        con = pyodbc.connect(conn)
        print("Test Connect Success")
        pd.read_sql_query("select '1'", con)   
        con.close()
        print("Test Connect Closed")
    except pyodbc.Error as e:
        print(e)


# 2. Method to test connect to oracle #
def oracle():
    print("Oracle Test Connect")
    conn = "DRIVER={drivername};DBQ={host}:{port}/{sid};UID={username};PWD={password}".format(
                            drivername = config['oracle']['drivername'],
                            host = config['oracle']['host'],
                            port = config['oracle']['port'],
                            sid = config['oracle']['sid'],
                            username = config['oracle']['username'],
                            password = config['oracle']['password'])
    try:
        con = pyodbc.connect(conn)
        print("Test Connect Success")
        con.close()
        print("Test Connect Closed")
    except pyodbc.Error as e:
        print(e)


# 3. Method to test connect to snowflake #
def snowflake():
    print("Snowflake Test Connect")
    conn = sf.connector.connect(account = config['snowflake']['account'],
                            user = config['snowflake']['username'],
                            password = config['snowflake']['password'],
                            warehouse = config['snowflake']['warehouse'])
    print("Snwoflake Connect Success")
    cur = conn.cursor()
    result = cur.execute("show databases")
    result_list = result.fetchall()
    print(result_list)
    conn.cursor().close()
    print("Test Connect Closed")
    

# 4. Method to test connect to ftp #
def ftp():
    print("FTP Test Connect")
    file_path = config['ftp']['file_path']
    filename = config['ftp']['filename']
    try:
        ftp = ftplib.FTP(host = config['ftp']['host'], user = config['ftp']['username'], passwd = config['ftp']['password'])
        print("FTP Connection Successful")
    except ftplib.error_perm:
        print("FTP Connection Error")
    ftp.cwd(file_path)
    ftp.set_pasv(False)
    if filename in ftp.nlst():
        print("FTP File fetched")
    else:
        print("FTP File Not there")
    return ftp


# Codeblock to trigger each data source #
val = int(input("Enter the value 1 to 4: "))
print(val)
if val == 1:
    connect = teradata()
elif val == 2:
    connect = oracle()
elif val == 3:
    connect = snowflake()
else:
    connect = ftp()