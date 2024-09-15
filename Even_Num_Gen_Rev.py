#Program for generate Even Number in reverse order
n=int(input("Enter the number:"))
if n<=0:
    print("{} is invalid".format(n))
else:
    print("-"*50)
    print("Even Number Within {} ".format(n))
    print("-"*50)
    if n%2!=0 :
        n=n-1
        while n>=1 :
            print("\t\t {}".format(n))
            n=n-2
        else:
            print("-"*50)
