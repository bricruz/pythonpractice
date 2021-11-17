def list_check(lst):
    """Are all items in lst a list?
        >>> list_check([[1], [2, 3]])
        True
        >>> list_check([[1], "nope"])
        False
    """
    count = 0
    for thing in lst:
        if not isinstance(thing,list):
            count += 1
        else:
            count += 0
    if count > 0:
        return False
    else:
        return True

print(list_check([[1], 'spam', [2,'tot']]))
