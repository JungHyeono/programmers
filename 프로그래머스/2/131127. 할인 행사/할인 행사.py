def solution(want, number, discount):
    count = 0
    
    want_dict = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount) - 9):  # 10일 간격으로 확인하기 때문에, 끝에서 9일 전까지만 반복
        current_discount = discount[i:i+10]
        discount_dict = {}
        
        for item in current_discount:
            if item in discount_dict:
                discount_dict[item] += 1
            else:
                discount_dict[item] = 1
        
        match = True
        for item in want_dict:
            if item not in discount_dict or discount_dict[item] < want_dict[item]:
                match = False
                break
        
        if match:
            count += 1
    
    return count
