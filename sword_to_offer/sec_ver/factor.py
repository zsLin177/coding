'''
数的质因子分解
'''

def decode1(num, path):
    '''
    递归
    '''
    if num == 1:
        return
    i = 2
    while num%i != 0:
        i += 1
    path.append(i)
    decode1(num//i, path)

def decode2(num):
    '''
    非递归
    '''
    res = []
    remain = num
    while remain > 1:
        for i in range(2, num+1):
            if remain%i == 0:
                res.append(i)
                remain = remain // i
                break
    
    return res


if __name__ == '__main__':
    path = []
    decode1(617, path)
    print(path)
    print(decode2(617))
