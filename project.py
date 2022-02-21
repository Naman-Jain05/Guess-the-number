import random
randNUmber=random.randint(1,100)
#print(randNUmber)
num=None
guesses=0
while(num!=randNUmber):
    num=int(input("enter your number:"))
    guesses +=1
    if(num==randNUmber):
        print(f"wohoooo guesses={guesses}")
    elif(num>randNUmber):
        print(f"entered number is high try a lower number")
    elif(num<randNUmber):
        print(f"entered number is low try a higher number")


with open("hiscore.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("you broke the high score")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
else:
    print("better try next time")


