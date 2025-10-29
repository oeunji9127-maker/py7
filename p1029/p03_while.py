while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 입력")
    print("-"*80)
    num= int(input("원하시는 숫자를 입력해주세요>>"))
    if num==0:
        break
    elif num==1:
        print("1. 학생성적 입력")
        name= input("이름을 입력하시오>>")
        kor= int(input("국어점수를 입력하시오>>"))
        eng= int(input("영어점수를 입력하시오>>"))
        math= int(input("수학점수를 입력하시오>>"))
        total= kor+eng+math
        avg= total/3

        stu_list=[]
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
        


# 5번 동안 숫자를 입력받아 합계를 출력하시오

# sum=0
# for i in range(5):
#     num=int(input("숫자{}을 입력하세요".format(i+1)))
#     sum=sum+num
# print("숫자 5개의 총합계는 {}".format(sum))


# i=1
# sum=0
# while i<=5:
#     num=int(input("숫자{}을 입력하세요".format(i)))
#     sum=sum+num
#     i=i+1
# print("5개 숫자의 총합계:{}".format(sum))



# 1~10까지 합을 구하시오

# 1. for문을 사용
# num=0
# for i in range(1,11):
#     num=num+i
# print("1~10까지 총합계:",num)


# 2. while문을 사용
# sum=0
# i=1

# while i<=10:
#     sum=sum+i
#     i= i+1
# print(sum)



