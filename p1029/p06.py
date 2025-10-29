n_list=[]
i= 0
while True:
    if i<3:
        name= input("{}번째 이름을 입력하세요".format(len(n_list)+1))
        kor= int(input("{}번째 국어점수를 입력하세요".format(len(n_list)+1)))
        n_list.append([name,kor])
        print(n_list)
    else: break
    i= i+1
print
    
    