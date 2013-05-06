def gcdRecur(a,b):

    if b == 0:
        return a
        
    else:
        return gcdRecur(b, a%b)
    # b is zero - happy days




print(gcdRecur(6,12))
# -> (12,6) -> (6,0) -> 6
print(gcdRecur(9,12))
# -> (12,9) -> (9, 3) -> (3, 0)
print(gcdRecur(17,12))
# -> (12,5) -> (5, 2) -> (2,1) -> (1,0)
print(gcdRecur(6,0))
