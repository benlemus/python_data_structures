def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.split(' ')

    for item in lst:
        lst[lst.index(item)] = item.capitalize()

    return ' '.join(lst)