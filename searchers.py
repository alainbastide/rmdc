


def search_dicts_in_dict(a_dictionary):
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
