import psycopg2
host_name = "localhost"
data_base = "school"
user_name = "postgres"
password = "123456"
port_id = 5432
conn = psycopg2.connect(host = host_name, dbname = data_base, user = user_name, password = password, port = port_id)
cur = conn.cursor()

def print_all(cur):
    cur.execute("select * from teachers")
    for record in cur.fetchall():
        print(record[1], record[2], record[3])

def insert_list(list, cur):
    insert_query = '''
    insert into teachers (
    id, name, salary, grade) values(
    %s, %s, %s, %s)
    '''
    for v in list:
      cur.execute(insert_query, v)

def update_age_grade(id, cur):
    id = str(id)
    update_query = "update teachers set salary = salary + 100, grade = grade + 1 where id = " + id
    cur.execute(update_query)

print_all(cur)
list = [(5, "Zeinab", 66789, 7), (6, "Sara", 568, 5)]
#insert_list(list, cur)
print_all(cur)
update_age_grade(5, cur)
print_all(cur)

conn.commit()
cur.close()
conn.close()