stu_list= [
    [10101,"홍길동",100,100,100,300,100.00],  # 이름,국어,영어,수학,합계
    [10102,"유관순",90,90,90,270,90.00],
    [10103,"이순신",80,80,80,240,80.00]
]
stu_count=10104  # 학생번호
titles= ["번호","이름","국어","영어","수학","합계","평균"]
# titles: 항목번호
# titles: 과목번호 시작은 2번부터

### 학생성적입력, 출력, 수정, 삭제를 구현하시오


# 학생성적 프로그램 처음시작 페이지
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

    # 1. 학생성적 입력
    if num==1:
        print("[ 학생성적 입력 ]")
        print()
        name= input("{}번 학생 이름을 입력해주세요: ".format(stu_count))
        
        # 10104번 학생이름을 입력해주세요: 오은지
        # 국어점수 100
        # 영어점수 100
        # 수학점수 100
        # 입력이 완료되었습니다
        
        kor= int(input("국어점수를 입력해주세요>> "))
        eng= int(input("영어점수를 입력해주세요>> "))
        math= int(input("수학점수를 입력해주세요>> "))
        total= kor+eng+math
        avg= total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count+=1
        print("입력이 완료되었습니다")
        print("-"*50)
        print()

    # 학생성적 출력
    elif num==2:
        # 번호      이름    국어    수학    영어    합계    평균
        # 10104    오은지   100    100     100    300    100
        print("[ 학생성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*stus))   


    # 학생성적 수정
    elif num==3:
        print("[ 학생성적 수정 ]")
        print()
        
        for i,stu in enumerate(stu_list):
            print("{}. {}".format((i+1),stu[1]))
        print()
        # 1. 홍길동
        # 2. 유관순
        # 3. 이순신
        # 4. 오은지
        
        # 수정하려는 학생번호를 입력하세요
        stu_name_num=int(input("수정하려는 학생번호를 입력하세요>> "))
        print()
        
        # 1. 국어점수
        # 2. 수학점수
        # 3. 영어점수 ->>(출력)
        # 수정하려는 과목의 번호를 입력하세요(1~3)->>(입력)
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수 ")
        print()
        sub_num= int(input("수정하려는 과목의 번호를 입력하세요>> "))
        sub_score= int(input("수정하려는 과목의 점수를 입력해주세요>> "))
        stu_list[stu_name_num-1][sub_num+1]= sub_score
        print("수정이 완료되었습니다")
        print(stu_list[stu_name_num-1])
        print("-"*50)
        print()
    
    
    # 학생성적 삭제    
    elif num==4:
        print("[ 학생성적 삭제 ]")
        
        for i,stu in enumerate(stu_list):
            print("{}. {}".format((i+1),stu[1]))
        print()
        # 1. 홍길동
        # 2. 유관순
        # 3. 이순신
        # 4. 오은지
        
        # 삭제하려는 학생번호를 입력하세요
        stu_name_num=int(input("삭제하려는 학생번호를 입력하세요>> "))
        print()
        del stu_list[(stu_name_num-1)]
        print("해당학생의 점수리스트가 삭제되었습니다")
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*stus))
        print("-"*50)
        print()


    elif num==0:
        print("프로그램 종료")
        break


