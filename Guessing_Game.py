import random

ans = random.randint(1,9)
i = 0

while True:
    y1 = input("Guess a number between 1 and 9:")
    if y1 == "exit":
        break
    y = int(y1) 
    if y > 9 or y < 1:
        print("Please input a valid answer!")
        i+=1
    elif y == ans:
        print("Exactly!\nYou guessed correctly in", i+1 ,"tries")
    elif y>ans:
        print("Too high")
        i+=1
    elif y<ans:
        print("Too low")
        i+=1
    
