print("%d %d" % (100,200))
# %를 넣은만큼 %에 넣을 값의 개수를 맞춰줘야한다.

# str1= "이름"
# str2= "국어"
# str3= "수학"
# str4= "영어"
# str5= "합계"
# str6= "평균"

name= input("이름을 입력하시오.")
kor= int(input("국어점수를 입력하시오."))
math= int(input("수학점수를 입력하시오."))
eng= int(input("영어점수를 입력하시오."))
total= kor+math+eng
avg= (kor+math+eng)/3

print("-"*50)
print("이름\t%s" % (name))
print("국어점수:%d\t수학점수:%d\t영어점수:%d" % (kor,math,eng))
print("합계:%d\t평균:%.2f" % (total,avg) )
print("-"*50)



