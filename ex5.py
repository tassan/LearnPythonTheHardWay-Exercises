name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
to_cm = 2.54
to_kg = 2.2

print("Let's talk about %s." % name)
print("He's %d centimeters tall." % (height * to_cm))
print("He's %d kilograms heavy." % (weight / to_kg))
print("Actually that's not heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight))
