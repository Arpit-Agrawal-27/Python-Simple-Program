while(True):
    name=input("Enter Ur Name:") 
    words=name.split() 
    res=False
    for word in words:
        if(not word.isalpha()):
            res=True
            break
    if(res):
        print("{} is invalid Name--try again:".format(name))
    else:
        print("{} is Valid Name:".format(name))
        break
