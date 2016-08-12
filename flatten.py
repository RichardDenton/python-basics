def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flatList = []
    for item in aList:
        if type(item) == list:
            flatList += flatten(item)
        else:
            flatList.append(item)
    return flatList