def calculate_love_score(name1,name2):
    both = name1.upper()+ name2.upper()
    v1 = 'TRUE'
    v2='LOVE'
    total1= 0
    for i in v1:
        count = 0 
        for j in both:
            if j == i:
                count += 1
        # print(f'{i} occurs {count} times')
        total1 += count
    total2 = 0
    for i in v2:
        count2 = 0
        for j in both:
            if j == i:
                count2+=1
        # print(f'{i} occurs {count2} times')
        total2 += count2
    print(f'Your love score is {str(total1) + str(total2)}')    

calculate_love_score(name1=input('enter first persons name : '), name2=input('enter second persons name : '))

