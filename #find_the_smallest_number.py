#find_the_smallest_number
smnsf = None
for num in [3,2,1,4,2]:
    if smnsf is None:
        smnsf = num
    elif num<smnsf:
        smnsf = num
print (smnsf)

