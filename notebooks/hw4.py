def is_reverse(string1, string2):
    """compare two words (strings) and return True if one of the words is the reverse of the other
    
    Parameters
    ----------
    string1 : str
              A string containing one word
    string2 : str
              A string containing one word          
        
    Return
    ------
            : bool
              True if string1 is the reverse of string2; Otherwise, False
    
    """
    length1 = len(string1)
    length2 = len(string2)
    if length1 != length2:
        return False
    
    for i in range(length1):
        if string1[i] != string2[-1-i]:
            return False
    return True