def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_list = []
    phrase_list = list(phrase)
    for letter in phrase_list:
        if letter.islower() and letter == to_swap.lower():
            flipped_list.append(letter.upper()) 
        elif letter.isupper() and letter == to_swap.upper():
            flipped_list.append(letter.lower())
        else:
            flipped_list.append(letter)

    flipped = "".join(flipped_list)

    return flipped

    # for i in range(len(phrase_list)):
    #     if phrase_list[i] == to_swap:
    #         phrase_list[i].upper()
    #     print(phrase_list[i])
    
        

print(flip_case('Aaaah','a'))
            
