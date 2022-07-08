"""단계 1.1"""
"""단게 1.2 (수정)"""
"""단게 1.5(수정)"""
"""단게 1.6(수정)"""
"""단게 1.7(수정)"""
"""단게 1.8(수정)"""
"""단게 1.7(수정)"""
"""단계 1.8"""
"""단계 1.9"""
import random
order = random.randrange(0,2) 
total = list(range(1, 32)) 
count = list(range(1, 4)) 

i = 0

while i <= 31:    
    
    if i == 31 : 
        break
    
    if order % 2 == 0:
        num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
        while num not in range(0,4):
            print('1,2,3중 하나를 입력하세요.\n')
            num = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능)"))
        
        for count in range(num):
            i += 1
           
            print("player"+str(i))
            if i == 31:
                print("Computer Win!")
                break  
    
       
    else:
        computer = random.randrange(1,4)
        
        for count in range(computer):
            i += 1
            
            print("computer"+str(i))
            if i == 31:
                print("Player Win!")  
                break
    
    order += 1

    
