s=input('enter your string')
l=len(s)
mid=int(l/2)
rev=-1
for a in range(mid):
    if s[a]==s[rev]:
        a+=1
        rev-=1
    else:
        print(s,"is not palindrome")
        break
else:
    print(s,"palindrome")
