def longest_sub(s):
    """
    Returns the longest alphabetical order substring in a given string
`   """
    acc=s[0]
    subs=""
    for i in range(len(s)-1):
        if s[i]<=s[i+1]:
            acc=acc+s[i+1]
        else:
            if(len(subs)<len(acc)):
                subs=acc
                acc=s[i+1]
            else:
                acc=""
                acc=s[i+1]
    if len(subs)<len(acc):
        subs=acc
    return subs
