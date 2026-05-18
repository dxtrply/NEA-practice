def isValidLength(value, minLength, MaxLength = 255):
    if len(value) < minLength:
        return False

    if len(value) > MaxLength:
        return False
    
    return True