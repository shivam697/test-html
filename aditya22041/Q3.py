n = int(input())
a=[]
for i in range(n):
    x= int(input())
    a.append(x)
T= int(input())
def solve(n,a,T):
        s=0
        for i in range(n):
            s+=a[i]
            if(s>=T):
                return i+1
        return -1
print(solve(n,a,T))


def _test():
     assert solve(5,[100,200,300,400,500],750)==4
_test()