#Program for to create the function for calculating the simple interest and total amount
def simple_interest():
    p=int(input("Enter the principal Amount:"))
    t=int(input("Enter the Time:"))
    r=int(input("Enter the Rate of Intrest"))
    if p<=0 or t<=0 or r<=0:
        return "Given Input Is Invalid"
    else:
        si=(p*t*r)/100
        totalamu=si+p
        return p,t,r,si,totalamu
#function call
res=simple_interest()
if type(res)==str:
    print(res)
else:
       print("*"*50)
        print("Calculations of Simple Interest")
        print("*"*50)
        print("\tPrinciple Amount:{}".format(res[0]))
        print("\tTime:{}".format(res[1]))
        print("\tRate of Interest:{}".format(res[2]))
        print("\tSimple Interest:{}".format(res[3]))
        print("\tTotal Amount to Pay:{}".format(res[4]))
        print("*"*50)
      
