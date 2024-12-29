#Rock Paper Scissor Game
import random
'''
1=rock
2=paper
3=scissor
'''
n='Y'
while (n!='N' and n!='n'):
    you={1:"Rock",2:"Paper",3:"Scissor"}
    your={"R":1,"P":2,"S":3}
    com=random.choice([1,2,3])
    mine=input("R : Rock | P : Paper | S : Scissor \nEnter your choice : ")
    x=your[mine]
    print(f"Your Input : {you[x]}\n Computer Input : {you[com]}")

    if(com==x):
        print("Match Draw ")
    else:
        if(com==1 and x==2):
            print("You Win ")
        elif(com==1 and x==3):
            print("You Lose")
        elif(com==2 and x==1):
            print("You Lose ")
        elif(com ==2 and x==3):
            print("You Win ")
        elif(com==3 and x==1):
            print("You Win ")
        elif(com==3 and x==2):
            print("You Lose ")
        else:
            print("Wrong Input :0")
    n=input("Do you want to play more(Y/N)\n")
print("Thanks for Playing \nHope you like it :)")

