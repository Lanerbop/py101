# QUESTION 1
# 5 will be printed. num is initialized in the global scope
# and my_func access the global variable num and prints

# QUESTION 2
# 5 will be printed. my_func initialized a local variable
# named num, but that does not affect the global variable
# num.

# QUESTION 3
# 10 will be printed because num is specified as the global
# variable num. after my_func is invoked, num is reassigned
# to 10 and then printed.

# QUESTION 4
# "Hello World" will be printed because the inner function
# can access the variable outer_var. Inner is invoked
# and "Hello World" is printed.

# QUESTION 5
# There will be a NameError because num was initialized inside
# my_func and is a local variable. num has not been defined
# globally.

# QUESTION 6
# The code will print Inner 1: 25 and then Inner 2: 15.
# Inside inner_func1, x is a local variable assigned to
# 25. Inner_func2 access the nonlocal variable x, which
# is 15.