import argparse

operations = {'add': lambda x, y: x + y,
              'div': lambda x, y: x / y,
              'mult': lambda x, y: x * y,
              'sub': lambda x, y: x - y
              }
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Basic calculator'
    )

    parser.add_argument('operation', type=str, choices=operations.keys())
    parser.add_argument('num1', type=float)
    parser.add_argument('num2', type=float)

    arguments = parser.parse_args()

    try:
        function = operations[arguments.operation]
        result = function(arguments.num1, arguments.num2)
        print(result)
    except ValueError as e:
        print(f'Error: {e}')
    except ZeroDivisionError:
        print('Error: zero division')
#python test.py sub 7 8



