stu_list= [
    ["홍길동",90,90,90,270],  # 이름,국어,영어,수학,합계
    ["유관순",100,100,100,300],
    ["이순신",80,80,80,240]
]
titles= ["이름","국어","영어","수학","합계"]

print("-"*50)
print(""*15,"[ 학생성적 프로그램 ]")
print("-"*50)
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("-"*50)
choice= int(input("원하는 번호를 입력하세요>>"))
print()

# 학생성적 출력
if choice==2:
    print(""*15,"[ 학생성적 리스트 ]")
    print()
    print("{}\t{}\t{}\t{}\t{}\t".format(*titles))
    print("-"*50)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}".format(*stus))
        
        
    
    
    
    

