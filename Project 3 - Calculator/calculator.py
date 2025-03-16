class Calculator:

    def __init__(self, nums):
        self.num1 = int(nums[0])
        self.num2 = int(nums[1])
        if len(nums) > 2:
            raise Exception("You can only perform operations on two numbers.")

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            return "Error : Division by zero!"
        return self.num1 / self.num2
    
def main():
    while True:
        try:
            expression = input("\nEnter Your Expression: ")

            if "exit" in expression.strip().lower():
                break

            # Split numbers by operators
            elif "+" in expression:
                elements = expression.split("+")
                cal = Calculator(elements)
                ans = cal.add()
                print("Answer:",ans,elements,cal.num1,cal.num2)

            elif "-" in expression:
                elements = expression.split("-")
                cal = Calculator(elements)
                ans = cal.subtract()
                print("Answer:",ans)

            elif "*" in expression:
                elements = expression.split("*")
                cal = Calculator(elements)
                ans = cal.multiply()
                print("Answer:",ans)

            elif "/" in expression:
                elements = expression.split("/")
                cal = Calculator(elements)
                ans = cal.divide()
                if cal.num2 == 0:
                    print(ans)   # Only prints the error
                else:
                    print("Answer:",ans)
            
            else:
                print("Invalid expression! Please enter a valid operation like --> 36+28.")

        except ValueError:
            print("Invalid Input!!")
            print("Try these examples --> 28+36, 29-8, 46*44, 81/9")
        except Exception as e:
            print(e)

print("\n====== Calculator ======\n")
print("Instructions:")
print("- You can perform any Arithmetic operation on two numbers directly.")
print("- Examples: 28+36, 29-8, etc.")
print("- Type 'Exit' to terminate the program.")

main()