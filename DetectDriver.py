import pyodbc

driver_name = [x for x in pyodbc.drivers()]

for x in driver_name:
    print(x)