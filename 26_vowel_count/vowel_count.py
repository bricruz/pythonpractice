def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.
        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowelsstring = 'aeiouAEIOU' 
    thevowels = []
    lowervowels = []
    for letter in list(phrase):
        if letter in vowels:
            thevowels.append(letter)
    thedic = {}
    for vowel in thevowels:
        
        lowervowels.append(vowel.lower())
    for vowel in lowervowels:
        thedic[vowel] = lowervowels.count(vowel)
    
    
    
    return thedic

print(vowel_count('OllieOxenfree'))

        
