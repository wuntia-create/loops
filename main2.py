#Number of rows
rows = 6
#outer loop for each row
for i in range(1, rows + 1):
    #Inner loop for printing stars in each row
    for j in range(i):
        print("*",end="")
    print() #Move to the next line after each row