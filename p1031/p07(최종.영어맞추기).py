import random

english={
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea',
    '물':'water',
    '지구':'earth',
    '하늘':'sky',
    '공기':'air',
    '고양이':'cat',
    '강아지':'dog',
    '아기':'baby',
    '엄마':'mother',
    '아빠':'father',
    '집':'house',
    '소년':'boy',
    '소녀':'girl',
    '열쇠':'key'
}

# 20문제 중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오
count=0
a_list= list(range(20))
question=random.sample(a_list,5) # 랜덤5개: 20문제중 5문제 추출
question.sort()  # 랜덤5문제 순차정렬
correc_dic={}  # 정답,오답 입력을 위한 저장공간                
print(question)

for i,k in enumerate(english.keys()):  # 인덱스번호를 키와 함께 추출
    if i in question:
        print(i,k,english[k])
        
        # 문제출력
        print("{}번문제. {}는 영어로 무엇일까요?".format(i,k))
        answer= input(">>")
    
        # answer == v
        if answer==english[k]:
            print("띵동~~ 정답입니다~~!")
            correc_dic[k]="정답"
            count+=1
            print("-"*50)
            
        else:
            print("오답! 정답은 {}".format(english[k]))
            correc_dic[k]="오답"
            print("-"*50)
        
# 맞은개수 출력
for k,correc in correc_dic.items():  # correc_dic [사랑:정답  차:오답]
    print("{}:{}".format(k,correc),end="  ")
print("[ 맞 은 개 수 ]:{}".format(count))

        
            
        
        

