# Print a Range of Number and Also Total Sum of Those Numbers
starting_number = int(input("Enter your starting number: "))
ending_number = int(input("Enter your endding number: "))
total_sum = 0
for i in range(starting_number, ending_number+1):
    total_sum += i
    print(i)
print(f"Total sum is {total_sum}")