# 숫자를 입력받아 100보다 큰수인지 아닌지 출력하시오.
# 100보다 큰수입니다.
# 100보다 작은수입니다.

# num= float(input("실수를 입력해주세요."))
# if(num<100):
#     print("100보다 작은 수 입니다.")
# else:
#     print("100보다 큰 수입니다.")


# 입력된 숫자가 짝수인지 홀수인지 출력하시오.
# 홀수입니다. 짝수입니다.
# num%2==0

# num= int(input("숫자를 입력해주세요."))
# if(num%2==0):
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")


# 현재시간 구하기
# 파이썬에서 제공해주는 내부모듈(class) 
   
# 요건 반드시 외워두세요.. 내부모듈 알아두면 좋아요!   
import datetime
now= datetime.datetime.now()
print(now)

print(now.year,"년도")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

# 입력한 주민번호의 월을 파악해서 현재날짜와 같은 월이면
# 이벤트 대상입니다. 이벤트 대상이 아닙니다.를 출력하세요.

print("현재날짜의 월과 주민번호의 월이 같으면 선물을 드립니다.")
jumin= input("주민번호를 입력해주세요.")
if(int(jumin[2:4])==now.month):
    print("축하합니다. 이벤트에 당첨되셨습니다.")
else:
    print("아쉽지만 이벤트당첨은 다음기회에...")
    
    