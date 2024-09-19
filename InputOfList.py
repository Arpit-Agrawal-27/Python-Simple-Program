#Program for to accept the Number of list
lst=[]
print("Enter value and for stop Press any special symbol or press enter Two time")
print("-"*60)
while True:
    val=input()
    if not val.isalnum() and not val.__contains__(".") and not val.startswith("-") and not val.isspace():
        break
    else:
        lst.append(val)
print("List of value={}".format(lst))
