# coding: utf-8
"""
Parsear el log de apache y convertirlo en una tabla de Hive
"""
from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd

conn= connect(host='sandbox.hortonworks.com', port=10000, auth_mechanism='PLAIN', user='hive', password='hive', database = 'default')

cursor = conn.cursor()

p = []

cursor.execute('select * from practica.demografico limit 100')
for row in cursor:
    p = row
    print p

"""
cursor.execute('create table practica.log_ctas2 as select * from ejemplo.logs')

cursor.execute('select * from practica.log_ctas2 limit 100')
for row in cursor:
    p = row
    print p

cursor.execute('create temporary table practica.log_ctas_temp as select * from ejemplo.logs')

cursor.execute('select * from ejemplo.log_ctas_temp limit 5')
for row in cursor:
    p = row
    print p


cursor.execute('drop table practica.log_ctas_temp')



cursor.execute('select count(*) total, b.education, c.product_name from practica.reln_cust_prod a inner join foodmart.customer b on a.customer_id = b.customer_id inner join foodmart.product c on c.product_id = a.product_id where c.low_fat group by  b.education, c.product_name order by total desc limit 10')

df = as_pandas(cursor)

df.describe()

df
"""