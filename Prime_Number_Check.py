#Program for to decide The Given Number Prime or Not
n=int(input("Enter the Number:"))
res = "Prime Number"
if n<=1:
    print("{} is Invalid Input".format(n))
else:

    i=2
    while i<n:
        if n%i==0:
            res="Not Prime Number"
            break
        i+=1
    print()
    print("-"*50)
    print("{} is {}".format(n,res))
    print("-"*50)

