import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=dsckoresql;"
                      "Database=BSDW_2;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()

