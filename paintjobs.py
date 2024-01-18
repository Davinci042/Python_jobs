
#Declaring Global variables

ftpergallon = 112
laborperhr = 25
while True:
    try:
        ftreq = float(input("How much square feet of wall do you want to paint?: "))
        
    except ValueError:
        print("Invalid Input! Please enter a number")
        continue
    break

while True:
    try:
        paintprice = float(input("What is the cost of paint per gallon?: "))
    except ValueError:
            print("Invalid Input! Please enter a number")
            continue
    break

def main():
     gallonreq = ftreq // ftpergallon
     if (ftreq % ftpergallon) != 0:
         gallonreq +=1 
     else:
          pass
     paintcost = gallonreq * paintprice
     ftperhr = (ftpergallon * gallonreq * paintprice) / paintcost
     laborhrs = ftreq / ftperhr
     laborcost = laborhrs * laborperhr
     totalcost = laborcost + paintcost
     Laborhrs = "{:,.2f}".format(laborhrs)
     Laborcost = '${:,.2f}'.format(laborcost)
     Paintcost = '${:,.2f}'.format(paintcost)
     Totalcost = '${:,.2f}'.format(totalcost)

     print('The number of gallons of paint required is ' + str(gallonreq) +'gallons')
     print('The cost of paint required is ' + str(Paintcost))
     print('The hours of labour required to complete the job is : ' + str(Laborhrs) +'hrs')
     print('The cost of labour to complete the job is : '+ str(Laborcost))
     print('The total cost of the paint job is : ' + str(Totalcost))

main()