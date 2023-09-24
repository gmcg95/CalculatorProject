class Calculator:

    def __init__(self, default_value=0):
        self.default_value = default_value

    def calculus(self):
        print(self.default_value)
        operation_input = input('>')
        while operation_input == 'x':
            print('Calculator closed')
            break
        while operation_input != 'x':
            try:
                try_operation_input = float(operation_input.split(operation_input[0])[1])

                if isinstance(try_operation_input, float):

                    if '+' in operation_input:
                        calculus_command = float(operation_input.split('+')[1])
                        self.default_value = self.default_value + calculus_command
                        print(self.default_value)
                    elif '-' in operation_input:
                        calculus_command = float(operation_input.split('-')[1])
                        self.default_value = self.default_value - calculus_command
                        print(self.default_value)
                    elif '*' in operation_input:
                        calculus_command = float(operation_input.split('*')[1])
                        self.default_value = self.default_value * calculus_command
                        print(self.default_value)
                    elif '/' in operation_input:
                        calculus_command = float(operation_input.split('/')[1])
                        if calculus_command == 0:
                            try:
                                zero_division = self.default_value / calculus_command
                            except ZeroDivisionError:
                                print('You are going to INFINITY, stay on your path!')
                                print(self.default_value)
                        else:
                            self.default_value = self.default_value / calculus_command
                            print(self.default_value)
                    elif '=' in operation_input:
                        calculus_command = float(operation_input.split('=')[1])
                        self.default_value = calculus_command
                        print(self.default_value)
                    else:
                        print('Invalid operation')
                        print(self.default_value)
            except ValueError:
                print('Invalid operation')
                print(self.default_value)
            operation_input = input('>')
