import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Your Phone Number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim_details = carrier.name_for_number(phone, "en")
register = geocoder.description_for_number(phone, "en")


print("Your Namber:", number)
print("Your Country code and National Number:", phone)
print("Your Location:", time)
print("Your Sime Name:", sim_details)
print("Your Country Name:", register)
