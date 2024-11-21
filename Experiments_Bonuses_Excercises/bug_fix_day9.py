#BUG FIXING EXCERCISE: The progrom below intends to find out how many items have atleast one underscore ("_")
#character in them. However, there is an error with the code. Try to find and fix it.
#
#ids = ["XF345_89", "XER76849", "XA454_55"]
#
#x = 0
#
#for id in ids:
#    if '_' in id:
#print(x)
#FIXED#FIXED#FIXED#FIXED#FIXED#FIXED#FIXED

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
#    print(x)     THIS WOULD BE WRONG BECAUSE THE PRINT FUNCTION SHOULD BE AFTER THE ITERATION
#    so it doesnt print for every iteration

print(x)