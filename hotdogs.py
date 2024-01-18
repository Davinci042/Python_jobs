#Declare global variables
#This block of code will ensure user input errors is properly handle so our code doesn't crash
while True:
    try:
        serving = int(input("How many hotdog meal will each guest have?: "))
    except ValueError:
        print('Error! Enter a number')
        continue
    break

while True:
    try:          
        people = int(input("How many guests are invited?: "))
    except ValueError:
        print("Error! Enter a number")
        continue
    break

hotdog = 10
buns = 8

#this function will return the total number of servings
def total_hotdog(x: int, y: int):
    #The 2 arguments, x and y required are number of hotdog per invitee and total number of invitees
    servings_total = x * y
    total_hotdogs = servings_total // hotdog
    if (servings_total % hotdog) == 0:
        return(total_hotdogs)
    else:
        total_hotdogs +=1
        return(total_hotdogs)
        
   

def total_bun(x: int, y: int):
    servings_total = x * y
    total_buns = servings_total // buns
    if (servings_total % buns) == 0:
        return(total_buns)
    else:
        total_buns +=1
        return(total_buns)
  


def main():
    servings = serving * people
    total_hotdogs = total_hotdog(serving, people)
    total_buns = total_bun(serving, people)
    leftover_hotdog = (total_hotdogs * hotdog) - servings
    leftover_bun = (total_buns * buns) - servings

    print('The minimun number of packages of hotdog required is' +' ' + str(total_hotdogs))
    print('The minimun number of packages of hot dog buns required is' +' ' + str(total_buns)) 
    print('The number of hotdogs that will be left over is' + ' ' + str(leftover_hotdog))
    print('The number of hot dog buns that will be left over is' + ' ' + str(leftover_bun))

main()



    