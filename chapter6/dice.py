import random
keep_going =True
# while keep_going:         
dice = [0, 0, 0, 0, 0,0, 0,]
for  i in range(6):
    dice[i]= random.randint(1,6)
print(dice)
dice.sort()
print(dice)

if dice[0] == dice[0]:
    print("ЯЦЗЫ!")
else:
    print("OTHER")