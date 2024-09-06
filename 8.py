G = 6.67430e-11
mass1 = float(input("Enter the mass of the first object in Kg: "))
mass2 = float(input("Enter the mass of the second object in Kg: "))
distance = float(input("Enter the distance between the objects in meter: "))
force = G * mass1 * mass2 / distance**2
print(f"The gravitational force between the objects is ", round(force, 2), " N")
