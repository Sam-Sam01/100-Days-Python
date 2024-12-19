
def prime_checker(number):
    if number <= 1:
        print("Number must be greater than ONE to be prime.")
        return  # Exit the function for invalid input   
    
    for i in range(2, (number//2)+1):
        if number % i == 0:
            print(f"{number} is NOT a prime number.")
            return  # Exit if any divisor is found
    
    print(f"{number} IS a prime number.")

n = int(input("Number: "))

prime_checker(number=n)