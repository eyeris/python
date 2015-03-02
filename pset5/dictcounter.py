def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largest=""
    if len(aDict)==0:
        return None
    elif len(aDict)==1:
        return aDict.keys()[0]
    msize=0
    for i in aDict:
        count=0
        for j in aDict[i]:
            count+=1
        if msize<count:
            msize=count
            largest=i
    return largest

