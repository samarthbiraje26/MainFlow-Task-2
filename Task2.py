import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def gcd(a, b):
    return math.gcd(a, b)

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def remove_duplicates(lst):
    return list(set(lst))

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0
    for char in s:
        if char.isalpha():  # Only consider alphabetic characters
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count

def main():
    while True:
        print("\nSelect an option:")
        print("1. Check Prime Number")
        print("2. Sum of Digits")
        print("3. Calculate LCM and GCD")
        print("4. Reverse List")
        print("5. Sort a List")
        print("6. Remove Duplicates from List")
        print("7. Find String Length")
        print("8. Count Vowels and Consonants")
        print("9. Exit")
        choice = int(input("Enter your choice (1-9): "))

        if choice == 1:
            n = int(input("Enter a number: "))
            print("Prime:", is_prime(n))

        elif choice == 2:
            n = int(input("Enter a number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == 3:
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            print("LCM:", lcm(a, b))
            print("GCD:", gcd(a, b))

        elif choice == 4:
            lst = list(map(int, input("Enter a list of integers: ").split()))
            print("Reversed list:", reverse_list(lst))

        elif choice == 5:
            lst = list(map(int, input("Enter a list of integers: ").split()))
            print("Sorted list:", bubble_sort(lst))

        elif choice == 6:
            lst = list(map(int, input("Enter a list of integers: ").split()))
            print("List without duplicates:", remove_duplicates(lst))

        elif choice == 7:
            s = input("Enter a string: ")
            print("Length of the string:", string_length(s))

        elif choice == 8:
            s = input("Enter a string: ")
            vowels, consonants = count_vowels_consonants(s)
            print("Vowels:", vowels)
            print("Consonants:", consonants)

        elif choice == 9:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()