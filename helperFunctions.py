#This holds any helper functions that may be useful
#accross multiple files

#This function informs the user entering in a string if it is too
#long or too short.
def stringErrorPrompt(string : str, minLength : int, maxLength : int) -> bool:
    stringLength = len(string)
    if(stringLength < minLength):
        print("Error: Data entered below minimum acceptable length.")
        return False
    if(stringLength > maxLength):
        print("Error: Data entered above maximum acceptable length.")
        return False
    return True