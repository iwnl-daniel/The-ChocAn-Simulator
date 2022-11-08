#This holds any helper functions that may be useful
#accross multiple files

#This function takes a string and length bounds, and returns 0 if the
#string is within the bounds, 1 if is outside the maximum bound,
#and -1 if it is below the minimum bound.
def stringLengthError(string : str, minLength : int, maxLength : int) -> int:
    stringLength = len(string)
    if(stringLength < minLength):
        return -1
    if(stringLength > maxLength):
        return 1
    return 0