def gcdIter(a, b):
    gcd = ''
    num = min(a,b)
    for i in reversed(range(1, 1 + num)):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
        else:
            continue
    return gcd