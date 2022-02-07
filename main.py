import random 
#Part A

weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("\n")
print("Cost per week:", cost_per_week) 

classes_per_week = 2
print("Classes per week:" , classes_per_week)

cost_per_class = ((cost_per_week/classes_per_week))
print("Cost per class:" ,cost_per_class)
print("\n")
print(cost_per_week , type(cost_per_week))

print(classes_per_week , type(classes_per_week))

print(cost_per_class, type(cost_per_class))

#Part B
objects = ['Dwight','Jim','Michael','Angela','Kevin']
print("\nCharacter from The Offcie : ", objects[0])
words = random.choice(objects)
print("\tRandom name from The Office : " , words)