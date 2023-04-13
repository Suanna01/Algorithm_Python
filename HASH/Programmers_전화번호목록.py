def solution(phone_book):
    answer = True
    hash = {}
    
    for phone_num in phone_book:
        hash[phone_num] = 1
        
    for phone_num in phone_book: # 각각 폰번호마다 검사
        temp = ""
        for num in phone_num: # 전화번호를 한글자 씩 쪼갬
            temp += num # 쪼갠 숫자가 반복문이 돌아갈 때마다 붙여나감
            if temp in hash and temp != phone_num: # 딕셔녀리의 키로 존재하는지 검사
                answer = False
    return answer