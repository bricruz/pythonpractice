def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    onlyTrue = []
    for thing in lst:
        booly = bool(thing)
        if booly == True:
            onlyTrue.append(thing)

    return onlyTrue
    

print(compact([0,1,2,'',[],False,(),None,'All done']))
