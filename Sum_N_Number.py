#Program for print the sum of First N number
n=int(input("Enter How Many Natural Nums Sum u want:"))
if n<=0:
    print("{} is Invalid input".format(n))
else:
    s=0
    i=1
    print("-"*50)
    print("Sum of {} Natural Number".format(n))
    print("-"*50)
    while i<=n:
        print("\t\t {}".format(i))
        s=s+i
        i=i+1
    else:
        print("-"*50)
        print("\t\tsum={}".format(s))
        print("-"*50)
print("*"*50)
print("With the Help of for loop")
print("-"*50)
s=0
for i in range(1,n+1):
    s=s+i
    print("\t\t{}".format(i))
else:
    print("-"*50)
    print("\tsum={}".format(s))
    print("-"*50)
