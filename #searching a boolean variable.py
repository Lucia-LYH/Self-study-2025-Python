#searching a boolean variable
found = False
for num in [0,2,3]:
    if num == 3:
        found = True
        print ('found', num)
        continue
    else:
        found = False
        print ('did not find')