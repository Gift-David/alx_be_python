# A script to give clothing advice based on the weather

weather = input("What's the weather like today (Sunny/Rainy/Cold):").lower()

if weather == "sunny":
    print("Wear a T-shirt and sun glasses")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, I don't have recommendations for this weather")