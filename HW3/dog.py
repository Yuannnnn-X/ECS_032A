# dog.py
# Yuan Xie
#
# instructions on how to take a dog for a walk

# prompt the weather
Weather = input("Enter weather condition (rainy/sunny/snowy/cloudy):")
# if the weather is rainy
if Weather == "rainy":
    print("Instructions for the walk:")
    print("The dog should be taken for a short walk with an umbrella.")
# if the weather is sunny
elif Weather == "sunny":
    Temp = int(input("Enter temperature:"))
    if 80 < Temp <= 114:
        print("Instructions for the walk:")
        print("The dog should be taken for a walk in the shade and given water.")
    elif 45 < Temp <= 80:
        print("Instructions for the walk:")
        print("The dog can enjoy a regular walk.")
    elif -14 < Temp <= 45:
        print("Instructions for the walk:")
        print("Dress the dog warmly for a walk.")
    else:
        print("Instructions for the walk:")
        print("Invalid weather condition.")
# if the weather is snowy
elif Weather == "snowy":
    print("Instructions for the walk:")
    print("Take the dog for a short walk and ensure they stay warm.")
# if the weather is cloudy
elif Weather == "cloudy":
    print("Instructions for the walk:")
    print("Enjoy a regular walk with your dog.")
# else
else:
    print("Instructions for the walk:")
    print("Invalid weather condition.")
        
           
