def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.
    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names
    Returns list of space-separated first and last names.
        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]
        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    fullnames = []
    for name in people:
        firstName = name['first']
        lastName = name['last']
        namestring = firstName + " " + lastName
        fullnames.append(namestring)
    return fullnames

names = [{'first': 'Bob', 'last': 'Barker'},{'first': 'Grace', 'last': 'Hopper'},]
print(extract_full_names(names))
