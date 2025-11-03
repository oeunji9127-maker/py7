stu_list= [ # 주소값이 저장되어있음
    [10101,"홍길동",100,100,100,300,100.00],  # 이름,국어,영어,수학,합계
    [10102,"유관순",90,90,90,270,90.00],
    [10103,"이순신",80,80,80,240,80.00]
]
stu_count=10104  # 학생번호
titles= ["번호","이름","국어","영어","수학","합계","평균"]
# titles: 항목번호
# titles: 과목번호 시작은 2번부터


def screen_print():
    print("[ 학생성적 프로그램 ]")
    print()
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    print("4. 학생성적 삭제")
    print("0. 프로그램 종료")
    print()
    
    
def stu_input():
    
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    # 전역변수 vs. 지역변수
    # 전역변수: 프로그램 전체에서 사용
    # 지역변수는 한정된 지역안에서만 사용
    # 지정한 변수를 전역변수로 사용하고 싶다면, 함수앞에 global을 붙여준다
    # 복합변수인 리스트는 값이 아닌 "주소"를 가지고 있으므로 굳이 global을 붙일 필요가 없다 
    
    global stu_count # 전역변수를 가져올때 사용
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


def stu_print():
   # 번호      이름    국어    수학    영어    합계    평균
    # 10104    오은지   100    100     100    300    100
    print("[ 학생성적 출력 ]")
    print(*titles,sep="\t")
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus)) 