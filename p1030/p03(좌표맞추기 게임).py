import random

a_list= list(range(1,26))
random.shuffle(a_list)
print(a_list)


while True:
    print("[ 좌표 맞추기 게임 ]")
    print("-"*50)
    for i,val in enumerate(a_list):
        print(val,end="\t")
        if (i+1)%5==0:
            print()
    print("-"*50)

    num=int(input("원하는 번호를 입력하세요>>"))
    print()
    
    for i,val in enumerate(a_list):
        if num==val:
            a_list[i]="x"
            break
        
            
            
        
