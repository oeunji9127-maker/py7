# for 변수 in 범위:
# for i in range(10):  # 범위 0~9
# for i in [0,1,2,3,4,5,6,7,8,9]:

# for i in [50,3,26,99,88]:
#     print(i)
# # 50,3,26,99,88이 차례대로 출력

# for i in range(2):  # [0,1,2,3,4]
#     print(i,end="  ")

# # 1~10까지 합을 구하시오
# sum=0
# for i in range(1,10+1):
#     sum= sum+i
#     print("누적합계: {}".format(sum))

sum=0
for i in range(1,21):  # [0,1,2..19,20]
    sum= sum + i
    if sum>100:
        break
    
    print("{}번째 누적합: {}".format(i,sum))
print(f"누적합이 100이 넘지 않는 선에서 합한 누적합은 {sum-i}입니다.")

# result= 1
# for i in range(1,11):
#     result= result*i
#     print("{}번째 누적곱{}".format(i,result))
# print(f"10번째까지의 누적곱은 {result}입니다")


