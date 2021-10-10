# Lab4_1.py

print("Comparing two numbers:")
x = float(input("  Enter 1st Float number: "))
y = float(input("  Enter 2nd Float number: "))
print(f"  The entered numbers are {x:.1f} and {y:.1f}")

if x == y:
    print(f"{x:.1f} equals {y:.1f}")
elif x > y:
    print(f"{x:.1f} is greater than {y:.1f}")
else :      # don't put any condition on the else part
            # This automatically means x < y since x is not == y, x is not > y
    print(f"{x:.1f} is less than {y:.1f}")

