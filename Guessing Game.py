import random

ans = random.randint(1,9)
print(ans)
i = 0
y = int(input("Guess a number between 1 and 9:"))
while (y!="exit"):
    if y > 9 or y < 1:
        print("Please input a valid answer!")
    elif y == ans:
        print("Exactly")
    elif y>ans:
        print("Too high")
    elif y<ans:
        print("Too low")
    elif y == "exit":
        break
    i+=1
print("You had %d tries!", i)