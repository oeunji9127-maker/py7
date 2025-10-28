# # 1~5 for문을 사용해서 출력하시오
# for i in range(1,5+1):
#     print(i)

# # 숫자를 입력받아, 입력받은 값을 출력하는 것을 5번 반복하시오
# for i in range(5):
#     num= int(input("숫자를 입력하시오"))
#     print(num)



# 1부터 10까지 숫자의 합을 출력하시오
# sum= 0
# for i in range(1,10+1):
#     sum= sum + i
# print("총합계: {}".format(sum)) 

# # 10번 숫자를 입력하여 숫자의 합을 구하시오
# sum= 0
# for i in range(1,7+1):
#     num= int(input("숫자{}을 입력하시오".format(i)))
#     sum= sum + num
# print("7번 입력하신 숫자의 총합계는 {}입니다".format(sum))


# 1에서 10까지 홀수 합계를 구하시오
sum= 0
for i in range(1,11,2):
    sum= sum + i
print("1~10 까지 홀수의 총합계:",sum)

sum= 0
for i in range(1,10+1):
    if i%2==1:
        sum= sum + i
print("1~10 까지 홀수의 총합계: {}".format(sum))

        
# for문
# for문의 구조: " for 변수 in 범위 (range,list,문자열)"

# for i in range(5):  # 0~4
#     print(i)
    
# # 반갑습니다 10번 출력하시오
# for i in range(5):
#     print("반갑습니다")
    
    
# a_list= []
# for i in range(1,3+1):
#     num= int(input("숫자{}을 입력하시오>>".format(i)))
#     a_list.append(num)
    
# print("리스트: ",a_list)



# 조건문이 포함된 반복문

# a_list=[]
# for i in range(1,10+1):
#      num= int(input("숫자{}을 입력하세요".format(i)))
#      if num%2==0:
#          break  # 반복문을 중지하는 명령어
#      a_list.append(num)
# print("리스트: ",a_list)
