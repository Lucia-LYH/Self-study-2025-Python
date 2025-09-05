#try_except

rawstr = input ('Enter a positive integer:')
try:
    ival = int (rawstr)
except:
    ival = -1
if ival>0:
    print(ival,'nice work')
else:
    print ('oops, try again')