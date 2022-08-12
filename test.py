import logging

import searchers as rmdc
import sqlformatter as sqlf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class test_class:
    def __init__(self):
        pass

## set a simple dict
test_dict= {'TF':['H','V'],'TX':['1','2'],'A':1,'B': {'a' : {'W': {'Q':1,'BP':['CX','TX']}, \
    'X':('T1',8,7.4),'RP':['OX','PX']},'RZ':['BX','AX']},'SST': 'Mikado', \
    'WX': {'TT':1}, 'ZZ':5.6, 'C':{'G':20,'R':['O','P']},'U':8.4, 'ZS': test_class()}
# test_dict= {'C':{'G':20,'R':['O','P']}}

logger.info({'test_dict':test_dict})

## search and find dictionaries 
logger.info(rmdc.search_dicts_in_dict(test_dict))

## search and find dictionaries, lists and tuples
some_dictionaries, some_lists, some_tuples = \
    rmdc.search_dictionaries_lists_tuples_in_dict(test_dict)

## print all
logger.info({'some_dictionaries':some_dictionaries})

logger.info({'some_lists':some_lists})

logger.info({'some_tuples':some_tuples})

some_dictionaries, some_lists, some_tuples = \
    sqlf.search_dictionaries_lists_tuples_in_dict_sql(test_dict)

## print all
logger.info({'some_dictionaries':some_dictionaries})

logger.info({'some_lists':some_lists})

logger.info({'some_tuples':some_tuples})


