age = 25

has_license = False

can_drive = age >= 16 and has_license 

print(can_drive)

# Worked Example

volts = -60
action_potental = -55
fire = False

can_fire = volts >= action_potental and fire 
print(can_fire)

#Truth tables
dead = True
volts = -60
fire = True 

can_fire = volts >= -55 and fire and not dead 

# adding on short cut assignment 

score = 10
score = score +5 
score += 5 
score *= 5


