students_names=[]
count=int(input("how many studnets do you want to put here?"))
for i in range(count):

    give_here_names=input("enter names ").split()

    students_names+=give_here_names


print(students_names)

update=input("hey do you want to be update some thing ? then write here index. if no just type NO")

if update.upper()=="NO":
    print("no changes are made")
    exit()
else: 
    update=int(update)
    obj=input("/n with what ?")
    students_names.insert(update,obj)
print(students_names)
