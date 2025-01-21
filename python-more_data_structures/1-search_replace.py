#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for ming in my_list:
        if ming == search:
            new_list.append(replace)
        else:
            new_list.append(ming)
    return new_list
