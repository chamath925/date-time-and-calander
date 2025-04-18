def hotel_cost(nights):
    return 2000 * nights

def plane_ride_cost(city):
    if "palali" == city:
        return 682
    elif 'katunayaka' == city:
        return 1672
    elif "matthala" == city:
        return 1976

def rental_car_cost(days):
    if days <= 7:
        return 875*days - 50
    elif days >= 3:
        return 850*days - 20
    else:
        return 825*days
    
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+ hotel_cost(days) + plane_ride_cost(city)+ spending_money

print("cost of car rental: ",rental_car_cost(5))
print("cost of plane ride: ",plane_ride_cost("palali"))
print("cost of hotelroom : ",hotel_cost(7))
print("total cost of trip",trip_cost("palali",7,5))