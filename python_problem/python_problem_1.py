"""단계 1.1"""
num = 0
i =1
sum = 0
"""단게 1.2 (수정)"""
num = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력가능) :")

if num.isdigit():
    if (int(num) not in (1,2,3)):
        print("1,2,3 중 하나를 입력하세요. \n")
else:
    print("정수를 입력하세요. \n")

"""단게 1.3"""
num = int(num)
for i in range(int(num)):
    print("playerA: %d \n" %(i+1))
sum += num
"""단게 1.4"""


num = input("부를 숫자의 개수를 입력하세요(1,2,3만 입력가능) :")    
if num.isdigit():
    if (int(num) not in (1,2,3)):
        print("1,2,3 중 하나를 입력하세요. \n")
else:
    print("정수를 입력하세요. \n")
num = int(num)
for i in range(int(num)):
    print("playerB: %d \n" %(sum+i+1))

"""단게 1.5(수정)"""