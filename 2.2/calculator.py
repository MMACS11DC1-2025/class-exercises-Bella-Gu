
Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

# calc

print("enter a math equation. use '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division")

print("Number 1")
a = float(input())
print()

print("Operator (+, -, *, /)")
operator = input().strip()
print()

print("Number 2")
b = float(input())
print()

if operator == "+":
    print(float(a+b))
elif operator == "-":
    print(float(a-b))
elif operator == "*":
    print(float(a*b))
elif operator == "/":
    print(float(a/b))
else:
    print("not valid")
