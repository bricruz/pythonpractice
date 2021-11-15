def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict = {}
    phraseCopy = phrase
    for letter in phrase:
        count = 0
        dict[letter] = count
        for char in phraseCopy:
            if letter == char:
                count += 1
                dict[letter] = count
    
    return dict

print(multiple_letter_count('AAaabBbCcCdDDD'))