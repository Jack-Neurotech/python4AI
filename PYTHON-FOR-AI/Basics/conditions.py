temperature = 25

if temperature > 30:
    print("It's very hot")

elif temperature >25: 
    print("Hot")

else:
    print("good")


# Multiple conditions with and, or, not

age = 25

has_license = True

if age >= 18 and has_license:
    print("good")

if age < 18 and has_license:
    print("ok")

elif age < 16 and has_license:
    print("permit")




