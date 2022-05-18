# 1. Importing a data file containing the menu items and price list
import json

def readJsonFile():
    data=""
    try:
         with open('files/menu.json') as json_file:
           data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
    
# 2. Retrieving the json data, storing it in a variable, then printing out the data of each menu item and its price for users to view
data = readJsonFile()
menulist = data["menu"]
itemlist = data["item"]
for m in itemlist:
    print(m, itemlist[m], "RM",menulist[m])

# 3. Creating empty variables for total amount to be paid, type of item selected, quantity of item(s) selected, and calculated price
totalamount = 0;
itemno_list = []
quantityno_list = []
pricelist = []

# 4. Asking users to input what type of items and the quantity of items they wish to buy. If users enter 'No", the code will proceed to calculate the total price
while True:
    print("Enter No below if you do not wish to make a purchase, or if you have nothing else to buy")
    itemno = input("Which item do you want to buy (Please refer to the menu item numbers above and Enter 1, 2, 3, 4, or 5)? ")
    if itemno == "No":
        break
    quantity = int(input("How many do you want to buy? "))
    
# 5. Calculating the total amount of price that user needs to pay
#   Using itemno to determine the position of the items in the pre-created menulist List from step 2, and retrieving its corresponding price
#   Users might buy multiple quantities of the same item. After calculating the price for each item type bought, they are added together to calculate the final price to pay
    price = menulist[itemno] * quantity
    totalamount += price
    
# 6. Adding on user input values into the Lists that were created in step 3. These lists will be used below in step 8
    itemno_list.append(itemno)
    quantityno_list.append(quantity)
    pricelist.append(price)
    
# If user did not make a purchase, the program will exit    
if totalamount == 0:
    print("You did not make a purchase. Please come again next time.")
    exit();

# 7. Telling users the total amount to pay and asking the user how much they are paying
#    If user pays less than the totalamount, the loop will repetitively ask users to re-enter a valid amount to pay
print("Total amount you need to pay is RM", totalamount)
isPaidRight = False
while isPaidRight != True:
    totalpaid = int(input("Key in how much you will pay "))
    if int(totalpaid) >= totalamount:
        isPaidRight = True
    else:
        print("You did not pay enough, please try again")


# 8. Calculating amount of change to give back to users
returnmsg = ""
moneynotes = [100, 50, 10, 5, 1]
totalreturn = totalpaid - totalamount
ptotalreturn = totalreturn
for x in moneynotes:
    if totalreturn >= x:
        notequantity = int(totalreturn / x)
        totalreturn = totalreturn - notequantity * x
        returnmsg += str(notequantity) +" note(s) of RM"+str(x)+", "
if int(totalpaid) == totalamount:
    print("No change required")
else:
    print("Here is your change: "+returnmsg)

# 9. Creating a receipt of user's purchase
startindex = 1
print("****** RECEIPT *****")
for x in itemno_list:
    print(str(startindex)+". "+itemlist[itemno_list[startindex-1]]+" X "+str(quantityno_list[startindex-1])+"   RM"+str(pricelist[startindex-1]))
    startindex += 1
print("Total Amount : RM"+str(totalamount))
print("        Paid : RM"+str(totalpaid))
print("      Change : RM"+str(ptotalreturn))
print("****** Thank you ******")
