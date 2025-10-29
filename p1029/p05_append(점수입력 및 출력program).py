name= input("이름을 입력하시오>>")
kor= int(input("국어점수를 입력하시오>>"))
eng= int(input("영어점수를 입력하시오>>"))
math= int(input("수학점수를 입력하시오>>"))
total= kor+eng+math
avg= total/3


stu_list=[]

# 리스트.append(해당값): 리스트 안에 해당값을 맨뒤에 추가
stu_list.append(name)
stu_list.append(kor)
stu_list.append(eng)
stu_list.append(math)
stu_list.append(total)
stu_list.append(avg)
print(stu_list)

print("이름: {}".format(stu_list[0]))
print("국어: {}".format(stu_list[1]))
print("수학: {}".format(stu_list[2]))
print("영어: {}".format(stu_list[3]))
print("합계: {}".format(stu_list[4]))
print("평균: {:.2f}".format(stu_list[5]))
print("-"*80)
print("이름:{}  국어:{}  영어:{}  수학:{}  합계:{}  평균:{:.2f}".format(*stu_list))








