# Enter your code here. Read input from STDIN. Print output to STDOUT
date1=str(input()).split(" ")
da=int(date1[0])
ma=int(date1[1])
ya=int(date1[2])
fine=0
date2=str(input()).split(" ")
dd=int(date2[0])
md=int(date2[1])
yd=int(date2[2])


if ya > yd:
    fine = 10000
elif ya == yd:
    if ma > md:
        fine = (ma - md) * 500
    elif ma == md and da > dd:
        fine = (da - dd) * 15

print(fine)
