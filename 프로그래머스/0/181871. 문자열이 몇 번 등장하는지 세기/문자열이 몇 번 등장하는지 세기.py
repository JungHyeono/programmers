def solution(myString, pat):
    count = 0
    k = myString.find(pat)
    for i in range(len(myString)):
        if k > -1:
            myString = myString[k+1:]
            print(myString)
            count += 1
        else: break
        k = myString.find(pat)
    return count