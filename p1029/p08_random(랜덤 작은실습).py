# randomrange()를 사용해서 1~10까지의 랜덤숫자를 3개를 출력하시오
# import random
# for i in range(3):  
#     # 변수i가 범위 [0,1,2]안에서 돌고 있으므로 i증식식을 굳이 적어줄 필요가 없다 
#     print(random.randrange(1,11),end="  ")

# import random
# print(random.sample(range(1,11),3))
# 1~10까지 중복이 되지 않게 숫자3개를 뽑는다

# 1~10사이에 있는 랜덤숫자 생성

import random
r_num= random.randrange(1,21)
n_list=[]

for i in range(10):
    my_num=int(input("숫자를 입력하세요>>"))
    n_list.append(my_num)
    if r_num==my_num:
        print("당첨되었습니다")
        print("당첨번호: {}".format(r_num))
        print("입력번호: {}".format(n_list))
        break
    elif r_num>my_num: print("더 큰 수를 입력하세요>>")
    else: print("더 작은 수를 입력하세요>>")

