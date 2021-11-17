def titleize(phrase):
    """Return phrase in title case (each word capitalized).
        >>> titleize('this is awesome')
        'This Is Awesome'
        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    listphrase = phrase.split(" ")
    title = []
    for word in listphrase:
        
        title.append(word.capitalize())
        
    print(" ".join(title))

titleize('Waddup WIT it')
