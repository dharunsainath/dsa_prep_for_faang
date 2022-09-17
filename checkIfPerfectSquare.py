def checkPerfectSquare(N, start, last):
 
   
    mid = int((start + last) / 2)
 
    if (start > last):
        return False
 
    
    if (mid * mid == N):
        return True
 
   
    elif (mid * mid > N):
        return checkPerfectSquare(N, start,
                                  mid - 1)
 
    
    else:
        return checkPerfectSquare(N, mid + 1,
                                  last)
 
# Driver code
N = 100
print (checkPerfectSquare(N, 1, N))