#Program for to create the function for calculating the simple interest and total amount
def simple_interest():
    p=int(input("Enter the principal Amount:"))
    t=int(input("Enter the Time:"))
    r=int(input("Enter the Rate of Intrest"))
    si=(p*t*r)/100
    totalamu=si+p
    return p,t,r,si,totalamu
#function call
res=simple_interest()
   print("*"*50)
    print("Calculations of Simple Interest")
    print("*"*50)
    print("\tPrinciple Amount:{}".format(res[0]))
    print("\tTime:{}".format(res[1]))
    print("\tRate of Interest:{}".format(res[2]))
    print("\tSimple Interest:{}".format(res[3]))
    print("\tTotal Amount to Pay:{}".format(res[4]))
    print("*"*50)
  
