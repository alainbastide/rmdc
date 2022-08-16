<!-- <style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style> -->


# Really Minimalist Dictionary Converter to SqLite

[![Github All Releases](https://img.shields.io/github/downloads/alainbastide/rmdc/total.svg)]() Release will come soon

This repository is a proof of concept for identifying lists, tuples and dictionaries in a given python dictionary. Python functions follow python dictionaries (dict) to dig.

The code can be improved or integrated into other code to perform more complex operations based on python-specific type detection.

The second part of the code consists in the production of SQL codes to produce an elementary SQL structure and include data in this structure.

## First step : Really Minimalist Dictionary Converter
Identify the data structure of the given dictionary.


```python
import logging

import searchers as rmdc
import sqlformatter as sqlf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class test_class:
    def __init__(self):
        pass


## set a simple dict
test_dict = {
    "TF": ["H", "V"],
    "TX": ["1", "2"],
    "A": 1,
    "B": {
        "a": {
            "W": {"Q": 1, "BP": ["CX", "TX"]},
            "X": ("T1", 8, 7.4),
            "RP": ["OX", "PX"],
        },
        "RZ": ["BX", "AX"],
    },
    "SST": "Mikado",
    "WX": {"TT": 1},
    "ZZ": 5.6,
    "C": {"G": 20, "R": ["O", "P"]},
    "U": 8.4,
    "ZS": test_class(),
    "FD": None,
}

test_list_dict = [test_dict.copy()]
for i in range(1, 10):
    test_list_dict.append(test_dict.copy())

for i in range(len(test_list_dict)):
    rmdc.generate_random_values(test_list_dict[i])
    logger.info(test_list_dict[i])

logger.info({"test_dict": test_dict})

## search and find dictionaries
logger.info(rmdc.search_dicts_in_dict(test_dict))

## search and find dictionaries, lists and tuples
(
    some_dictionaries,
    some_lists,
    some_tuples,
) = rmdc.search_dictionaries_lists_tuples_in_dict(test_dict)

## print all
logger.info({"some_dictionaries": some_dictionaries})

logger.info({"some_lists": some_lists})

logger.info({"some_tuples": some_tuples})

sql_commands = sqlf.create_sqlite_table_structure_from_dictionary(
    test_dict, dict_name="test_dict", drop=True
)

logger.info(sql_commands)

```

Results in a terminal

```bash
$ test.py
INFO:__main__:{'TF': ['l', 'F'], 'TX': ['H', 'P'], 'A': -4, 'B': ['kZ', 'WW'], 'SST': 'wOK', 'WX': 5, 'ZZ': -5, 'C': ['j', 'l'], 'U': 4, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['V', 'P'], 'TX': ['j', 'C'], 'A': -9, 'B': ['RW', 'ho'], 'SST': 'dxkY', 'WX': -8, 'ZZ': -3, 'C': ['N', 'z'], 'U': 6, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['N', 'R'], 'TX': ['Z', 'r'], 'A': -1, 'B': ['oT', 'YH'], 'SST': 'o', 'WX': 8, 'ZZ': -8, 'C': ['V', 'm'], 'U': -6, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['R', 'd'], 'TX': ['c', 'Y'], 'A': 5, 'B': ['uJ', 'yH'], 'SST': 'pWiMAAFLD', 'WX': -9, 'ZZ': -3, 'C': ['A', 'd'], 'U': -4, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['Q', 'o'], 'TX': ['k', 'F'], 'A': -4, 'B': ['DF', 'Sg'], 'SST': 't', 'WX': 6, 'ZZ': 1, 'C': ['Z', 'J'], 'U': 10, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['S', 'H'], 'TX': ['e', 'x'], 'A': -10, 'B': ['ro', 'Vh'], 'SST': 'o', 'WX': 6, 'ZZ': -9, 'C': ['M', 'v'], 'U': 0, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['W', 'o'], 'TX': ['U', 'j'], 'A': -10, 'B': ['Uz', 'FG'], 'SST': 'J', 'WX': -7, 'ZZ': 2, 'C': ['d', 'X'], 'U': -3, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['p', 'M'], 'TX': ['p', 'Y'], 'A': 4, 'B': ['yf', 'SH'], 'SST': 'z', 'WX': -1, 'ZZ': 9, 'C': ['K', 'E'], 'U': -5, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['I', 'K'], 'TX': ['o', 'f'], 'A': -7, 'B': ['NT', 'Vv'], 'SST': 'h', 'WX': 2, 'ZZ': 8, 'C': ['w', 'F'], 'U': -6, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'TF': ['r', 'W'], 'TX': ['h', 'f'], 'A': 10, 'B': ['Te', 'Rp'], 'SST': 'R', 'WX': 6, 'ZZ': 0, 'C': ['T', 'd'], 'U': 1, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}
INFO:__main__:{'test_dict': {'TF': ['r', 'W'], 'TX': ['h', 'f'], 'A': 1, 'B': {'a': ['Hg', 'TM'], 'RZ': ['Te', 'Rp']}, 'SST': 'Mikado', 'WX': {'TT': 7}, 'ZZ': 5.6, 'C': {'G': -10, 'R': ['T', 'd']}, 'U': 8.4, 'ZS': <__main__.test_class object at 0x7ff84a3ebe80>, 'FD': None}}
INFO:__main__:[['B'], ['WX'], ['C']]
INFO:searchers:[]:A:1<class 'int'>INTEGER Found
INFO:searchers:['B']:SST:Mikado<class 'str'>STRING Found
INFO:searchers:['B', 'WX']:TT:7<class 'int'>INTEGER Found
INFO:searchers:['B', 'WX']:ZZ:5.6<class 'float'>REAL Found
INFO:searchers:['B', 'WX', 'C']:G:-10<class 'int'>INTEGER Found
INFO:searchers:['B', 'WX', 'C']:U:8.4<class 'float'>REAL Found
WARNING:searchers:['B', 'WX', 'C']:ZS:<__main__.test_class object at 0x7ff84a3ebe80><class '__main__.test_class'>Unsupported format
WARNING:searchers:['B', 'WX', 'C']:FD:None<class 'NoneType'>Unsupported format
INFO:__main__:{'some_dictionaries': [['B'], ['WX'], ['C']]}
INFO:__main__:{'some_lists': ['TF', 'TX', ['a', 'RZ'], ['R']]}
INFO:__main__:{'some_tuples': []}
data_type_in_base_dictionary :  B  :  {'a': 'list', 'RZ': 'list'}
data_type_in_base_dictionary :  WX  :  {'TT': 'int'}
data_type_in_base_dictionary :  C  :  {'G': 'int', 'R': 'list'}
INFO:sqlformatter:DICT DATA handeled elsewhere before{'a': ['Hg', 'TM'], 'RZ': ['Te', 'Rp']} <class 'dict'>
INFO:sqlformatter:DICT DATA handeled elsewhere before{'TT': 7} <class 'dict'>
INFO:sqlformatter:DICT DATA handeled elsewhere before{'G': -10, 'R': ['T', 'd']} <class 'dict'>
ERROR:sqlformatter:UNEXPECTED DATA<__main__.test_class object at 0x7ff84a3ebe80> <class '__main__.test_class'>
WARNING:sqlformatter:TYPE UNKNOWN: {'TF': 'list', 'TX': 'list', 'A': 'int', 'B': 'dict', 'SST': 'str', 'WX': 'dict', 'ZZ': 'float', 'C': 'dict', 'U': 'float', 'ZS': 'test_class', 'FD': 'NoneType'}
data_type_in_base_dictionary :  test_dict  :  {'TF': 'list', 'TX': 'list', 'A': 'int', 'B': 'dict', 'SST': 'str', 'WX': 'dict', 'ZZ': 'float', 'C': 'dict', 'U': 'float', 'ZS': 'test_class', 'FD': 'NoneType'}
INFO:__main__:
    DROP TABLE IF EXISTS 'B_table'; 

    CREATE TABLE IF NOT EXISTS 'B_table' ( 
    __id_B__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE 
        );
    ALTER TABLE 'B_table'     ADD 'a' TXT;     /*list*/
    ALTER TABLE 'B_table'     ADD 'RZ' TXT;     /*list*/

    DROP TABLE IF EXISTS 'WX_table'; 

    CREATE TABLE IF NOT EXISTS 'WX_table' ( 
    __id_WX__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE 
        );
    ALTER TABLE 'WX_table'     ADD 'TT' INTEGER;     

    DROP TABLE IF EXISTS 'C_table'; 

    CREATE TABLE IF NOT EXISTS 'C_table' ( 
    __id_C__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE 
        );
    ALTER TABLE 'C_table'     ADD 'G' INTEGER;     
    ALTER TABLE 'C_table'     ADD 'R' TXT;     /*list*/

    DROP TABLE IF EXISTS 'test_dict_table'; 

    CREATE TABLE IF NOT EXISTS 'test_dict_table' ( 
    __id_test_dict__ INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE 
            ,B INTEGER /*dict*/
        ,WX INTEGER /*dict*/
        ,C INTEGER /*dict*/
        ,FOREIGN KEY (B)  REFERENCES 'B_table' (__id_B__) 
        ,FOREIGN KEY (WX)  REFERENCES 'WX_table' (__id_WX__) 
        ,FOREIGN KEY (C)  REFERENCES 'C_table' (__id_C__) 
    );
    ALTER TABLE 'test_dict_table'     ADD 'TF' TXT;     /*list*/
    ALTER TABLE 'test_dict_table'     ADD 'TX' TXT;     /*list*/
    ALTER TABLE 'test_dict_table'     ADD 'A' INTEGER;     
    ALTER TABLE 'test_dict_table'     ADD 'SST' TXT;     
    ALTER TABLE 'test_dict_table'     ADD 'ZZ' REAL;     
    ALTER TABLE 'test_dict_table'     ADD 'U' REAL;     
    ALTER TABLE 'test_dict_table'     ADD 'FD' TXT;     /*!! None Type in Python*/


```
## Second step : produce SQL commands
Basic SQL generator to create SQL data structure and data inclusion.

### Next ...
 Automatic SQL commands 

https://docs.travis-ci.com/user/languages/python/
