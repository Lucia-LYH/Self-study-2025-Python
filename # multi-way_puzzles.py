# multi-way_puzzles

x=6
if x<2:
    print ('less than 2')
elif x<20:
    print ('less than 20')
elif x<10: # the following line will be skipped cuz x=6 matches the x<20 condition
    print ('less than 10')
else:
    print ('greater than 20')