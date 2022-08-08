def search_dicts_in_dict(a_dictionary):
    """ Dig in a dictionary to search and find all dictionaries
    
    Parameters
    ----------
    a_dictionary : a dictionary

    Returns
    ----------
    result : a list build like a tree in which we find  ditionaries

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
        selected_key = a_dictionary[key]
        if type(selected_key) is dict :
            found_key = [key]
            result.append(found_key)
            
            rerun = search_dicts_in_dict(selected_key)
            if rerun != [] : found_key.append(rerun)
    
    return result  

def search_dictionaries_lists_tuples_in_dict(a_dictionary):
    """ Dig in a dictionary to search and find all dictionaries, lists and tuples
    
    Parameters
    ----------
    a_dictionary : a dictionary

    Returns
    ----------
    result_dict : a list build like a tree in which we find  ditionaries
    result_list : a list build like a tree in which we find  ditionaries
    result_tuple : a list build like a tree in which we find  ditionaries

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
    INFO:__main__:[['C']]
    INFO:__main__:[['R']]
    INFO:__main__:[]   
    """
    result_dict = []
    result_list = []
    result_tuple = []
    for key in a_dictionary.keys():
        selected_key = a_dictionary[key]
        if type(selected_key) is dict :
            found_key = [key]
            result_dict.append(found_key)

            rerun,lists,tuples = search_dictionaries_lists_tuples_in_dict(selected_key)
            
            if rerun != [] : 
                found_key.append(rerun)  
                
            if lists!=[]:
                result_list.append(lists)
                
            if tuples!=[]:
                result_tuple.append(tuples)
                
        if type(selected_key) is list: 
            result_list.append(key)
        if type(selected_key) is tuple: 
            result_tuple.append(key)
        
    return result_dict,result_list,result_tuple
