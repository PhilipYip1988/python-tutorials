import sys
numbers = sys.argv
if len(numbers) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f'{num1} + {num2} = {num1 + num2}')
    except ValueError:
        print('Invalid command line arguments')
else:
    print('Wrong number of command line arguments')
