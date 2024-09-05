n=77
print('welcome to the game gusseing the number')
count=9
guess=1
for i in range(0,9):
    count=count-1
    
    num=(int(input("enter the num")))
    if num>n:
        print("decrese your number")
    elif num<n:
        print("increase your num")
    elif num==n:
        print("your guess is right in a" ,guess, "attempts")
        break
    else:
        print("you loose the game")
    guess=guess+1
    print("your left with",count ," guess")
    
    
