def secondRightmostZeroBit(n):
    return  -~((n-~(n^(n+1))//2)^(n-~(n^(n+1))//2+1))//2


print(secondRightmostZeroBit(37))
print(secondRightmostZeroBit(1073741824))