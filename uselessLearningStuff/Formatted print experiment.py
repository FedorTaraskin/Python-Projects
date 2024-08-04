import dis

# Non-formatted print statement
def non_formatted_print():
    name = "Alice"
    age = 30
    print("My name is", name, "and I am", age, "years old.")

# Formatted print statement
def formatted_print():
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")

print("Bytecode for non-formatted print:")
dis.dis(non_formatted_print)

print("Bytecode for formatted print:")
dis.dis(formatted_print)
print("Turns out that non formatted strings are faster for an entire SINGLE instruction (that's nothing haha..)")