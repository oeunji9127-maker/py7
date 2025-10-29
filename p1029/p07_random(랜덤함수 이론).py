import random  #random 클래스를 가져와서 쓰겠다.
# 임의로 하나의 숫자를 뽑는다

print(random.random())  # 0.000000000 <= x < 1.000000000
# random클래스 안에 random()함수를 사용하겠다는 뜻

import random
print(random.randrange(1,11))  # 1~10 사이의 숫자를 랜덤으로 가져온다
print(random.randint(1,11))    # 1~10 사이의 랜덤숫자 (randrange = randint)

print(random.sample([1,2,3,4,5],4))
# 해당 리스트에서 4개를 랜덤으로 가져옴, 중복이 안됨

print(random.choices([1,2,3,4,5],k=4))
# 해당 리스트에서 4개를 랜덤으로 가져옴, 중복가능

a_list= [1,2,3,4,5]
random.shuffle(a_list)
# 해당 리스트의 값을 랜덤으로 섞는다
print(a_list)


