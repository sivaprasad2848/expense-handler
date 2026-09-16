def write_to_file(data):
    fp=open("expence_data","w")
    for item in data:
        #print(item[0]+" "+str(item[1])+" "+item[2])
        data=item[0]+" "+str(item[1])+" "+item[2]+"\n"
        fp.write(data)
    fp.close()
def read_data_from_expences():
    expence_data1=[]
    with open("expence_data","r") as fp:
        for line in fp:
            line_data=line.strip()
            lst1=line_data.split(" ")
            expence_data1.append((lst1[0],lst1[1],lst1[2]))
    return expence_data1

# expence=[('food',1200,'19/09/2026'),('travel',1500,'17/09/2026')]
# write_to_file(expence)
# k=read_data_from_expences()
# print(k)