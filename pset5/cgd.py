def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gsd=1
    mm=min(a,b)
    while(mm>1):
        if a%mm==0 and b%mm==0:
            return mm
        mm-=1
    return gsd
