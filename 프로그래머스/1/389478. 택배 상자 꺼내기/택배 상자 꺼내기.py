def solution(n, w, num):
    result = 0
    _list = [[0]*w for i in range(int(n/w)+1)]
    cnt = 1
    for i in range(0,int(n/w)+1):
        if cnt > n: break
        elif i % 2 == 0:
            for j in range(0,w):
                _list[i][j] = cnt
                print(cnt)
                if cnt == num:
                    x,y = i,j
                cnt += 1
                if cnt > n: break
        elif i % 2 == 1:
            for k in range(w-1,-1,-1):
                _list[i][k] = cnt
                print(cnt)
                if cnt == num:
                    x,y = i,k
                cnt += 1
                if cnt > n: break
        
    for l in range(x, int(n/w)+1):
        if _list[l][y] != 0:
            result += 1
    print(_list)
    
    return result