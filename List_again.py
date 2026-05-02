ViMEET= ["ID Card", "Laptop", "Bag"]

Found=["Bottle"]

ViMEET.extend(Found)

Search=input("what do you want ?").capitalize()

if Search in ViMEET:
    print("yes its available")
    ViMEET.remove(Search)
else:
    print("not avilable")

ViMEET.sort()
print(ViMEET)

print(ViMEET)
