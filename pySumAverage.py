#Sum/Average Program
#Your first and last name: Isaiah Bishop
#Your student ID: 1288086

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberlist = []
total = 0
for x in range (0,20):
    num = int(input ("Enter Number"))
    numberlist.append(num)

for x in range (0,20):
    total = total + numberlist[x]
    
print(total)
print(total/len(numberlist))
