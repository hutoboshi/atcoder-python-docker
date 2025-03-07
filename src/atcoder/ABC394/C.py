def transform_string(s):
  s=list(s)
  n=len(s)
  cur=0
  
  while cur<n-1:
    if s[cur]=="W" and s[cur+1]=="A":
      s[cur]="A"
      s[cur+1]="C"
      if cur>0:
        cur-=1
    else:
      cur+=1
  return "".join(s)

s=input()
print(transform_string(s))
