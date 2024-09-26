def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    if parens[0] == ')' or parens[-1] == '(':
            return False
    
    checked = []

    for char in parens:
        if char == '(':
            checked.append(char)
        elif char == ')':
             if not checked:
                  return False
             checked.pop()
    
    # if len(checked) = 0, True
    # if len(checked) != 0, False
    return len(checked) == 0
                  


    