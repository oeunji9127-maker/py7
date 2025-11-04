import random
import stuFunc


# 학생성적프로그램
while True:
    stuFunc.screen_print()
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:   #학생성적입력
     stuFunc.stu_input()
     
    elif choice == 2: #학생성적출력
        stuFunc.stu_print()
        
    elif choice == 3: #학생성적수정
        stuFunc.stu_modify()
        
    elif choice == 4: #학생성적삭제
        stuFunc.stu_del()
        
    elif choice==5: # 등수처리
        stuFunc.stu_rank()
        
    elif choice == 0: #프로그램종료
        print("[ 프로그램을 종료합니다. ]")
        print()
        break
    
    # 끝
