def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    if False not in [True if type(item) == list else False for item in lst]:
        return True

    else:
        return False
