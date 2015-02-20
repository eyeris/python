"""
Bisection search example for number game.
"""


print "Please think of a number between 0 and 100!"
low = 0
high = 100
ans = (high + low)/2
rang=["h","l","c"]
while True:
    print "Is your secret number"+str(ans)+"?"
    inp=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inp not in rang:
        print "Sorry, I did not understand your input."
        continue
    elif inp=="h":
        high=ans
    elif inp=="l":
        low=ans
    elif inp=="c":
        print "Game over. Your secret number was: "+str(ans)
        break
    ans = (high + low)/2

