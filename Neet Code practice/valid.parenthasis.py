#valid parenthasis

# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# to get the top element out of a stack: my_stack.pop() would return the top element

def is_valid_parenthasis(s: str) -> bool:
    open_and_closed = {'(': ')', '{': '}', '[': ']'}
    
    stack = []
    for char in s:
        if char in open_and_closed:
            stack.append(char) 
        else:
            if not stack:
                return False
            my_top = stack.pop()
            if open_and_closed[my_top] != char: 
                return False

    return not stack

print(is_valid_parenthasis("([])"))