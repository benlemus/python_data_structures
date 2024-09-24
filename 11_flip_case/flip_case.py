def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_phrase = []

    for char in phrase:
        if char.lower() == to_swap.lower():
            if char == to_swap.lower():
                new_phrase.append(char.upper())

            if char == to_swap.upper():
                new_phrase.append(char.lower())
        else:
           new_phrase.append(char)
    
    return ''.join(new_phrase)

'''    
    # Determine the lower and upper case versions of the character to swap
    to_swap = to_swap.lower()
    
    # Create a new string where the case is flipped for the desired character
    return ''.join(
        [char.swapcase() if char.lower() == to_swap else char for char in phrase]
    )
'''

    
