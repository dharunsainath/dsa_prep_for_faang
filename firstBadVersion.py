

def firstBadVersion(n):
    left=1
    right=n
    while (left < right):
        mid = left + (right - left) / 2
        if isBadVersion(int(mid)):
            right = mid
        else:
            left = mid + 1
        
    
    return int(left)


def isBadVersion(n):
    arr=[False,False,False,False,True,True]

    return(arr[n])

print(firstBadVersion(6))
