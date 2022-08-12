import logging
import sqlite3 
import sys
from xml.etree.ElementTree import tostring

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def explore_table(conn,table):
    """
    explore_table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute('''
                PRAGMA table_info('%s');
                '''
                %(table)
)
    rows = cur.fetchall()


    for row in rows:
        print(row)
        
    return rows

def create_table_command_sqlite(table):
    """
    explore_table
    :param conn: the Connection object
    :return:
    """
    return " \
                CREATE TABLE IF NOT EXISTS '%s' ( \
                    _id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE \
                );\n" \
                %(table)

def add_column_command_sqlite(table,column_name,column_type='TXT'):
    """
    explore_table
    :param conn: the Connection object
    :return:
    """
    return " \
                ALTER TABLE '%s' \
                ADD '%s' %s; \
                \n" \
                %(table,column_name,column_type)



def search_varname_exists(conn,table, varname):
    """
    search_varname
    :param conn: the Connection object
    :return:
    """
    column_of_varname = 1

    rows = explore_table(conn,table)
    list_of_items = [row[column_of_varname] for row in rows]
    
    if varname is not list:
        varname = [varname]
    else :
        if varname.count() != 1:
            print('Error')
            
    result = len(list(set(list_of_items).intersection(set(varname)))) == 1
    
    
    return result
    


def select_all_tasks(conn,table):
    """
    Query all rows in the table 'table'
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM '%s'"%( table ))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def search_dicts_in_dict(a_dictionary,skey=[], maintablename='activities'):
    """ Dig in a dictionary to search and find all dictionaries
    
    Parameters
    ----------
    a_dictionary : a dictionary

    Returns
    ----------
    result : a list built like a tree in which we find  ditionaries

    Example : 
     ----------
    test_dict= {'C':{'G':20,'R':['O','P']}}

    logger.info(test_dict)

    ## search and find dictionaries 
    logger.info(rmdc.search_dicts_in_dict(test_dict))


    Results : 
    ----------
    INFO:__main__:{'C': {'G': 20, 'R': ['O', 'P']}}
    INFO:__main__:[['C']]


    """    
    result = []
    for key in a_dictionary.keys():
        selected_value = a_dictionary[key]
        if type(selected_value) is dict :
            found_key = [key]
            result.append(found_key)
            
            rerun = search_dicts_in_dict(selected_value,key)
            if rerun != [] : found_key.append(rerun)
    
    return result  

def search_dictionaries_lists_tuples_in_dict_sql(a_dictionary,skey=[]):
    """ Dig in a dictionary to search and find all dictionaries, lists and tuples
    
    Parameters
    ----------
    a_dictionary : a dictionary

    Returns
    ----------
    ???

    Example : 
    ----------
    ???

    Results : 
    ----------
    ???
    """
    result_dict = []
    result_list = []
    result_tuple = []

    sql_commands =str("")

    data_type_in_base_dictionary = {}


    tdict = a_dictionary.keys()

    kdict = list(tdict)
    for key in kdict:
        selected_value = a_dictionary[key]
        if type(selected_value) is dict :
            found_key = [key]
            result_dict.append(found_key)
            
            # digger
            # recursion is not infinite
            skey.append(key)
            rerun,lists,tuples = \
                search_dictionaries_lists_tuples_in_dict_sql(selected_value,skey)
            
            if rerun != [] : 
                found_key.append(rerun)  
                
            if lists!=[]:
                result_list.append(lists)
                
            if tuples!=[]:
                result_tuple.append(tuples)
            
                
        elif type(selected_value) is list: 
            result_list.append(key)
        elif type(selected_value) is tuple: 
            result_tuple.append(key)
        elif type(selected_value) is int:
            logger.info(str(skey) + str(':') + str(key)  + str(':')  + str(selected_value) + str(type(selected_value)) + \
                'INTEGER Found')
        elif type(selected_value) is str:
            logger.info(str(skey) + str(':') + str(key)  + str(':')  + str(selected_value) + str(type(selected_value))+ \
                'STRING Found')
        elif type(selected_value) is float:
            logger.info(str(skey) + str(':') + str(key)  + str(':')  + str(selected_value) + str(type(selected_value)) + \
                'REAL Found')
        else :
            logger.warning(str(skey) + str(':') + str(key)  + str(':')  + str(selected_value) + str(type(selected_value)) + \
                'Unsupported format')


        ## start to produce sql
        if result_dict == [] and kdict[len(kdict)-1] == key :
            logger.info(str(skey) + str(':') + str(key)  + str(':')  + " NO_DICT_IN : " +  str(skey) + ":"+str(a_dictionary))
            table_name = str(skey[len(skey)-1])
            sql_commands += create_table_command_sqlite(table_name)
            for keyi in range(len(kdict)):

                data_type_in_base_dictionary[kdict[keyi]] = a_dictionary[kdict[keyi]].__class__.__name__           

                if type(a_dictionary[kdict[keyi]]) is str: 
                    #add date, int, float
                    sql_commands += add_column_command_sqlite(table_name,kdict[keyi],column_type='TXT')
                elif  type(a_dictionary[kdict[keyi]]) is int:    
                    sql_commands += add_column_command_sqlite(table_name,kdict[keyi],column_type='INTEGER')
                elif  type(a_dictionary[kdict[keyi]]) is float:    
                    sql_commands += add_column_command_sqlite(table_name,kdict[keyi],column_type='REAL')
                elif  type(a_dictionary[kdict[keyi]]) is list:    
                    sql_commands += add_column_command_sqlite(table_name,kdict[keyi],column_type='TXT') # no array in sqlite !!!
                elif  type(a_dictionary[kdict[keyi]]) is tuple:    
                    sql_commands += add_column_command_sqlite(table_name,kdict[keyi],column_type='TXT') # no array in sqlite !!!
            
            logger.info("DATA_TYPE : " + str(data_type_in_base_dictionary) )
            sql_commands += add_column_command_sqlite(table_name,'_PYTHON_DATA_TYPE',column_type='TXT')

            logger.info(sql_commands)

# BASE_ENCODE = 'utf-8'

# C= {'a':{'b':2,'c':4}}
# strc = str(C).encode(BASE_ENCODE)
# print(strc)
# d = eval(strc.decode(BASE_ENCODE))
# print(type(d))
# print(d)

# E= [['R']]
# stre=str(E).encode(BASE_ENCODE)
# print(stre)
# f = eval(stre.decode(BASE_ENCODE))
# print(type(f))
# print(f)
# 
       
## https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.create_function
## https://www.sqlitetutorial.net/sqlite-foreign-key/
    return result_dict,result_list,result_tuple
