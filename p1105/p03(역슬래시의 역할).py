print('안녕하세요. \"홍길동\"입니다')
# 역슬래시(\): 문자열 안의 특수문자를 문자로 인식하라는 뜻

import os
f= open("C:/down/aaa.txt","r",encoding="utf8")
f= open("C:/down/bbb.txt","r",encoding="utf8")

# 3개 출력하시오
# 3개를 a_list 리스트에 추가하시오

a_list=[]
while True:
    txt= f.readline()
    if txt=="":break
    a_list.append(txt.stirp.split(","))
    # strip 스트립: 공백제거, split 스플릿: 문자열 분리구분
f.close()

print(a_list)


# txt= f.readline()
# print(txt.strip()) # strip: 공백제거
# print(txt.strip().split(",")) 
# # 문자열을 구분자 쉼표를 기준으로 분리해 리스트타입으로 저장
# # split: 리스트 안에 들어있는 요소들의 타입은 문자열!! 점수를 사용하려면 타입변환이 필요!
# print(txt.split(",")[5])  # 합계 출력
# f.close()

