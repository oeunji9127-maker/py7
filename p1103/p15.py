# 로또 맟추기 프로그램
# 로또 3개를 자동번호 추출로 입력받아,
# 몇개가 맞는지 출력하시오

import random
# 로또번호
lotto= random.sample(range(1,46),6)
lotto.sort()

# 자동추출 내번호
rlist= []
print=("[ 나의 랜덤로또 ]")
for i in range(5):
    rlist.append(random.sample(range(1,46),6))
print(rlist)





            

