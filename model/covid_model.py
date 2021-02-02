import csv
import sqlite3

"""Limits the number of data saved in db. If it's false it will save all in db if True it will only every 1000"""
only_partial_data = False
"""every_number_data, every n number elements will be added"""
every_number_data = 100
"""The name of the file containing the data"""
file_name = 'InternationalCovid19Cases.csv'
"""The name of the sqlite3 connection"""
connection = sqlite3.connect('_covid.db_')
"""The cursor used to run sql statements"""
cursor = connection.cursor()
"""The name of the table"""
table_name = 'covid'
"""The create statement"""
create_statement = 'CREATE TABLE if not exists ' + table_name \
                   + ' (country_id text, date text, cases INTEGER, deaths INTEGER, name_fr text, name_en text)'
"""The drop statement"""
drop_statement = 'DROP TABLE IF EXISTS ' + table_name
"""The insert statement"""
insert_statement = 'INSERT INTO ' + table_name \
                   + ' (country_id, date, cases, deaths, name_fr, name_en) ' \
                     'VALUES (?, ?, ?, ?, ?, ?)'
"""The select all statement"""
select_all_statement = 'SELECT rowid, * from ' + table_name
"""The select by id statement"""
select_id_statement = 'SELECT rowid, * FROM ' + table_name + ' WHERE rowid = ?'
"""The delete statement"""
delete_statement = 'DELETE FROM ' + table_name + ' where rowid = ?'
"""The update statement"""
update_statement = 'UPDATE ' + table_name + ' set country_id = ?, date = ?, cases = ?, ' \
                                            'deaths = ?, name_fr = ?, name_en = ? where rowid = ?'
order_by_statement = select_all_statement + ' ORDER BY '


def get_list():
    """
    returns the list used to store the data
    """
    cursor.execute(select_all_statement)
    return cursor.fetchall()


def get_ordered_list(columns, desc):
    """
    Runs an order by statement phrased using columns to order by, and a flag to determine ascending/descending
    :param columns: the list of columns we are sorting by
    :param desc: true if descending, false if ascending
    """
    statement = (order_by_statement + generate_order_by(columns)) % tuple(columns)
    if desc:
        statement += ' DESC'
    else:
        statement += ' ASC'

    print(statement)
    cursor.execute(statement)
    return cursor.fetchall()


def get_size():
    """
    returns the size of the list
    """
    return len(get_list())


def create_table():
    """
    Creates Table
    """
    cursor.execute(create_statement)
    commit()


def initialize_list():
    """
    Initializes the data by reading the data file
    The maximum amount of entries that will be stored is 100
    It will reset any current values in the table
    """
    reset_db()
    try:
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)
            index = 1
            for row in reader:
                index += 1
                if only_partial_data:
                    if index % every_number_data == 0:
                        add(row['id'], row['date'], row['cases'], row['deaths'], row['name_fr'], row['name_en'])
                else:
                    add(row['id'], row['date'], row['cases'], row['deaths'], row['name_fr'], row['name_en'])
            commit()
    except FileNotFoundError:
        return False
    return True


def add(country_id, date, cases, deaths, name_fr, name_en):
    """
    Adds an element to the list
    """
    cursor.execute(insert_statement, (country_id, date, cases, deaths, name_fr, name_en))


def delete(rowid):
    """
    Deletes an element from the list
    Doesn't run if the list is empty
    :param rowid: id of the element to be deleted
    """
    if select_by_id(rowid) is True:
        cursor.execute(delete_statement, rowid)
    commit()


def select_by_id(rowid):
    """
    returns True if the rowid is in the table
    """
    cursor.execute(select_id_statement, rowid)
    return cursor.fetchone() is not None


def update(country_id, date, cases, deaths, name_fr, name_en, rowid):
    """
    Calls the sql update statement using the parameters passed in
    """
    cursor.execute(update_statement, (country_id, date, cases, deaths, name_fr, name_en, rowid))
    commit()


def commit():
    """
    Commits the transaction
    """
    connection.commit()


def close():
    """
    Closes the database connection
    """
    connection.close()


def reset_db():
    """
    Resets the table by dropping and recreating the table
    """
    cursor.execute(drop_statement)
    cursor.execute(create_statement)
    commit()


def generate_order_by(columns):
    """
    :param columns: This list of columns to be part of the order by statement
    :type columns: 
    :return: Returns marks based on how many columns for example 1 = '%s', 2 = '%s, %s'
    """
    return_statement = '%s'
    if len(columns) == 1:
        return return_statement

    for x in range(1, len(columns)):
        return_statement += ', %s'
    return return_statement
