#Program for to create the function for calculating the simple interest and total amount
def simple_interest():
    p=int(input())
    t=int(input())
    r=int(input())
    si=(p*t*r)/100
    totalamu=si+p
    return p,t,r,si,totalamu
#function call
res=simple_interest()
print("-"*50)
print(res[0])
print(res[1])
print(res[2])
print(res[3])
print(res[4])

  
