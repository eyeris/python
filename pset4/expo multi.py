def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    num=1
    while exp>0:
        num*=base
        exp-=1
    return num