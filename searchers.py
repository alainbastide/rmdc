import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def search_dicts_in_dict(a_dictionary,skey=[]):
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

def search_dictionaries_lists_tuples_in_dict(a_dictionary,skey=[]):
    """ Dig in a dictionary to search and find all dictionaries, lists and tuples
    
    Parameters
    ----------
    a_dictionary : a dictionary

    Returns
    ----------
    result_dict : a list built like a tree in which we find  ditionaries
    result_list : a list built like a tree in which we find  ditionaries
    result_tuple : a list built like a tree in which we find  ditionaries

    Example : 
    ----------
    test_dict= {'C':{'G':20,'R':['O','P']}}

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

    Results : 
    ----------
    INFO:__main__:{'C': {'G': 20, 'R': ['O', 'P']}}
    INFO:__main__:[['C']]
    INFO:searchers:['C']:20<class 'int'>INTEGER Found
    INFO:__main__:[['C']]
    INFO:__main__:[['R']]
    INFO:__main__:[]  
    """
    result_dict = []
    result_list = []
    result_tuple = []

    for key in a_dictionary.keys():
        selected_value = a_dictionary[key]
        if type(selected_value) is dict :
            found_key = [key]
            result_dict.append(found_key)

            # digger
            # recursion is not infinite
            skey.append(key)
            rerun,lists,tuples = \
                search_dictionaries_lists_tuples_in_dict(selected_value,skey)
            
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
            logger.info(str(skey) + str(':') + str(selected_value) + str(type(selected_value)) + \
                'INTEGER Found')
        elif type(selected_value) is str:
            logger.info(str(skey) + str(':') + str(selected_value) + str(type(selected_value))+ \
                'STRING Found')
        elif type(selected_value) is float:
            logger.info(str(skey) + str(':') + str(selected_value) + str(type(selected_value)) + \
                'REAL Found')
        else :
            logger.warning(str(skey) + str(':') + str(selected_value) + str(type(selected_value)) + \
                'Unsupported format')
        
    return result_dict,result_list,result_tuple
