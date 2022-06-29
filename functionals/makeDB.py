
'''Allows you to create a MySQL database & tables without the need to do so...
       You just need to provide credentials (but skipping them will use the default '''

def prereq(database = None
           ) -> tuple:
    '''Initializes the DB setup'''
    import mysql.connector

    dbconfig = {'host': '127,0,0,1',
                'user': 'root',
                'password': 'Manofaction.1', }

    if database: dbconfig.update({'database':database})

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    return (conn,cursor)

def createDB(newDBname, username: 'user', password = 'Manofaction.1', save = True) -> None:
    conn, cursor = prereq()
    SQl = f'create database {newDBname};'
    _SQL = f"grant all on {newDBname}.* to '{username}' identified by '{password}';"
    cursor.execute(SQL)
    cursor.execute(_SQL)
    conn.commit()
    cursor.close()
    conn.close()

    if save and __name == '__main__':
        with open(f'{newDBname}info.txt','w') as info:
            info.write(f'''database: {newDBname}
                           user: {username}
                           password: {password}''')


def create_table(dbname, tabname, fields: dict, id_ts = True) -> None:
    '''Creates the table from the supplied values:
    dbname:  Name of the database to create table in
    tabname: Name for the created table
    fields:  A dict of field_name(key , heading) & varchar_values(value)
    id_ts:   Automativally add serial no. & timestamp as 2 starting fields'''

    prifields = '''id int auto_increment primary key,
                   ts timestamp default current_timestamp,'''

    id_ts = prifields if id_ts else None 

    _sql = f'create table {tabname} (\n {id_ts} \n'
    for field, vc in fields.items():
         _sql += f'\n{field} varchar({vc}) not null,'

    _sql += ' );'
    
    conn, cursor = prereq(dbname)
    cursor.execute(_sql)
    conn.commit()
    cursor.close()
    conn.close()
