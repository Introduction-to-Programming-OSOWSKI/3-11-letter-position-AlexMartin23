def letterPos(strWord, strLetter):
    srtTest = "" #initialize test variable 
    intreturn = 0
    for i in range (0, len(strWord)-1):
        strTest = strWord[i]
        if strTest == strLetter:
            return i + 1
    return 0


print(letterPos("alex", "q"))  
        
    