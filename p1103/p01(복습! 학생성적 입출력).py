stu_list= [
    [10101,"홍길동",100,100,100,300,100.00],  # 이름,국어,영어,수학,합계
    [10102,"유관순",90,90,90,270,90.00],
    [10103,"이순신",80,80,80,240,80.00]
]
stu_count=10104  # 학생번호
titles= ["번호","이름","국어","영어","수학","합계","평균"]


while True:
    print("[ 학생성적 프로그램 ]")
    print()
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 프로그램 종료")
    print()
    num=int(input("원하시는 숫자를 입력해주세요>>"))
    print()

# 학생입력부분
    if num==1:
        print("[ 학생성적 입력 ]")
        print()
        name=input("{}번 학생이름을 입력해주세요>> ".format(stu_count))
        stu_count+=1
        kor= int(input("국어점수를 입력해주세요>> "))
        eng= int(input("영어점수를 입력해주세요>> "))
        math= int(input("수학점수를 입력해주세요>> "))
        total= kor+eng+math
        avg= total/3
        stu_list.append= [stu_count,name,kor,eng,math,total,avg]
        print("입력이 완료되었습니다")
        print("-"*50)


# 학생출력부분
    if num==2:
        print("[ 학생성적 출력]")
        print()
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stus in stu_list:
            for stu in stus:
                print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*stus))
        print("출력이 완료되었습니다")
        
        