num_fruits = int(input("Enter fave fruits"))
fruits = []

for i in range(num_fruits):
    fruit = input(f"Enter fruit {i+1}:")
    fruits.append(fruit)

print("Your favorite fruits are:")
for fruit in fruits:
    print(fruit)
