
Students_name=[]
# insert data
names=input("enter staudents name").split()
Students_name+=names
print(Students_name)

while True:

    changes=input("do you wants change data? YES/NO").upper()

    if changes=="YES":

            print("choose options")
            print("option 1 insert")
            print("option 2 update")
            print("option 3 deleate")
            print("option 4 show data")
            print("5. Exit Program")

            user_changes=int(input("enter option number. "))
            if user_changes==1:
                index=int(input("at which index?"))
                obj=input("what is name of students?")
                Students_name.insert(index,obj)
                print(Students_name)

            elif user_changes==2:
                old_Student_name_update=int(input("enter old student index number to update "))
                if old_Student_name_update>=len(Students_name):
                    print("this index number hight than expected one")
                    continue

                New_Updated_name=input("enter new updated name of student")
                Students_name[old_Student_name_update]=New_Updated_name

                print(Students_name)

            elif user_changes==3:
                remove_Student_name=input("Enter student name to remove")
                if remove_Student_name in Students_name:
                     
                    Students_name.remove(remove_Student_name)

                else:
                     print("Sorry the name of the studnet not exist")
                     continue
                
                print(Students_name)
                

            elif user_changes==4:
                print(Students_name)

            elif user_changes==5:
                print("Exiting program. Goodbye!")
                break


    else:
            print("no data changes.")
            exit()
        # print("option 4")

