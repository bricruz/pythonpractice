def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?
    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary
    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.
        >>> includes([1, 2, 3], 1)
        True
        >>> includes([1, 2, 3], 1, 2)
        False
        >>> includes("hello", "o")
        True
        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True
        >>> includes({1, 2, 3}, 1)
        True
        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True
        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    collection_list = list(collection) if type(collection) is not dict else []

    
    if type(collection) is dict:
        collect_keys = list(collection.keys())
        collect_vals = list(collection.values())
        collection_list = collect_keys + collect_vals
    
    if type(collection) is set:
        start = None

    if len(collection_list) > 0:
        for i in range(len(collection_list)):
            if start != None and i < start:
                continue
            else:
                if collection_list[i] == sought:
                    there = True
                    if there == True:
                        break
                else:
                    there = False
    if there == True:
        return True
    else:
        return False
        

print(includes(('Elmo', 5, 'red'), 'red', 1))