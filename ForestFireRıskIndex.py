import math
counter = 1
while 1:
    #input variable
    temperature = float(input("Temperature at 12:00, C: "))
    humidity = float(input("Relative humidity at 12:00, %: "))
    wind_speed = float(input("Wind Speed at 12:00:,km/h: "))
    daily_rain = float(input("Daily rain, mm: "))

    print (temperature,humidity,wind_speed,daily_rain)
    # starting initialization
    
    while counter == 1:
        print("Initialization")
        counter = 0
        #F0 = 1 #FFMC of the previous day
        F0 = 88
        rf = 0.00001
        #P0 = 1 #Duff Moisture Code of the previous day
        P0 = 30
        m = 1.0 #Water content in fine fuel after the drainage
        #D0 = 5 # DC of the previous day
        D0 = 210
        Ew = 0 #TEE (equilibrium water content) of fine fuel after moistening
        kd = 0
        
        
        
     if x <= 1:
        print("Fire Risk is Very Low")
    elif (x>1) & (x<=4):
        print("Fire Risk is Low")
    elif (x>4) & (x<=12):
        print("Fire Risk is Moderate")
    elif (x>12) & (x<=18):
        print("Fire Risk is High")
    elif (x>18) & (x<=29):
        print("Fire Risk is Very High")
        
