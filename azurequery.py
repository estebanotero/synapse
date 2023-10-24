import pyodbc

server = 'myfreedbserver77.database.windows.net'
database = 'myFreeDB'
username = 'esteban'
password = 'Italia90'
driver= '{ODBC Driver 17 for SQL Server}'

# Create a connection string
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
conn = pyodbc.connect(conn_str)

# Create a cursor
cursor = conn.cursor()

# Execute a query
cursor.execute('SELECT * FROM [dw].[Tipo_de_cambio]')

# Fetch the results
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()
