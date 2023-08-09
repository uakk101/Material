def meters_to_feet(meters):
    return meters * 3.281

def feet_to_meters(feet):
    return feet / 3.281

meters = float(input("Enter length in meters: "))
print("Length in feet:", meters_to_feet(meters))

feet = float(input("Enter length in feet: "))
print("Length in meters:", feet_to_meters(feet))
