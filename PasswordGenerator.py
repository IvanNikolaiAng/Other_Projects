import random

Weak = ["abroad", "centre", "credit", "assume", "almost", "credit", "crisis", "custom", 
"damage", "danger", "mirror", "mobile", "modern", "modest", "module", "moment", "taught", "tenant", 
"tender", "tennis", "thanks", "A", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

Medium = [1,2,3,4,5,6,7,8,9,0,"!","?","/",",","."]


while True:
    sec = input("Password Generator\nChoose a security level:\nWeak\tMedium\tStrong\tExit\n")

    Weakpass = []
    Medpass = []
    Strongpass = []

    if sec == "Weak":
        Weakpass = random.sample(Weak, 2)
        Weakpass = Weakpass[0] + Weakpass[1]
        print(Weakpass,"\n")
    if sec == "Medium":
        Weakpass = random.sample(Weak, 2) 
        Medpass = random.sample(Medium, 6)
        Medpass = Weakpass + Medpass
        random.shuffle(Medpass)
        Medpass = ''.join(str(i) for i in Medpass)
        print(Medpass,"\n")
    if sec == "Strong":
        Weakpass = random.sample(Weak, 3) 
        Medpass = random.sample(Medium, 6)
        for i in range(len(Weakpass)):
            for c in Weakpass[i]:
                cap = bool(random.getrandbits(1))
                if cap == 1:
                    Strongpass.append(c.upper())
                else:  
                    Strongpass.append(c)
        Strongpass = Strongpass + Medpass
        random.shuffle(Strongpass)
        Strongpass = ''.join(str(i) for i in Strongpass)
        print(Strongpass,"\n")
    if sec == "Exit":
        break
