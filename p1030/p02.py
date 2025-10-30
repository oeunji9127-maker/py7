import random

a_list= list(range(1,10))

random.shuffle(a_list)
print(a_list)

for i,val in enumerate(a_list):
    print(val,end="  ")
    if (i+1)%3==0:
        print()
        

        
        
        
        
        
        

