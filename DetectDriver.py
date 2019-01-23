import pyodbc

driver_name = [x for x in pyodbc.drivers()]

print(driver_name)