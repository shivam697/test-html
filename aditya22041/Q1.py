n = int(input())
a = list(map(int, input().split()))

def solve(n ,a):
    s=0
    for i in a:
         s+=i
    av = s//n
    ans = []
   
    for i in range(n):
        
        if(a[i]>=av):
            
            ans.append(a[i])
    return av, ans
av , ans = solve(n,a)
print(av)
for i in ans:
    print(i, end=' ')
def _test():
    assert solve(5,[20, 30, 50, 10, 40])==(30,[30,50,40])
    assert solve(4,[10,10,10,10])==(10, [10,10,10,10])
_test()