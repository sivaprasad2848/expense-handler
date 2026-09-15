#expence manager
y=0
expences=[]
while(y==0):
    print("1->For Insert")
    print("2->For Display")
    opt=int(input("Enter the option"))
    if opt==1:
        title=input("Enter the Expence Title")
        amount=input("Enter the Expence Amount")
        dt=input("Enter the Expence Date")
        expences.append((title,amount,dt))
    if opt==2:
        #print(title+" "+amount+" "+dt)
        print(expences)
    y=int(input("Do You Want to Continue? 0 for yes"))