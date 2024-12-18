import sys 
input_number = int(sys.argv[1])
print(f'user given number is (input_number)')
digits = [int(digits)for digits in sys.argv[1]]
print(f'sum of the digits of (input_number)is {sum(digits)}')