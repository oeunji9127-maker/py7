def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# 방법1
# while True:
#     a= int(input("숫자1을 입력하세요>> (0.프로그램종료)"))
#     if a==0:
#         print("프로그램을 종료합니다")
#     b= int(input("숫자2를 입력하세요>> "))
#     cal(a,b)

# 두수를 입력해서 사칙연산을 하시오. 함수를 사용할 것
# 무한반복되도록 하시오
# 0을 입력하면 프로그램을 종료하시오



# 방법2
# i=0
# a_list=[0,0]

# print("[ 사칙연산 프로그램 ]")
# while True:
#     a= input("숫자를 입력하세요>> ")
#     if a.isdigit(): # 숫자인지 확인하는 작업, 그래서 input을 입력할때도 굳이\
#         # int타입을 지정해주지 않아도 된다  
#         a_list[i]= int(a)
#         i+=1
#     else: print("숫자만 입력가능합니다")
#     if i==2: break
# cal(a_list[0],a_list[1])


    

