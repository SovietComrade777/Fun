import random
l1=['serious','angry','happy','sad','revengefull']
a=random.randint(0,len(l1)-1)
print("I am Currently:",l1[a])
#fuck em up
l=['yes','no','IDK']
while True:
    B=random.randint(0,len(l)-1)
    S= input("Enter Your Query :})")
    if S=="exit" or S=="leave" or S=="stop":
        break
    elif S=='Jai Shree Ram':
        print("Jai"+S)
    elif S=="How are you":
        print("I am Currently : ",l1[B])
    else:
        print(l[B])
    
#i wrote this code mf 1st unit-71.5 1st sem-