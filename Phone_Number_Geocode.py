import phonenumbers 
from phonenumbers import carrier
from phonenumbers.util import prnt
from phonenumbers import geocoder

num = input("Enter phone number : ")
pNum = phonenumbers.parse(num)

print(geocoder.description_for_number(pNum, "en"))
print(carrier.name_for_number(pNum, "en"))
prnt(pNum)
