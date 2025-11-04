import random
import stuFuncone


# 학생성적프로그램
while True:
    stuFuncone.screen_print()
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:   #학생성적입력
     stuFuncone.stu_input()
     
    elif choice == 2: #학생성적출력
        stuFuncone.stu_print()
        
    elif choice == 3: #학생성적수정
        stuFuncone.stu_modify()
        
    elif choice == 4: #학생성적삭제
        stuFuncone.stu_del()
        
    elif choice==5: # 등수처리
        stuFuncone.stu_rank()
        
    elif choice == 0: #프로그램종료
        print("[ 프로그램을 종료합니다. ]")
        print()
        break
    