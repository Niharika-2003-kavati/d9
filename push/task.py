
firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")
city = input("Enter City: ")
age = int(input("Enter Age: "))
fav_animal = input("Enter Favourite Animal: ")
fav_number = input("Enter Favourite Number")
def get_initials(firstname, lastname):
    return firstname[0].upper() + lastname[0].upper()
def get_city_code(city):
    return city[:3].upper()
def check_voting(age):
    if age >= 18:
        return "Eligible for Voting"
    else:
        return "Not Eligible for Voting"
def combine_inputs(firstname, lastname, city, age, fav_animal, fav_number):
    return [firstname, lastname, city, age, fav_animal, fav_number]
print("Initials:", get_initials(firstname, lastname))
print("City Code:", get_city_code(city))
print("Voting Status:", check_voting(age))
print("Combined List:", combine_inputs(firstname, lastname, city, age, fav_animal, fav_number))