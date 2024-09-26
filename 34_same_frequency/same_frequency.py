def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    
    num1_digits = {}
    num2_digits = {}

    for char in str(num1):
        if char not in num1_digits.keys():
            num1_digits[char] = str(num1).count(char)

    for char in str(num2):
        if char not in num2_digits.keys():
            num2_digits[char] = str(num2).count(char)

    if num1_digits == num2_digits:
        return True
    return False

             