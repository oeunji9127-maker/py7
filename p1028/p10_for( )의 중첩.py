# 구구단 만들기
# for()문의 중첩

# for i in range(2,10):
#     print("[ {}단 ]".format(i))
#     for j in range(1,10):
#         print("{}X{}={},".format(i,j,i*j),end="  ")
#         if j==9: print("{}X{}={}".format(i,j,i*j))
#     print()


# 구구단 홀수단 출력하기
   
# for i in range(2,10):
#     if i%2==0:
#         print("[ {}단 ]".format(i))
#         for j in range(1,10): 
#             print("{}X{}={}".format(i,j,i*j),end="  ")
#         print()
        
# enumerate(리스트): 리스트번호,리스트값

fruits= ["사과","배","복숭아","딸기","바나나"]
print("[ 과일리스트 ]")
for i, fruit in enumerate(fruits):
    print("{}.{}".format(i+1,fruit),end="  ")
    
# for i, fruit in enumerate(fruits)
# for 리스트번호, 리스트값 in enumerate(리스트) 



    





    

            
            
            
            
            
            
            
            
            
            
            
            
        
            
        

