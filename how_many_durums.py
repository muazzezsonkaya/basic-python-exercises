try:
    a = float(input("How much does your expense cost in TL:"))
    b = input("How much is the price of dürüm?:")
    if b.strip() == "" :
        #user did not enter a dürüm price
        c = 250
        #avarage dürüm price is 250 tl in Antalya
    
    else:
        c = float(b)    

    durum = a / c
    print("It makes", durum, "dürüm my dear friend!")

except:
    print("Please enter a valid number. Letters or invalid characters cannot be processed my dear friend.")
