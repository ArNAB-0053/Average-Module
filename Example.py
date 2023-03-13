import AverageModule

numbers = int(input("\nEnter number of elements: "))
# print("\nEnter numbers: ") 
avg = AverageModule.Average(numbers)
print(f"\nThe average of {numbers} numbers is: ", avg.average())