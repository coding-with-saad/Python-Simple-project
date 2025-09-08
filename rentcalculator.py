rent=int(input("enter rent of the house  "))
food=int(input("enter the amount of food order  "))
electricity_spend=int(input("enter the toal of electricity spend "))
charger_per_unit=int(input("enter charge per unit in the area  "))


persons=int(input("enter the number of person living in the house "))

total_bill=electricity_spend*charger_per_unit

output=(food+rent+total_bill)//persons

print("Each person will pay =",output)