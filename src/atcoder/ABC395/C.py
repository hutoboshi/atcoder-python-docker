n=int(input())
a=list(map(int,input().split()))
ans=n
if len(set(a))==n:exit(print(-1))
from collections import deque,defaultdict
q=deque()
cnt=defaultdict(int)
l=-1
r=0
for r in range(n):
  q.append(r)
  cnt[a[r]]+=1
  if cnt[a[r]]==2:
    while len(q) and cnt[a[r]]>1:
      idx=q.popleft()
      cnt[a[idx]]-=1
      l=idx
  ans=min(ans,r-l+1,ans)
print(ans)