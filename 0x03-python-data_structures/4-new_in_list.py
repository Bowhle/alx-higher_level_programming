def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    if idx >= len(new_list) -1:
        return new_list
    new_list.insert(idx, element)
    return new_list