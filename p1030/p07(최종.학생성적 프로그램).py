stu_list= [
    [101010,"홍길동",100,100,100,300,100],  # 이름,국어,영어,수학,합계
    [101011,"유관순",90,90,90,270,90],
    [101012,"이순신",80,80,80,240,80]
]
titles= ["번호","이름","국어","영어","수학","합계","평균"]
stu_count=101010  # 학생번호

# 학생성적 프로그램
while True:
    print("-"*50)
    print("[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 프로그램 종료")
    choice= int(input("원하는 번호를 입력하세요>>"))
    
    if choice==1:
        print("[ 학생성적 입력 ]")
        name= input("{}번 학생이름을 입력하세요>>".format(stu_count))
        kor= int(input("국어점수를 입력해주세요>>"))
        eng= int(input("영어점수를 입력하세요>>"))
        math= int(input("수학점수를 입력해주세요>>"))
        total= kor+eng+math
        avg= total/3
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count+=1  # 학생번호 1증가
        print("성적입력이 완료되었습니다")
        print()
        
    elif choice==2:  # 학생성적 출력
        print("[ 학생성적 리스트 ]")
        print()
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*titles))
        print("-"*50)
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus)) 
        
    elif choice==3:
        print("[ 학생성적 수정 ]")
        print()
        # 1. 101010 홍길동
        # 2. 101011 유관순
        # 3. 101012 이순신
        for i,stus in enumerate(stu_list):
            print("{}. {} {}".format((i+1),stus[0],stus[1]))
        print("-"*50)
        choice= int(input("수정하려는 번호를 입력하세요>>"))
        # 1
        print("[ {}학생 수정과목 선택 ]".format(stu_list[choice-1][1]))
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        
        # subject: 1국어, 2영어, 3수학
        # [국어 영어 수학주소]: 2국어, 3영어, 4수학
        # titles: [0번호 1이름 2국어 3영어 4수학 5합계 6평균]
        # stu_list= [(0)101010, (1)홍길동, (2)100, (3)100, (4)100, (5)300, (6)100]
        
        print("-"*50)
        subject= int(input("수정하려는 과목을 선택하세요>>"))
        # 0=choice-1: [101010,"홍길동",90,90,90,270]
        print("-"*50)
        print("현재 {}점수: {}".format("titles[subject+1]",\
            stu_list[choice-1][subject+1]))
        print("-"*50)
        
        # 점수 수정
        score= int(input("수정할 점수를 입력하세요>>"))
        stu_list[choice-1][subject+1]= score
        
        # 합계 수정
        stu_list[choice-1][5]=\
            stu_list[choice-1][2]+stu_list[choice-1][3]+stu_list[choice-1][4]
        
        # 평균 수정
        stu_list[choice-1][6]= stu_list[choice-1][5]/3
         
        print("{}점수 {}점으로 수정이 완료되었습니다.".format\
            (titles[subject+1],score))
        print(stu_list[choice-1])
        print()
        
        
    elif choice==4:
        print("[ 학생성적 삭제 ]")
        print()
        # 1. 101010 홍길동
        # 2. 101011 유관순
        # 3. 101012 이순신
        for i,stus in enumerate(stu_list):
            print("{}. {} {}".format((i+1),stus[0],stus[1]))
        print("-"*50)
        choice= int(input("삭제하려는 번호를 입력하세요>>"))
        flag= int(input("{}번 {}학생이 맞습니다까? (1.yes, 2.no)".format\
            (stu_list[i][0],stu_list[i][1])))
        if flag==2:
            print("삭제가 취소되었습니다")
            continue
        
        # 삭제부분
        del stu_list[choice-1]
        print("삭제가 되었습니다")
        print(stu_list)
        print()
        
    elif choice==0: pass
    else: 
        print("원하는 번호를 제대로 입력해주세요")
    
    
    
    
    
    
    
    
    
    