import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

user_input
if user_input_harvest_id in [el[0] for el in cur.execute('''select id from harvest_info''')]:
    print('Такий id вже існує, створюю інший . . .')
    user_input_harvest_id = [el[0] for el in cur.execute('''select id from harvest_info''')][-1] + 1

