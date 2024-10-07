#aadil rashid valid palindrome

# madam
# racecar

# M A D A M
# -       -
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) 

    while left < right:
        print(f"LEFT: {left} | RIGHT: {right}")
        if s[left] != s[right - 1]:
            return False
        else:
            left +=1
            right -=1
    
    return True

print(is_palindrome("madam"))