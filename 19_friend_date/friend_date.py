def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    lista = []
    listb = []
    for item in a:
        if item in b:
            return True
        elif type(item) == list:
            for thing in item:
                lista.append(thing)
    
    for item in b:
        if type(item) == list:
            for thing in item:
                listb.append(thing)
    for item in lista:
        if item in listb:
            return True

    return False

print(friend_date(('Elmo',10,[1,2,3]),(7,'Dog',[4,5])))


