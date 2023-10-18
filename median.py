"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    
    except ValueError:
        print("Some input could not be converted to a number!")
    
    else:
        numbers.sort() #sorting the numbers first
        print(f'Sorted numbers: {numbers}')

        l = len(numbers) #length 
        if l%2 == 1:
            median = numbers[l//2]

        else:
            med1 = numbers[l//2]
            med2 = numbers[(l//2)-1]
            median = [(med1 + med2)/2]
        break
print(f'The median of the list of inputs you have given is: {median}')
