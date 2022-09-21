from operator import index
import random

ans = random.randint(0000, 9999)
print("Welcome to the Cows and Bulls Game:")
ans_list = [int(x) for x in str(ans)]
while len(ans_list) < 4:
    ans_list.insert(0 , int(0)) 
print(ans_list)
guess = 0

def checker(input, ans):
    input_list = [int(x) for x in input]
    print("You have inputted:", input_list)
    length = 4
    cow = []
    bull = []
    for i in range(length):
        if ans_list[i] == input_list[i]:
            cow.append(i)
    for i in range(length):
        if input_list[i] in ans_list and ans_list[i] != input_list[i]:
            bull.append(i)
    cow = len(cow)
    # print(cow)
    bull = len(bull)
    # print(bull)
    return cow, bull

while True:
    x = input("Enter a 4 digit number:")
    check = checker(x, ans)
    cow = check[0]
    bull = check[1]
    print("cow: %d \t bull: %d" % (cow, bull))
    if cow < 4:
        guess+=1
    elif cow == 4:
        print("You have guessed correctly!\nYou took",guess+1,"tries!")
        break







