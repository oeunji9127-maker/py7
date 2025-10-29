a_list= range(1,10)  # 1-9 까지의 숫자리스트
for i in a_list:
    print(i,end="  ")
    if i%3==0:
        print()
print("-"*80)
    
    
# 4 * 4 리스트형태로 출력해라
# 1 2 3 4 
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16 

n_list= range(1,17)  # 1-16 까지의 숫자리스트
for i in n_list:
    print("{}".format(i),end="\t")
    # "{}".format(),end=" "
    # 연속적인 i를 연이어서 출력하는 end=" "는 for반복문에서 이용
    if i%4==0:
        print()
print("-"*80)

# [ 3 * 3 리스트 형태]
a_list= [[1,2,3],[4,5,6],[7,8,9]]

for aa in a_list:  # >>[1,2,3]
    for a in aa:   # >> 1
        print(a,end="\t")
        if a%3==0:
            print()
        
a_list= [9,1,2,5,6,8,3,4,7]  # 주소 0-9


# enumerate함수로 index(주소번호) 지정하기
for i,value in enumerate(a_list):
    print(value,end="\t")
    if (i+1)%3==0:
        print()
print("-"*80)


### 4 * 4 리스트 형태로 출력하시오

import random
a_list= list(range(1,17))  # 1-16
random.shuffle(a_list)

for i,value in enumerate(a_list):
    print(value,end="\t")
    if (i+1)%4==0:
        print()
print("-"*80)


        