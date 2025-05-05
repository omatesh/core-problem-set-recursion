# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


# reverse
def reverse(text):
    if len(text) <= 0:
        return ""
    return text[len(text) - 1] + reverse(text[:len(text) - 1])


# bunny
def bunny(n):
    if n == 0:
        return 0
    return 2 + bunny(n - 1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif not parens[0] == '(' or not parens[len(parens)-1] == ')':
        return False
    return is_nested_parens(parens[1:-1])

