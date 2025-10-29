# for 변수 in 범위
# pass: 빈공백
# for,if문은 한줄이라도 코드가 없으면 에러가 나기에 pass를 작성
# break: 반복문을 종료
# continue: 그회차 반복문을 발생시키지 않음

# for i in range(10):
#     pass  # 아무것도 일어나지 않음: 빈공백과 같음
#     # print() # 이것도 가능
#     print ("프로그램 종료") 
#     break # 이 시점에서 반복문을 종료해라

# for i in range(10):
#     if i%2==0:
#         continue  # 짝수는 출력되지 않음
#     print(3)
#     # 홀수만 출력, 짝수는 스킵
    
# for i in range(2,9):  # 2-8
#     for j in range(1,10): # 1-9
#         print("숫자: ",j)
#     print("-"*50)
    
# for i in range(2,10):  # 2-9 (8번반복)
#     print(i)
#     for j in range(1,9):  # 1-8 (8번반복)
#         pass
#         print("-"*50)

# for i in range(2,10):  # (2-9) 8번
#     print(i)
    
# for i in range(10):
#     if i%2==1:
#         print(i)
# print("-"*50)

# for i in range(10):
#     if i%2==0:
#         continue  # if 조건문 안에 있는 항목을 제외하고 반복시킴
#     print(i)
# print("-"*80)



    
# 구구단을 출력하시오
for i in range(2,10):
    print("[ {} ]단".format(i))
    for j in range(1,10):
        print("{}X{}={}".format(i,j,i*j),end="  ")
    print()
    print("-"*80)
    
    
    
    
    
    
        
        

