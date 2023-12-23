import csv
from init import get_pass
import psycopg2

username = 'postgres'
password = get_pass()
database = 'db_lab3'

OUTPUT_FILE_T = 'Slovak_DB_{}.csv'

TABLES = [
    'hero_new',
    'play_role_new',
    'role_new',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])