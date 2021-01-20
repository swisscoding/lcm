#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Get least common multiple | ----\n", fg("red")))

# class
class LCM:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    # output magic method
    def __repr__(self):
        lcm_val = stylize(self.lcm(self.value1, self.value2), fg("red"))
        return f"\nLeast common multiple of {self.value1} and {self.value2} is {lcm_val}.\n"

    # methods
    def lcm(self, val1, val2):
        gcd_val = self.gcd(val1, val2)
        return str(int(val1 / gcd_val * val2))

    def gcd(self, n1, n2):
        divisor = 2
        temp = 0
        while True:
            if num1 % divisor == 0 and num2 % divisor == 0:
                temp = divisor
                divisor += 1
            else:
                divisor += 1
            if divisor > num1 or divisor > num2:
                if temp != 0:
                    return temp
                else:
                    return 1

# main execution
if __name__ == "__main__":
    # user interaction
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(LCM(num1, num2))
