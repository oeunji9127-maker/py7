stu_list= [
    ["홍길동",90,90,90,270],  # 이름,국어,영어,수학,합계
    ["유관순",100,100,100,300],
    ["이순신",80,80,80,240]
]
titles= ["이름","국어","영어","수학","합계"]

while True:
    
    print("[ 학생성적수정 ]")
    print("0. 홍길동")
    print("1. 유관순")
    print("2. 이순신")
    print("-"*30)
    num= int(input("수정하려는 학생번호를 입력하세요>>"))
    print("[ {}학생을 선택했습니다 ]".format(stu_list[num][0]))
    print("-"*50)

    print("1. 국어성적 수정")
    print("2. 영어성적 수정")
    print("3. 수학성적 수정")
    print("-"*50)
    print()

    subject= int(input("수정할 과목을 선택하세요>>"))
    print("[ {}학생 {}점수 수정 ]".format(stu_list[num][0],titles[subject]))
    print("-"*50)
    
    print("현재 {}점수:{}".format(titles[subject],stu_list[num][subject]))
    score= int(input("수정할 점수를 입력하세요>>"))
    print(score)
    stu_list[num][subject]=score
    stu_list[num][4]=stu_list[num][1]+stu_list[num][2]+stu_list[num][3]
    print(stu_list[num])
    print("-"*50)
    print()

















