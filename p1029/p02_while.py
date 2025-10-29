# while 조건:

# for i in range(10):
#     print(i)
    
# i= 0  # 초기값
# while i<10:
#     print(i)
#     i = i+1

num=1    
for i in range(10000):
    if num==0:
        print("프로그램을 종료합니다")
        break
    num=int(input("숫자를 입력하세요 (0입력:프로그램종료) >>"))
    print("입력한 값:",num)
    
    
    
