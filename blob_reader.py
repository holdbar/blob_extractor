import pyodbc

server = 'localhost'
base = 'intimedemo'
user = 'sa'
password = ''

con = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+base+';UID='+user+';PWD='+password)

print('1')

cursor = con.cursor()

param = '343531'

query = 'select filedata from attachments where sourceid = %s'

res = cursor.execute(query % (param, ))

print('2')

out = res.fetchone()[0]

with open('blob', 'wb') as f:
        f.write(out)

print('end')

cursor.close()

del cursor

con.close()
