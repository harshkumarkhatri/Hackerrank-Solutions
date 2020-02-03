# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
t=""
f=""
for i in range(0,n):
    s=input()
    for j in range(0,(len(s))):
        if j%2==0:
            t=t+s[j]
        else:
            f=f+s[j]
    print(t+" "+f)
    t=""
    f=""
