"""
Lines = explanations

1 = defining class
3 = class constuctor
6 = defining class method
7 = printing initial value (default_value)
8 = savind an input in a variable named operation_input
9 = doing a while loop for the case if you want to close the calculator
    the same outcome (for calculator to be closed) will be in any other stage where the input will be x,
    but without this message
11 = if the while loop is true (9), the code will not continue
12 = while loop for the other cases where the input is DIFFERENT from x
13 = raising a TRY-EXCEPT pair (line 13 and 48) for error handling in the case the input it is not float data type.
     I saved in a different variable the code to be tested for error,
     and in the line 48 I excepted the error and used print to output a message.
16 = for line 16 I used a condition with isinstance which flows the code only if the condition is true,
     in my case, if the input from user is float. (try variable, float)
18-44 = I used if conditionals for each possible operations in the problem (+,-,*,/,=)
        If the operation sign was found in the input, I used a variable that casts the input variable in float
        and splits the [0] (sign character)
        Then I saved in the class argument (with class instance; self.variable) the operation as:
        class argument = class argument operation float-casted variable
        Then I output the class argument (with the saved result after operation)
**32 =  because dividing anything by 0 = undetermined/infinity, I conditioned if the casted variable
        calculus_command == 0, to except the ZeroDivisionError and to output a message and the current result,
        aka the saved result for the class argument, aka print(self.default_value)
        Else, in any other case, the operation will be done as normal. ( x / y; where y != o )
45-47 = the last Else (for the first if conditional; if isinstance one) is used to output a message for invalid
        operation because of the cases which the input is invalid as invalid operation etc
48    = explained early, this was the except for the first try except pair and comes with the message:
        invalid operation for anything that is not float (as the try at line 13 explained)
51    = the same statement as the line 8 (operation_input = input('>')), but this statement belongs in the
        while loop.
        Without this statement, the while loop is infinite loop!

* the block of code is in the calculator file,
but the object of the class and the method calling are in the main file. (class file imported)
"""

"""
Project
Python calculator

It will be a default value(0) and then the current result depends on the operations made
Possible operations are:
+number - add from current value, this number
-număr - substracts from current value, this number
*număr - times from current value, this number
/număr - divide from current value, this number
=număr - set the value of the current value
x - exit the program/app

After each operation the program will output the current value and awaits for a new input.
"""


