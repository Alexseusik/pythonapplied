import sqlite3

'''
The structure of database is 4 tables: type, sort, tree_info, harvset_info
type : type
sort : sort, type (foreign key for table type)
tree_info : id, type, sort, year, place
harvest_info : id, tree_id, harvest_year (calculated at the end of the season)
'''

db = 'database.db'

conn = sqlite3.connect(db)
cur = conn.cursor()

# print([item[0] for item in cur.execute('select * from type')])


def adding_type_to_db():
    user_input_type = input('Введіть рід дерева, який треба додати:  ')
    if user_input_type in [item[0] for item in cur.execute('select * from type')]:
        print('Такий рід дерев вже існує у базі!')
    else:
        cur.execute('insert into type(type) values (?)', (user_input_type, ))
        conn.commit()
        conn.close()


def adding_sort_to_db():
    user_input_type, user_input_sort = input('Введіть рід та сорт дерева через пробіл, який треба додати:  ').split()

    check_type = bool([el[0] for el in cur.execute('''select * from type where type = ? ''', (user_input_type, ))])
    # True if type exist in type, False if not exist ^

    check_sort = bool([el[0] for el in cur.execute('''select * from sort where sort = ? and type = ? ''',
                                                   (user_input_sort,
                                                    user_input_type))])
    # True if sort exist in sort, False if not exist ^

    if check_type is True:
        print(f'Рід дерев {user_input_type} знайдено у базі!')
        if check_sort is True:
            print(f'Сорт {user_input_sort} роду {user_input_type} вже існує у базі!')
        else:
            cur.execute('''insert into sort(type, sort) values (?, ?)''', (user_input_type,
                                                                           user_input_sort))
            print(f'Додано сорт {user_input_sort} роду {user_input_type} до бази!')
    else:
        print(f'Рід дерев {user_input_type} не знайдено у базі :(')

    conn.commit()
    conn.close()


def adding_tree_to_db():
    user_input_tree_id, user_input_tree_type, user_input_tree_sort, user_input_tree_year, user_input_tree_place\
        = input('Введіть id, рід, сорт, рік посадки, місце посадки дерева через пробіл, який треба додати:  ').split()
    check_type = bool([el[0] for el in cur.execute('''select * from type where type = ? ''', (user_input_tree_type,))])
    check_sort = bool([el[0] for el in cur.execute('''select * from sort where sort = ? and type = ? ''',
                                                   (user_input_tree_sort, user_input_tree_type))])

    if (check_type is True) and (check_sort is False):
        print(f'{user_input_tree_sort} сорту {user_input_tree_type} роду не існує, треба додати до бази!')
    else:
        print(f'{user_input_tree_sort} сорту {user_input_tree_type} роду існує, додаємо дані дерева до бази!')
        try:
            cur.execute('''insert into tree_info(id, type, sort, year, place) values(?, ?, ?, ?, ?)''',
                        (user_input_tree_id,
                         user_input_tree_type,
                         user_input_tree_sort,
                         user_input_tree_year,
                         user_input_tree_place))
        except sqlite3.Error as e:
            print(e)
    conn.commit()
    conn.close()


def adding_harvest_to_db():
    for row in cur.execute('''select * from tree_info'''):
        print(row)
    print('\nУгорі дерева які вже є у базі даних\n')
    user_input_harvest_id, user_input_tree_id, user_input_year, user_input_amount\
        = input('Введіть id врожаю, id дерева, рік врожаю, кількість врожаю який треба додати:  ').split()
    check_tree = bool([el[0] for el in cur.execute('''select * from tree_info where id == ? ''',
                                                   (user_input_tree_id,))])
    if int(user_input_harvest_id) in [el[0] for el in cur.execute('''select id from harvest_info''')]:
        print('Такий id вже існує, створюю інший . . .')
        user_input_harvest_id = [el[0] for el in cur.execute('''select id from harvest_info''')][-1] + 1
    if check_tree is True:
        print(f'Дерева з id = {user_input_tree_id} знайдені ')
        all_trees = [row for row in cur.execute('''select * from tree_info where id == ? ''', (user_input_tree_id,))]
        print(all_trees)
        cur.execute('''insert into harvest_info(id, tree_id, year, amount) values (?, ?, ?, ?)''', (
            user_input_harvest_id, user_input_tree_id, user_input_year, user_input_amount
        ))
        print(f'Врожай дерева {user_input_tree_id} за {user_input_year} рік додано до бази!')
    else:
        print(f'Дерева з id = {user_input_tree_id} не знайдено :(')
    conn.commit()
    conn.close()


def all_trees_of_same_type():
    pass


adding_harvest_to_db()
