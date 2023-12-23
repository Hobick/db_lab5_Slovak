import psycopg2
from init import get_pass
import matplotlib.pyplot as plt

username = 'postgres'
password = get_pass()
database = 'db_lab3'
host = 'localhost'
port = '5432'
#Також створена копія цих перерізів для початкових таблиць (без _new)
query_create = '''
create view HeroNumberByAttribute as select attribute, count(*) from hero_new
group by attribute;
create view HeroNumberByAttackType as select attack_type, count(*) from hero_new
group by attack_type;
create view PossibleRolesNumberByAttribute as select attribute, count(*) from play_role_new, hero_new
where hero_new.name = play_role_new.name
group by attribute;
'''
#Додаючи _new можна отримати графіки для повної бази даних
query_1 = '''
select * from HeroNumberByAttribute;
'''
query_2 = '''
select * from HeroNumberByAttackType;
'''

query_3 = '''
select * from PossibleRolesNumberByAttribute;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()

    cur.execute(query_1)

    total = []
    att = []
    for row in cur:
        att.append(row[0])
        total.append(row[1])

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(att, total, label='Total')
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(att)

    bar_ax.set_xlabel('Атрибути')
    bar_ax.set_ylabel('Кількість')
    bar_ax.set_title('Кількість героїв кожного атрибуту')

    cur.execute(query_2)

    total = []
    for row in cur:
        total.append(row[1])
    
    pie_ax.pie(total, autopct='%1.1f%%')
    pie_ax.set_title('Частка героїв ближнього/дальнього бою')

    cur.execute(query_3)

    att = []
    quan = []

    for row in cur:
        att.append(row[0])
        quan.append(row[1])
    
    graph_ax.plot(att, quan, marker='o')
    graph_ax.set_xlabel('Атрибут')
    graph_ax.set_ylabel('Кількість ролей')
    graph_ax.set_title('Графік залежності кількості ролей від атрибуту')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()