#expence manager
from helper import *
from file_handling import *
y=0
k=read_data_from_expences()
set_expences(k)
while(y==0):
    opt=menu()
    if opt==1:
        insert_contact()
    if opt==2:
        display_contact()
    if opt==3:
        delete_contact()
    if opt==4:
        update_contact()
    y=int(input("Do You Want to Continue? 0 for yes"))
    if(y!=0):
        expence_list=get_expences()
        write_to_file(expence_list)