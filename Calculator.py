class Calculator:
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

    def adder(self):        # addition
        result = self.input1 + self.input2
        return result

    def subtractor(self):   # subtraction
        result = self.input1 - self.input2
        return result

    def multiplier(self):   # multiplication
        result = self.input1 * self.input2
        return result

    def divider(self):      # division
        result = self.input1 / self.input2
        return result

    def clear(self):        # reset to 0
        self.input1 = 0
        self.input2 = 0


# prompt user for input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
cal = Calculator(num1, num2)

# addition
addition_result = cal.adder()
print("The result of", cal.input1, "+", cal.input2, "is", addition_result)

# subtraction
subtraction_result = cal.subtractor()
print("The result of", cal.input1, "-", cal.input2, "is", subtraction_result)

# multiplication
multiplication_result = cal.multiplier()
print("The result of", cal.input1, "*", cal.input2, "is", multiplication_result)

# division
division_result = cal.divider()
print("The result of", cal.input1, "/", cal.input2, "is", division_result)

# reset to 0
cal.clear()
print("Input 1 is reset to", cal.input1)
print("Input 2 is reset to", cal.input2)
