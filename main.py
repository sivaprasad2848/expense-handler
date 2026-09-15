#expence manager
y=0
expences=[]
while(y==0):
    print("1->For Insert")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    opt=int(input("Enter the option"))
    if opt==1:
        title=input("Enter the Expence Title")
        amount=input("Enter the Expence Amount")
        dt=input("Enter the Expence Date")
        expences.append((title,amount,dt))
    if opt==2:
        #print(title+" "+amount+" "+dt)
        print(expences)
    if opt==3:
        i=int(input("Enter the index you want to delete"))
        del expences[i]
    if opt==4:
        i=int(input("Enter the index you want to update"))
        title=input("Enter the Expence Title")
        amount=input("Enter the Expence Amount")
        dt=input("Enter the Expence Date")
        expences[i]=(title,amount,dt)
    y=int(input("Do You Want to Continue? 0 for yes"))