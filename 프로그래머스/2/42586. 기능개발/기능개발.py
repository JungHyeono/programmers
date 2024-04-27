import math

def solution(progresses, speeds):
    times = []
    for i in range(len(progresses)):
        times.append(math.ceil((100-progresses[i])/speeds[i]))
    print(times)
    answer = []
    a_pos = 0
    t_pos = 0
    for i in range(len(times)):
        if not answer:
            answer.append(1)
        else:
            if times[i] <= times[t_pos]:
                answer[a_pos] += 1
            else:
                answer.append(1)
                t_pos = i
                a_pos += 1
                
    return answer