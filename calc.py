print('Enter your first number')
first_number = float(input())

print('Enter your second number: ')
second_number = float(input())

print('Select your operator: ')
operator = input()

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*' or operator == 'x':
    print(first_number * second_number)
elif operator == '/':
    print(first_number / second_number)
else:
    print('Invalid operator')
