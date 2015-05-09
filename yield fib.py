def genfib():
    fibn_1=1#(n-1)
    fibn_2=0#(n-2)
    while True:
        next=fibn_1+fibn_2
        yield next
        fibn_2=fibn_1
        fibn_1=next
