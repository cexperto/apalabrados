from create_table import *
from sqlalchemy import *

query_acumulated= connection.execute('SELECT count(id_n)+1 FROM numbers')
for row in query_acumulated:
    data = row[0]     
print(data)