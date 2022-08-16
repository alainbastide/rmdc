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
