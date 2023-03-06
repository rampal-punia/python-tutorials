# def info(func):
#     def wrapper(*args):
#         print(f"Function name is: {func.__name__}")
#         print(f'Function docstring: {func.__doc__}')
#         return func(*args)
#     return wrapper


# @info
# def double(number):
#     """
#     function to double a number

#     Args:
#         number (int): number

#     Returns:
#         int: Double of the number
#     """
#     return number * 2


# double(5)

##########################################

# def bold(func):
#     def wrapper(*args):
#         return "<b>" + func() + "</b>"
#     return wrapper


# def italics(func):
#     def wrapper(*args):
#         return "<i>" + func() + "</i>"
#     return wrapper


# @italics
# @bold
# def formate_text():
#     return "Python Rocks!"


# print(formate_text())
####################################################

# def info(arg1, arg2):
#     print(f'Decorator args1 = {str(arg1)}')
#     print(f'Decorator args2 = {str(arg2)}')

#     def the_real_decorator(function):
