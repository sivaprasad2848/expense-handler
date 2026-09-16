'''title=input("Enter a expence title")
amount=input("Enter a expence amount")
dt=input("Enter a expence date")
data=title+" "+amount+" "+dt+"\n"
fp=open("name_data","a")
fp.write(data)
fp.close()'''
fp=open("name_data","r")
data=fp.read()
fp.close()
print(data)
