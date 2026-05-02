user_claim=input("enter your lost one ").capitalize()
item_data["color"]="Silver"

# here goiing to cheack it 
# for user_claim in item_data["name"]:
if user_claim in item_data["name"]:
        item_data["is_claimed"]=True

elif user_claim in for_Phone["name"]:
       for_Phone["is_claimed"]=True
else:
        print("not matched")

print(item_data)
print(for_Phone)
