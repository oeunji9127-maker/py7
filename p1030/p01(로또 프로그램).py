# 로또 맞추기 프로그램을 구현하시오

# 1. 변수선언
import random
lotto= random.sample(range(1,46),6)
lotto.sort()

mynum_list=[]

# 2. 6개 번호생성
for i in range(1,7):
    mynum= int(input("숫자{}을 입력하세요(1~45)".format(i)))
    if 1<= mynum <=45:
        mynum_list.append(mynum)
    else: print("숫자를 잘못입력하셨습니다")
    
mynum_list.sort()
print("[ 입력한 번호 ]:{}".format(mynum_list))
print("[ 당 첨 번 호 ]:{}".format(lotto))

count=0
correc_list=[]
for n in lotto:
    for mn in mynum_list:
        if n==mn:
            count= count+1
            correc_list.append(mn)
print("[ 맞 은 숫 자 ]:{}".format(correc_list))
print("[ 맞 은 개 수 ]:{}".format(count))

if count<2:
    print("[ 당 첨 금 ]: 0원, 다음기회에")
elif count==3:
    print("[ 당 첨 금 ]: 5천원, 축하합니다!")
elif count==4:
    print("[ 당 첨 금 ]: 5만원, 축하합니다!")
elif count==5:
    print("[ 당 첨 금 ]: 300백만원, 축하합니다!")
elif count==6:
    print("[ 당 첨 금 ]: 20억원, 축하합니다! 당첨입니다")
            



