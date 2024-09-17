hostel_rent  = int(input("Pass your hotel rent here : "))
fooding_charge = int(input("Pass your fooding charge here :"))
pay_units = int(input("How many Electricity you did use in a month : "))
rate_per_unit = float(input("Pass your rate per Unit which you paid for electricity :"))

electricity_charge = pay_units*rate_per_unit

number_of_person = int(input("How many person are libal to pay for bills : "))

output = (hostel_rent+fooding_charge+electricity_charge)//number_of_person

print("Each Person will pay : ",output)