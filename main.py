#expence manager
y=0
expences=[]
while(y==0):
    title=input("Enter the Expence Title")
    amount=input("Enter the Expence Amount")
    dt=input("Enter the Expence Date")
    expences.append((title,amount,dt))
    #print(title+" "+amount+" "+dt)
    print(expences)
    y=int(input("Do You Want to Continue? 0 for yes"))