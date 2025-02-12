def divide_and_check(a, b):
    # Step b: Divide a by b
    c = a / b

    # Step c: Determine if c is a float or an integer
    if c.is_integer():  # Check if c is an integer
        return f'{a} divided by {b} = {int(c)} and is an integer'
    else:  # If c is not an integer, it's a float
        return f'{a} divided by {b} = {c} and is a float'


# Step 4: Call the function with a=23 and b=7 and print the result
result = divide_and_check(23, 7)
print(result)
