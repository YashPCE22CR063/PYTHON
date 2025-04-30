def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_value = gcd(num1, num2)
lcm_value = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd_value}")
print(f"LCM of {num1} and {num2} is: {lcm_value}")
