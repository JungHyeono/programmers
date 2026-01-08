while(True):
    num = input()
    if num == '0':
        break
    else:
        pass
    nlst = []
    _ispal = True
    for i in num:
        nlst.append(i)
    for j in range(0, int(len(nlst)/2)):
        if nlst[j] == nlst[-j-1]:
            pass
        else:
            _ispal = False
            break
    print("yes" if _ispal == True else "no")