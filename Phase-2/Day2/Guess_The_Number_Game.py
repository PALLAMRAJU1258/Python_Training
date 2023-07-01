import random as r
print("Guess the Number Game")
min_val=int(input("Enter the min value:"))
max_val=int(input("Enter the max value:"))
ans = r.randint(min_val,max_val)
while 1 :
    guess = int(input("Enter Your Guess:"))
    if ans  < guess :
        if guess - ans <= 10 :
            print("Number is High")
        else:
            print("Number is Too High")
    elif ans > guess:
        if ans - guess <= 10 :
            print("Number is Low")
        else:
            print("Number is Too Low")
    else:
        print("The Guess is correct")
        break
