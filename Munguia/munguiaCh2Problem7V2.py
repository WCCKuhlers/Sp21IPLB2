custName = input ("Please enter last name: ")

#numBathroom = float(input("Please enter the number of bathrooms: "))
#numOtherRooms = float(input("Please enter the number of other rooms: "))

SERVICE_CHG = 40
#print("Service Charge for your cleaning: $" + str(SERVICE_CHG))

#CHG_BATH = 15
#print("Charge for Bathroom cleaning: $" +str(CHG_BATH * numBathroom))
      
#CHG_ROOM = 10
#print("Charge for Room cleaning: $" + str(CHG_ROOM * numOtherRooms))

# Calculation for total cleaning charge

END_LINE = "Thank You!"
QUIT = "ZZZZ"
  
while custName != QUIT:
    if custName == QUIT:
        print(END_LINE)
    else:
        numBathroom = float(input("Please enter the number of bathrooms: "))
        CHG_BATH = 15

        numOtherRooms = float(input("Please enter the number of other rooms: "))
        CHG_ROOM = 10

        custTotalChg = SERVICE_CHG + (CHG_BATH * numBathroom) + (CHG_ROOM * numOtherRooms)
        print(custName + " total charge will be: $" +str(custTotalChg))
   
        custName = input ("Please enter last name: ")

        print(END_LINE)
