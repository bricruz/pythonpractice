def repeat(phrase, num):
    """Return phrase, repeated num times.
        >>> repeat('*', 3)
        '***'
        >>> repeat('abc', 2)
        'abcabc'
        >>> repeat('abc', 0)
        ''
    Ignore illegal values of num and return None:
        >>> repeat('abc', -1) is None
        True
        >>> repeat('abc', 'nope') is None
        True
    """
    thing = phrase
    if type(num) is int and num > 0:
        for i in range(num-1):
            thing += phrase
    else:
        return None
    return thing
print(repeat('*',1))