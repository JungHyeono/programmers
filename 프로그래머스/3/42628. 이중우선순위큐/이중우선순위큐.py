def solution(operations):
    queue = []
    for i in operations:
        if i[0] == 'I':
            queue.append(int(i[2:]))
        elif i == 'D 1' :
            if not queue :
                continue
            else : del queue[queue.index(max(queue))]
        else:
            if not queue :
                continue
            else : del queue[queue.index(min(queue))]
    return [0,0] if not queue else list([max(queue),min(queue)])