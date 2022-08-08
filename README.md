<!-- <style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style> -->


# Really Minimalist Dictionary Converter to SqLite

[![Github All Releases](https://img.shields.io/github/downloads/alainbastide/rmdc/total.svg)]()

This repository is a proof of concept for identifying lists, tuples and dictionaries in a given python dictionary. Python functions follow python dictionaries (dict) to dig.

The code can be improved or integrated into other code to perform more complex operations based on python-specific type detection.

```python
#!/usr/bin/env python3

import logging

import searchers as rmdc


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

## set a simple dict
test_dict= {'TF':['H','V'],'TX':['1','2'],'A':1,'B': {'a' : {'W': {'Q':1,'BP':['CX','TX']}, \
      'X':('T1',8,7.4),'RP':['OX','PX']},'RZ':['BX','AX']}, \
      'WX': {'TT':1}, 'C':{'G':20,'R':['O','P']}}

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
INFO:__main__:{'TF': ['H', 'V'], 'TX': ['1', '2'], 'A': 1, \
       'B': {'a': {'W': {'Q': 1, 'BP': ['CX', 'TX']}, 'X': ('T1', 8, 7.4), \
       'RP': ['OX', 'PX']}, 'RZ': ['BX', 'AX']}, 'WX': {'TT': 1}, \
        'C': {'G': 20, 'R': ['O', 'P']}}
INFO:__main__:[['B', [['a', [['W']]]]], ['WX'], ['C']]
INFO:__main__:[['B', [['a', [['W']]]]], ['WX'], ['C']]
INFO:__main__:['TF', 'TX', [[['BP'], 'RP'], 'RZ'], ['R']]
INFO:__main__:[[['X']]]

```

# TODO
## Next ...
 Automatic SQL commands 

https://docs.travis-ci.com/user/languages/python/
