import csv
from init import get_pass
import psycopg2

username = 'postgres'
password = get_pass()
database = 'db_lab3'

INPUT_CSV_FILE = 'Current_Pro_meta.csv'

query_hero00 = '''
DROP TABLE IF EXISTS hero_new CASCADE
'''
query_play_role00 = '''
DROP TABLE IF EXISTS play_role_new CASCADE
'''
query_role00 = '''
DROP TABLE IF EXISTS role_new CASCADE
'''

query_hero0 = '''
CREATE TABLE hero_new
(
    Name CHAR(20) NOT NULL,
    Attribute CHAR(3) NOT NULL,
    Attack_type CHAR(10) NOT NULL,
    PRIMARY KEY (Name)
)
'''
query_play_role0 = '''
CREATE TABLE play_role_new
(
    Name CHAR(20) NOT NULL,
    Role_name CHAR(20) NOT NULL,
    PRIMARY KEY (Name, Role_name),
    FOREIGN KEY (Name) REFERENCES Hero_new(Name),
    FOREIGN KEY (Role_name) REFERENCES Role_new(Role_name)
)
'''
query_role0 = '''
CREATE TABLE Role_new
(
  Role_name CHAR(20) NOT NULL,
  PRIMARY KEY (Role_name)
);
'''

query_hero1 = '''
DELETE FROM hero_new
'''
query_play_role1 = '''
DELETE FROM play_role_new
'''
query_role1 = '''
DELETE FROM role_new
'''

query_hero2 = '''
INSERT INTO hero_new (name, attribute, attack_type) VALUES (%s, %s, %s)
'''
query_play_role2 = '''
INSERT INTO play_role_new (name, role_name) VALUES (%s, %s)
'''
query_role2 = '''
INSERT INTO role_new (role_name) VALUES (%s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_hero00)
    cur.execute(query_hero0)
    cur.execute(query_role00)
    cur.execute(query_role0)
    cur.execute(query_play_role00)
    cur.execute(query_play_role0)
    
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        roles = []
        for idx, row in enumerate(reader):
            print(idx)
            hero_values = (row['Name'], row['Primary Attribute'], row['Attack Type'])
            cur.execute(query_hero2, hero_values)
            for role in row['Roles'].split(', '):        
                if role not in roles:
                    cur.execute(query_role2, [role])
                    roles.append(role)
                play_role_values = (row['Name'], role)
                cur.execute(query_play_role2, play_role_values)
            

    conn.commit()