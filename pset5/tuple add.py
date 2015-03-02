def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    test=()
    for i in range(0,len(aTup),2):
        test+=(aTup[i],)
    return test