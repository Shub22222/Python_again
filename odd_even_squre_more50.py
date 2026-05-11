num=[2, 5, 8, 10, 3, 12]
new=[]
for i in num:
    if i%2==0 :
        squre=i*i
        if squre>=50:
            new.append(squre)
print(new)
