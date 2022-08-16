import logging
import sqlite3

from types import NoneType

from dateutil.parser import parse

import random
import string

import numpy as np


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def random_char(len):
    """
    :param XXX: XXX
    :return: XXX
    """
    return "".join(random.choice(string.ascii_letters) for x in range(len))


def isfloat(num):
    """
    :param XXX: XXX
    :return: XXX
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def isdate(string, fuzzy=False):
    """
    :param XXX: XXX
    :return: XXX
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def generate_random_values(dictionary):
    """
    :param XXX: XXX
    :return: XXX
    """
    for i in range(len(dictionary)):
        for key in dictionary.keys():
            if type(dictionary[key]) is dict:
                dictionary[key] = generate_random_values(dictionary[key])
            elif type(dictionary[key]) is str:
                if dictionary[key].isdigit():
                    str(random.randint(a=-10, b=10))
                elif isfloat(dictionary[key]):
                    str(random.randint(a=-10, b=10))
                elif len(dictionary[key]) == 1:
                    random_char(1)
                else:
                    dictionary[key] = random_char(random.randint(a=1, b=10))
            elif type(dictionary[key]) is int:
                dictionary[key] = random.randint(a=-10, b=10)
            elif type(dictionary[key]) is float:
                dictionary[key] = random.randrange(-10, 10)
            elif type(dictionary[key]) is list:
                if (type(dictionary[key][0])) is str:
                    lenght = len(dictionary[key][0])
                    for i in range(len(dictionary[key])):
                        dictionary[key][i] = random_char(lenght)
                elif (type(dictionary[key][0])) is int:
                    lmin = np.min(dictionary[key])
                    lmax = np.max(dictionary[key])
                    for i in range(len(dictionary[key])):
                        dictionary[key][i] = random.randint(a=lmin, b=lmax)
                elif (type(dictionary[key][0])) is float:
                    lmin = np.min(dictionary[key])
                    lmax = np.max(dictionary[key])
                    for i in range(len(dictionary[key])):
                        dictionary[key][i] = random.randrange(a=lmin, b=lmax)

    return dictionary[key]


def create_connection(db_file):
    """
    :param XXX: XXX
    :return: XXX
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def explore_table(conn, table):
    """
    :param XXX: XXX
    :return: XXX
    """
    cur = conn.cursor()
    cur.execute(
        """
                PRAGMA table_info('%s');
                """
        % (table)
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    return rows


def create_table_command_sqlite(table_name, prefix="", suffix="", drop=False):
    """
    :param XXX: XXX
    :return: XXX
    """
    sup = ""
    if drop:
        sup = "DROP TABLE IF EXISTS '%s%s%s'; \n" % (prefix, table_name, suffix)

    return (
        "\
    %s\n\
    CREATE TABLE IF NOT EXISTS '%s%s%s' ( \n\
    __id_%s__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE \n\
    %s);\n"
        % (sup, prefix, table_name, suffix, prefix, table_name, suffix)
    )


def create_table_command_sqlite_from_list_keys(
    table_name, list_of_dict_keys, prefix="", suffix="_table", drop=False
):
    """
    :param XXX: XXX
    :return: XXX
    """
    foreign_commands = str()
    sup = ""
    if drop:
        sup = "DROP TABLE IF EXISTS '%s%s%s'; \n" % (prefix, table_name, suffix)

    for ilist in list_of_dict_keys:
        foreign_commands += (
            "\
        ,%s INTEGER /*dict*/\n"
            % (ilist)
        )

    for ilist in list_of_dict_keys:
        foreign_commands += (
            "\
        ,FOREIGN KEY (%s)  REFERENCES '%s%s%s' (__id_%s__) \n"
            % (ilist, prefix, ilist, suffix, ilist)
        )

    return (
        "\n\
    %s\n\
    CREATE TABLE IF NOT EXISTS '%s%s%s' ( \n\
    __id_%s__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE \n\
    %s\
    );\n"
        % (sup, prefix, table_name, suffix, table_name, foreign_commands)
    )


def add_column_command_sqlite(
    table, column_name, column_type="TXT", info="", prefix="", suffix="_table"
):
    """
    :param XXX: XXX
    :return: XXX
    """
    if info != "":
        info = f"/*{info}*/"
    return (
        "\
    ALTER TABLE '%s%s%s' \
    ADD '%s' %s; \
    %s\n"
        % (prefix, table, suffix, column_name, column_type, info)
    )


def search_varname_exists(conn, table, varname):
    """
    :param XXX: XXX
    :return: XXX
    """
    column_of_varname = 1

    rows = explore_table(conn, table)
    list_of_items = [row[column_of_varname] for row in rows]

    if varname is not list:
        varname = [varname]
    else:
        if varname.count() != 1:
            print("Error")

    result = len(list(set(list_of_items).intersection(set(varname)))) == 1

    return result


# def select_all_tasks(conn, table):
#     """
#     :param XXX: XXX
#     :return: XXX
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM '%s'" % (table))

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)


# def select_task_by_priority(conn, priority):
#     """
#     Query tasks by priority
#     :param conn: the Connection object
#     :param priority:
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)


def search_dicts_in_dict(a_dictionary, skey=[], maintablename="activities"):
    """Dig in a dictionary to search and find all dictionaries

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
        if type(selected_value) is dict:
            found_key = [key]
            result.append(found_key)

            rerun = search_dicts_in_dict(selected_value, key)
            if rerun != []:
                found_key.append(rerun)

    return result


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


from dateutil.parser import parse


def isdate(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def create_sqlite_table_structure_from_dictionary(
    a_dictionary,
    dict_name,
    structure_table="__structure_table__",
    sql_commands="",
    drop=False,
    list_of_tables=[],
):
    """Dig in a dictionary to search and find all dictionaries, lists and tuples

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

    tdict = a_dictionary.keys()
    kdict = list(tdict)
    data_type_in_base_dictionary = {}

    ## create base structure and relations based on dictionaries
    find_dict = a_dictionary.copy()
    for key in kdict:

        if type(a_dictionary[key]) is not dict:
            del find_dict[key]
        else:
            sql_commands += create_sqlite_table_structure_from_dictionary(
                a_dictionary[key], key, sql_commands, drop=drop
            )
    find_dict = list(find_dict.keys())
    sql_commands += create_table_command_sqlite_from_list_keys(
        dict_name, find_dict, drop=drop
    )
    list_of_tables = []
    ## add other elements in structure
    for keyi in range(len(kdict)):

        data_type_in_base_dictionary[kdict[keyi]] = a_dictionary[
            kdict[keyi]
        ].__class__.__name__

        data = a_dictionary[kdict[keyi]]

        if type(data) is str:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="TXT"
            )
        elif type(data) is int:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="INTEGER"
            )
        elif type(data) is float:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="REAL"
            )
        elif type(data) is list:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="TXT", info="list"
            )  # no array in sqlite !!!
        elif type(data) is tuple:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="TXT", info="tuple"
            )  # no array in sqlite !!!

        elif type(data) is NoneType:
            sql_commands += add_column_command_sqlite(
                dict_name, kdict[keyi], column_type="TXT", info="!! None Type in Python"
            )
            logger.warning("TYPE UNKNOWN: " + str(data_type_in_base_dictionary))
        elif type(data) is dict:
            logger.info(
                "DICT DATA handeled elsewhere before"
                + str(data)
                + " "
                + str(type(data))
            )
        else:
            logger.error("UNEXPECTED DATA" + str(data) + " " + str(type(data)))

    ## fill structure
    print(
        "data_type_in_base_dictionary : ",
        dict_name,
        " : ",
        data_type_in_base_dictionary,
    )
    return sql_commands
