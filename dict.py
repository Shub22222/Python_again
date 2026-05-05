items = [
    {"name": "Laptop", "is_found": False},
    {"name": "Keys", "is_found": False},
    {"name": "Wallet", "is_found": False},
    {"name": "Watch", "is_found": False}
]

user_claim=input("enter you want..").capitalize()

foundit=False
#i here act as a dictionary
for i in items:
    if user_claim==i["name"]:
        i["is_found"]=True
        foundit=True
        break


if not foundit:
    print("sorry not found it")


print(items)
