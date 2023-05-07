def prime(num):
    if num<=1:
        return False
    for i in range(2,num//2+1):
        if(num%i==0):
            return False
            break
    else:
        return True
def emirp(num):
    if not prime(num):
        return False
    rev = 0
    while num!=0:
        rev = (rev*10)+(num%10)
        num//10
    return prime(rev)
n = 13
emirp(n)

