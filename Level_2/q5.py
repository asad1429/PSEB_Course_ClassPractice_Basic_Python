Temprature = int(input("Enter the temperature in Celsius: "))

if Temprature < 10:
    print("It's cold outside. wear jacket.")
elif Temprature >= 10 and Temprature < 25:
    print("It's a pleasant day.")
elif Temprature >= 26 and Temprature < 35:
    print("It's Warm outside.")
else:
    print("It's hot outside. Stay hydrated.")