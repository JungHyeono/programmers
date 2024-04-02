def solution(people, limit):
    answer = 0
    left = 0                # 투포인트를 이용
    right = len(people)-1   # right는 배열 끝을 가르킴
    people.sort()           # 오름차순으로 정렬해 비교하는 방식
    while left <= right:
        if people[left] + people[right] <= limit: # 둘이 더한값이 limit보다 작으면
            left +=1    # left가 오른쪽으로
            right -=1   # right가 왼쪽으로
            answer+=1   # 구명보트 1개 증가
        else:
            right-=1    # 아닐경우 오른쪽만 줄어듦
            answer+=1   # 보트개수 1개 증가

    return answer