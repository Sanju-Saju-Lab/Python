import math  # Import the math module for advanced mathematical operations
import re    # Import the re module to work with regular expressions (for handling functions)

class ScientificCalculator:
    def __init__(self):
        self.memory = 0  # Initialize memory to store values for later
        self.ans = 0     # Initialize a variable to store the last result

    def evaluate_expression(self, expression):
        expression = expression.replace("Ans", str(self.ans))  # Replace 'Ans' with the last result
        expression = expression.replace("π", str(math.pi)).replace("pi", str(math.pi))  # Replace π and pi with the actual pi value
        expression = self.handle_functions(expression)  # Handle any mathematical functions like sin, cos, etc.

        # Define a function to assign precedence to operators (order of operations)
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            if op == '^':
                return 3
            return 0

        # Define a function to apply an operator to operands (e.g., +, -, *, /, ^)
        def apply_operator(operands, operator):
            b = operands.pop()  # Get the second operand
            a = operands.pop()  # Get the first operand
            if operator == '+':
                operands.append(a + b)  # Add the operands
            elif operator == '-':
                operands.append(a - b)  # Subtract the operands
            elif operator == '*':
                operands.append(a * b)  # Multiply the operands
            elif operator == '/':
                if b != 0:
                    operands.append(a / b)  # Divide the operands, checking for division by zero
                else:
                    raise ZeroDivisionError("Math ERROR")  # Raise an error if division by zero occurs
            elif operator == '^':
                operands.append(a ** b)  # Exponentiation

        operators = []  # Stack to store operators (+, -, *, etc.)
        operands = []   # Stack to store numbers
        i = 0  # Initialize the index to 0

        while i < len(expression):
            char = expression[i]  # Get the current character

            if char == ' ':
                i += 1  # Skip spaces
                continue

            # If the character is a digit or decimal point, it's a number
            if char.isdigit() or char == '.':
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]  # Build the number by adding digits or decimal point
                    i += 1
                operands.append(float(num))  # Add the number to the operands stack
                continue

            # If the character is an opening parenthesis, push it to the operators stack
            if char == '(':
                operators.append(char)

            # If the character is a closing parenthesis, apply operators until we find the matching opening parenthesis
            elif char == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operands, operators.pop())  # Apply operators to the operands
                operators.pop()  # Pop the opening parenthesis from the stack

            else:
                # While there are operators in the stack and the current operator has lower or equal precedence,
                # apply the operators
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(char)):
                    apply_operator(operands, operators.pop())
                operators.append(char)  # Add the current operator to the stack

            i += 1  # Move to the next character

        # Apply remaining operators after processing the whole expression
        while operators:
            apply_operator(operands, operators.pop())

        self.ans = operands[0]  # The result is the only remaining operand
        return operands[0]  # Return the result

    def handle_functions(self, expression):
        # Use regular expressions to replace math functions (like sin, cos, etc.) with their results
        expression = re.sub(r'sin(\d+(\.\d*)?)', lambda m: str(math.sin(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'cos(\d+(\.\d*)?)', lambda m: str(math.cos(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'tan(\d+(\.\d*)?)', lambda m: str(math.tan(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'log(\d+(\.\d*)?)', lambda m: str(math.log10(float(m.group(1)))), expression)
        expression = re.sub(r'ln(\d+(\.\d*)?)', lambda m: str(math.log(float(m.group(1)))), expression)
        expression = re.sub(r'sqrt(\d+(\.\d*)?)', lambda m: str(math.sqrt(float(m.group(1)))), expression)
        return expression  # Return the modified expression with results for functions

    def store_in_memory(self, value):
        self.memory = value  # Store the value in memory
        return "Stored in memory"  # Return a message confirming the storage

    def recall_memory(self):
        return self.memory  # Return the value stored in memory

    def clear_memory(self):
        self.memory = 0  # Clear the memory
        return "Memory cleared"  # Return a message confirming the memory is cleared


def main():
    calc = ScientificCalculator()  # Create an instance of the ScientificCalculator class

    while True:
        # Print available options
        print("\nOptions:")
        print("1: Evaluate Expression")
        print("2: Store in Memory")
        print("3: Recall Memory")
        print("4: Clear Memory")
        print("5: Off")

        choice = input("\nEnter your choice: ").strip()  # Ask the user for a choice and remove extra spaces

        if choice == '5':
            print("CASIO")  # Print exit message
            break  # Exit the loop and end the program

        try:
            if choice == '1':
                expression = input("Enter the mathematical expression: ")  # Ask the user for an expression
                try:
                    result = calc.evaluate_expression(expression)  # Evaluate the expression
                    print("Answer:", result)  # Print the result
                except ZeroDivisionError:
                    print("Math ERROR")  # Handle division by zero error
                except ValueError as ve:
                    print("Error:", ve)  # Handle invalid input errors
            elif choice == '2':
                value = float(input("Enter the value to store in memory: "))  # Ask for a value to store in memory
                print(calc.store_in_memory(value))  # Store the value in memory and print confirmation
            elif choice == '3':
                print("Memory value:", calc.recall_memory())  # Print the value stored in memory
            elif choice == '4':
                print(calc.clear_memory())  # Clear the memory and print confirmation
            else:
                print("Invalid choice. Please try again.")  # Handle invalid menu choices
        except Exception as e:
            print("Error:", e)  # Catch and print any other errors that occur during input

if __name__ == "__main__":
    main()  # Call the main function to run the program
