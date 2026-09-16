expences=[]
def insert_contact():
    title=input("Enter the Expence Title")
    amount=input("Enter the Expence Amount")
    dt=input("Enter the Expence Date")
    expences.append((title,amount,dt))
def display_contact():
    #print(title+" "+amount+" "+dt)
    #print(expences)
    for item in expences:
        print(item)
def delete_contact():
    i=int(input("Enter the index you want to delete"))
    del expences[i]
def update_contact():
    i=int(input("Enter the index you want to update"))
    title=input("Enter the Expence Title")
    amount=input("Enter the Expence Amount")
    dt=input("Enter the Expence Date")
    expences[i]=(title,amount,dt)
def menu():
    print("1->For Insert")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    op=int(input("Enter the option"))
    return op
def get_expences():
    return expences
def set_expences(t):
    global expences
    expences=t