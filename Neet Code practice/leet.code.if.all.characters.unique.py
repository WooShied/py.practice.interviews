#unique characters leet code

def unique(s: str) -> bool:
    seen = set()

    for char in s:
        if char in seen:
            return False
        
        seen.add(char)
        
    return True
    
print(unique("aaaaaaa"))