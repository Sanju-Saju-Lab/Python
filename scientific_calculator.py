import math  # Import the math module to use advanced mathematical functions like sin, cos, and sqrt
import re    # Import the re module to handle regular expressions for functions like sin, cos, etc.

class ScientificCalculator:
    def __init__(self):
        self.memory = 0  # Initialize memory to store values for later use
        self.ans = 0     # Initialize a variable to store the last result of a calculation

    def evaluate_expression(self, expression):
        # Replace 'Ans' with the last result and 'π' or 'pi' with the value of pi
        expression = expression.replace("Ans", str(self.ans))
        expression = expression.replace("π", str(math.pi)).replace("pi", str(math.pi))
        expression = self.handle_functions(expression)  # Call function to handle functions like sin, cos, etc.

        # Function to assign precedence (priority) to operators
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            if op == '^':
                return 3
            return 0

        # Function to apply an operator to operands
        def apply_operator(operands, operator):
            b = operands.pop()  # Pop the second operand from the stack
            a = operands.pop()  # Pop the first operand from the stack
            if operator == '+':
                operands.append(a + b)  # Perform addition
            elif operator == '-':
                operands.append(a - b)  # Perform subtraction
            elif operator == '*':
                operands.append(a * b)  # Perform multiplication
            elif operator == '/':
                if b != 0:
                    operands.append(a / b)  # Perform division if b is not zero
                else:
                    raise ZeroDivisionError("Math ERROR")  # Handle division by zero error
            elif operator == '^':
                operands.append(a ** b)  # Perform exponentiation

        operators = []  # Stack to store operators like +, -, *, etc.
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
                    num += expression[i]  # Add digits or decimal points to the number
                    i += 1
                operands.append(float(num))  # Push the number onto the operands stack
                continue

            # If the character is an opening parenthesis, push it onto the operator stack
            if char == '(':
                operators.append(char)

            # If the character is a closing parenthesis, apply operators until the opening parenthesis is found
            elif char == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operands, operators.pop())  # Apply operators
                operators.pop()  # Pop the opening parenthesis from the stack

            else:
                # Apply operators with higher or equal precedence
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(char)):
                    apply_operator(operands, operators.pop())
                operators.append(char)  # Push the current operator onto the stack

            i += 1  # Move to the next character

        # Apply any remaining operators after processing the entire expression
        while operators:
            apply_operator(operands, operators.pop())

        self.ans = operands[0]  # The result is the only remaining operand
        return operands[0]  # Return the result of the calculation

    def handle_functions(self, expression):
        # Replace functions like sin, cos, log, etc., with their calculated values
        expression = re.sub(r'sin(\d+(\.\d*)?)', lambda m: str(math.sin(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'cos(\d+(\.\d*)?)', lambda m: str(math.cos(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'tan(\d+(\.\d*)?)', lambda m: str(math.tan(math.radians(float(m.group(1))))), expression)
        expression = re.sub(r'log(\d+(\.\d*)?)', lambda m: str(math.log10(float(m.group(1)))), expression)
        expression = re.sub(r'ln(\d+(\.\d*)?)', lambda m: str(math.log(float(m.group(1)))), expression)
        expression = re.sub(r'sqrt(\d+(\.\d*)?)', lambda m: str(math.sqrt(float(m.group(1)))), expression)
        return expression  # Return the expression with all functions replaced by their results

    def store_in_memory(self, value):
        self.memory = value  # Store the value in memory
        return "Stored in memory"  # Return confirmation message

    def recall_memory(self):
        return self.memory  # Return the stored value from memory

    def clear_memory(self):
        self.memory = 0  # Clear the memory
        return "Memory cleared"  # Return confirmation message


def main():
    calc = ScientificCalculator()  # Create an instance of the ScientificCalculator class

    while True:
        # Display the menu options
        print("\nOptions:")
        print("1: Evaluate Expression")
        print("2: Store in Memory")
        print("3: Recall Memory")
        print("4: Clear Memory")
        print("5: Off")

        choice = input("\nEnter your choice: ").strip()  # Ask the user for a choice and remove extra spaces

        if choice == '5':
            print("CASIO")  # Display exit message and exit the loop
            break  # Exit the program

        try:
            if choice == '1':
                expression = input("Enter the mathematical expression: ")  # Ask for the mathematical expression
                try:
                    result = calc.evaluate_expression(expression)  # Calculate the result of the expression
                    print("Answer:", result)  # Display the result
                except ZeroDivisionError:
                    print("Math ERROR")  # Handle division by zero error
                except ValueError as ve:
                    print("Error:", ve)  # Handle any other errors during calculation
            elif choice == '2':
                value = float(input("Enter the value to store in memory: "))  # Ask for a value to store
                print(calc.store_in_memory(value))  # Store the value in memory and display confirmation
            elif choice == '3':
                print("Memory value:", calc.recall_memory())  # Display the value stored in memory
            elif choice == '4':
                print(calc.clear_memory())  # Clear the memory and display confirmation
            else:
                print("Invalid choice. Please try again.")  # Handle invalid menu choices
        except Exception as e:
            print("Error:", e)  # Handle any other errors

if __name__ == "__main__":
    main()  # Call the main function to run the program
