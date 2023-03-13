import AverageModule

# DefaultStyle
numbers = int(input("\nEnter number of elements: "))
avg = AverageModule.Average(numbers)
print(f"\nThe average of {numbers} numbers is: ", avg.average())

# DefaultStyle False
print("\nEnter numbers: ") 
avg = AverageModule.Average(numbers)
print(f"\nThe average of {numbers} numbers is: ", avg.average(defaultStyle=False))