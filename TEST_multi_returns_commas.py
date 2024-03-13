def multi_function():
    return 3, "cat", ["frog", True, 88]

my_fct = multi_function()

my_int, my_str, my_lst = my_fct[0], my_fct[1], my_fct[2]

# my_int = multi_function()[0]
# my_str = multi_function()[1]
# my_lst = multi_function()[2]

print(f"My function returns an integer '{my_int}', a string '{my_str}' and a list '{my_lst}'")