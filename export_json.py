import json
from init import get_pass
import psycopg2

username = 'postgres'
password = get_pass()
database = 'db_lab3'


conn = psycopg2.connect(user=username, password=password, dbname=database)

data = {}
with conn:

    cur = conn.cursor()
    
    for table in ('hero_new', 'play_role_new',  'role_new',):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default = str)
    