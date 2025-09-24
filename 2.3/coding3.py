"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
print("Would you like a burger for $5?")
response1 = input()

print("Would you like fries for $3?")
response2 = input()

cost = 0

if response1.lower() == 'yes':
    cost += 5
if response2.lower() == 'yes':
    cost += 3
total = cost * 1.14
print("Your total is $" + str(total))