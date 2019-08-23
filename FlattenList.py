def flatten_list(list_of_lists):  #flattens a list of lists into single array
    flat_list = []
    for sublist in list_of_lists:
        if type(sublist) is list: #make sure the item in list_of_lists is a list (iterable)
            for item in sublist:
                flat_list.append(item)
    flat_list = list(dict.fromkeys(flat_list))
    return flat_list
