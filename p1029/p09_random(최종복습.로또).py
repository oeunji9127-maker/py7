# 6개의 숫자를 입력받아 출력하시오
# 로또 기계만들기

# 클래스 선언 
import random

# 로또번호 생성
lotto= (random.sample(range(1,46),6))  # 중복되지 않게 1~45 사이에서 숫자6개 고르기
lotto.sort()

# 변수 선언 
num_list=[]
corr_list=[]

# 숫자 입력
for i in range(1,7):
    num=int(input("숫자{}을 입력하세요 (1~45)".format(i)))
    num_list.append(num)
num_list.sort()
print("[ 입력한 숫자 ]:{}".format(num_list))
print("[ 결 과 화 면 ]:{}".format(lotto))
count=0

# 당첨번호 확인
# 결과화면 출력
for i in lotto:
    for j in num_list:
        if i==j:
            count=count+1
            corr_list.append(j)
            break
print("[ 맞 은 개 수 ]:{}".format(count))
print("[ 맞 은 숫 자 ]:{}".format(corr_list))

# 당첨금 출력
if len(corr_list)<2:
    print("[ 당 첨 금 ]: 0원 당첨은 다음기회에..")
elif len(corr_list)==2:
    print("[ 당 첨 금 ]: 5천원")
elif len(corr_list)==3:
    print("[ 당 첨 금 ]: 5만원")
elif len(corr_list)==4:
    print("[ 당 첨 금 ]: 백만원")
elif len(corr_list)==5:
    print("[ 당 첨 금 ]: 5천만원")
elif len(corr_list)==6:
    ("[ 당 첨 금 ]: 20억 로또에 당첨되었습니다 축하합니다!!")
