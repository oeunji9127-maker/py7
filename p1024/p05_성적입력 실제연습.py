#이름 입력 - str (%s)
#국어점수 입력 - int (%d)
#수학점수 입력 - int (%d)
#영어점수 입력 - int (%d)
#합계 - int (%d)
#평균 - float (%f)

# %print를 사용해서 출력하시오.

# name= input("이름을 입력하시오.")
# print(name)
# print("%s" % name)
# 두개 모두 같은 의미

name= input("이름을 입력하시오.")
kor= int(input("국어점수를 입력하시오."))
eng= int(input("영어점수를 입력하시오."))
math= int(input("수학점수를 입력하시오."))
total= kor+eng+math
avg= (kor+eng+math)/3

print("%s님의 시험점수는 다음과 같습니다." % (name))
print("국어점수: %d, 수학점수: %d, 영어점수:%d" % (kor,math,eng))
print("세과목의 합계: %d, 세과목의 평균: %.2f" % (total,avg))


print("국어점수: %d\t수학점수: %d\t점수: %d" % (kor,math,eng))
print("합계: %d\t평균: %.2f" % (total,avg))
##역슬래시는 원화키를 누르면 된다.
## "\t" 는 Tap키와 같다.


      


 

