import random

def bat(us,cs,select):
    s=select
    user_score=us
    computer_score=cs
    res=0
    bat=True
    while (bat==True):
        user_bat=int(input("Enter the number 1 to 6:"))
       
        if(user_bat<=6):
            com_bowl=random.randint(1,6)
            print("Computer enters:",com_bowl)
            if(user_bat==com_bowl):
                print("OUT")
                bat=False
            else:
                res+=user_bat
                print("score:",res)
                user_score+=user_bat    
            if(s!=1 and user_score>computer_score):
                break    
        else:        
            print("Number 1 to 6 only allowed")   
    return user_score  

def bowl(cs,us,select):
    s=select
    user_score=us
    computer_score=cs
    bowl=True
    res=0
    while (bowl==True):
        user_bowl=int(input("Enter the number 1 to 6:"))
        if(user_bowl<=6):
            com_bat=random.randint(1,6)
            print("Computer enters",com_bat)
            if(com_bat==user_bowl):
                print("OUT")
                bowl=False
            else:
                res+=com_bat
                print("Score",res)
                computer_score+=com_bat    
            if(s!=2 and computer_score>user_score):
                break
            
        else:
            print("Number 1 to 6 only allowed")   
    return computer_score

def last(cs,us):
    
    user_score=us
    computer_score=cs
    bowl=True
    res=0
    
    while (bowl==True):
        user_bowl=int(input("Enter the number 1 to 6:"))
        if(user_bowl<=6):
            com_bat=random.randint(1,6)
            print("Computer enters",com_bat)
            if(com_bat==user_bowl):
                print("OUT")
                bowl=False
            else:
                res+=com_bat
                print("Score",res)
                computer_score+=com_bat    
            if(computer_score>user_score):
                break
            
        else:
            print("Number 1 to 6 only allowed")   
    return computer_score             
               
  
b=random.randint(1,6)



print("LETS SPIN THE TOSS")
print("YOUR CALL \n 1.ODD \t 2.EVEN\n")
toss=int(input("Enter option of the call:"))
a=int(input("Enter the number 1 to 6:"))
print("computer enter:",b)
player=0
computer=0
u_score=0
c_score=0
t=0



if((a+b)%2==1 and toss==1):
    print("YOU WON THE TOSS\n")
    player=1
    print("1.BAT \t 2.BOWL")   
if(player==1):
    select=int(input("You Decide to:"))
    if(select==1):
        print("You decided to bat first")
        print("-----1 innings-----")
        u_score=bat(u_score,c_score,select)
        print("Your Score:",u_score)
        print("******")
        print("Target:",u_score+1)
        print("******")
        print("-----2 innings-----")
        c_score=bowl(c_score,u_score,select)
    else:
        print("You decided to bowl first")
        print("-----1 innings-----")
        c_score=bowl(c_score,u_score,select)
        print("Computer Score:",c_score)
        print("******")
        print("Target:",c_score+1)
        print("******")
        print("-----2 innings-----")
        u_score=bat(u_score,c_score,select)
else:
    computer=1
    select=1
    
    print("Computer decided to bowl first")
    print("-----1 innings-----")
    u_score=bat(u_score,c_score,select)
    print("Your Score:",u_score)
    print("******")
    print("Target:",u_score+1)
    print("******")
    print("-----2 innings-----")
    c_score=last(c_score,u_score)
    


if(u_score==c_score):
    print("TIE")
elif(u_score>c_score):  
    print("🏆YOU WIN🏆")  
else:
    print("🤡COMPUTER WIN🤡")    


