# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[len(text)-1]:
        return False
  
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    return helper_fun(num1_str, num2_str)


def helper_fun(num1_str, num2_str):
    match = 0
    if not num1_str or not num2_str:
        return 0
    if num1_str[len(num1_str)-1] == num2_str[len(num2_str)-1]:
        match += 1
    param1 = num1_str[:len(num1_str)-1]
    param2 = num2_str[:len(num2_str)-1]
    return match + helper_fun(param1, param2)

