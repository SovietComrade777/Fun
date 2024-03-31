#Just Wrote this code in python as my first project
import random
l1=['serious','angry','happy','sad','revengefull']
a=random.randint(0,len(l1)-1)
print("I am Currently:",l1[a])
#huk em up
l=['yes','no','IDK']    
while True:
    B=random.randint(0,len(l)-1)
    S= input("Enter Your Query :})")
    if S=="exit" or S=="leave" or S=="stop":
        break
    elif S=='Jai Shree Ram':
        print("Jai "+S)
    elif S=="How are you":
        print("I am Currently : ",l1[a])
    else:
        print(l[B])
    
"""i wrote this code.Listen Never Quit Your Journey "mf" damn stay focused and never change your path a path should not be left if taken once otherwise i promise you can't do anything(in future).
    You will just change paths otherwise focus on one side. your friends ,relatives ,those who know you by any chance should always try to remmember the time spent with you and will tell you ,how they know you.
    \Jai Shree Ram|Jai Baba Ki/
    --------------------------
    /Remmember of |Mike Tyson \
""" 
