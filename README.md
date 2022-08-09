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
#!/usr/bin/env python3

import logging

import searchers as rmdc


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class test_class:
    def __init__(self):
        pass

## set a simple dict
test_dict= {'TF':['H','V'],'TX':['1','2'],'A':1,'B': {'a' : {'W': {'Q':1,'BP':['CX','TX']}, \
    'X':('T1',8,7.4),'RP':['OX','PX']},'RZ':['BX','AX']},'SST': 'Mikado', \
    'WX': {'TT':1}, 'ZZ':5.6, 'C':{'G':20,'R':['O','P']},'U':8.4, 'ZS': test_class()}

logger.info(test_dict)

## search and find dictionaries 
logger.info(rmdc.search_dicts_in_dict(test_dict))

## search and find dictionaries, lists and tuples
some_dictionaries, some_lists, some_tuples = \
    rmdc.search_dictionaries_lists_tuples_in_dict(test_dict)

## print all
logger.info(some_dictionaries)

logger.info(some_lists)

logger.info(some_tuples)
```

Results in a terminal

```bash
$ python3 test_mdc.py
INFO:__main__:{'test_dict': {'TF': ['H', 'V'], 'TX': ['1', '2'], 'A': 1, 
        'B': {'a': {'W': {'Q': 1, 'BP': ['CX', 'TX']}, 'X': ('T1', 8, 7.4), 
        'RP': ['OX', 'PX']}, 'RZ': ['BX', 'AX']}, 'SST': 'Mikado', 
        'WX': {'TT': 1}, 'ZZ': 5.6, 'C': {'G': 20, 'R': ['O', 'P']}, 
        'U': 8.4, 'ZS': <__main__.test_class object at 0x7f340bc77fd0>}}
INFO:__main__:[['B', [['a', [['W']]]]], ['WX'], ['C']]
INFO:searchers:[]:A:1<class 'int'>INTEGER Found
INFO:searchers:['B', 'a', 'W']:Q:1<class 'int'>INTEGER Found
INFO:searchers:['B', 'a', 'W']:SST:Mikado<class 'str'>STRING Found
INFO:searchers:['B', 'a', 'W', 'WX']:TT:1<class 'int'>INTEGER Found
INFO:searchers:['B', 'a', 'W', 'WX']:ZZ:5.6<class 'float'>REAL Found
INFO:searchers:['B', 'a', 'W', 'WX', 'C']:G:20<class 'int'>INTEGER Found
INFO:searchers:['B', 'a', 'W', 'WX', 'C']:U:8.4<class 'float'>REAL Found
WARNING:searchers:['B', 'a', 'W', 'WX', 'C']:ZS:<__main__.test_class 
        object at 0x7f340bc77fd0><class '__main__.test_class'>Unsupported format
INFO:__main__:{'some_dictionaries': [['B', [['a', [['W']]]]], ['WX'], ['C']]}
INFO:__main__:{'some_lists': ['TF', 'TX', [[['BP'], 'RP'], 'RZ'], ['R']]}
INFO:__main__:{'some_tuples': [[['X']]]}


```
## Second step : produce SQL commands
Basic SQL generator to create SQL data structure and data inclusion.

### Next ...
 Automatic SQL commands 

https://docs.travis-ci.com/user/languages/python/
