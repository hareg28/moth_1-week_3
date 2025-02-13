# Sum numbers in a list
def sum_list(numbers):
    return sum(numbers)

#  even numbers between 1 and 20
def print_even_numbers():
    for num in range(1, 21):
        if num % 2 == 0:
            print(num)

#  largest number in a list
def find_largest_number(numbers):
    return max(numbers)


if __name__ == "__main__":
    
    list = [10, 20, 4, 45, 99]

    
    print("Sum of the list:", sum_list(list))

    
    print("Even numbers between 1 and 20:")
    print_even_numbers()

    print("Largest number in the list:", find_largest_number(list))