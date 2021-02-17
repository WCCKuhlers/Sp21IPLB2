custName = input("Please enteer last name: ")

numBathroom = float(input("Please enter the number of bathrooms: "))
numOtherRooms = float(input("Please enter the number of other rooms: "))
END_LINE = "Thank you!"

SERVICE_CHG = 40
print("Service Charge for your cleaning: $" + str(SERVICE_CHG))

CHG_BATH = 15
print("Charge for Bathrrom cleaning: $" +str(CHG_BATH * numBathroom))

CHG_ROOM = 10
print("Charge for Room cleaning: $" + str(CHG_ROOM * numOtherRooms))

#Calculation for total cleaning charge
custTotalChg = SERVICE_CHG + (CHG_BATH *numBathroom) + (CHG_ROOM * numOtherRooms)
print("Total charge is: $" +str(custTotalChg))
print(END_LINE)
