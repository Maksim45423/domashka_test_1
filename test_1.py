def palindrome(s):
    s_r = "".join(s.lower().split())
    print(s_r == s_r[::-1])
    return s

def back_string(text):
    return text[::-1]

def vowels(string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"    
    sum = 0    
    for char in string:
        if char in vowels:
            sum += 1    
    return sum

def remove_duplicates(text_1):
    result = []
    seen = set()
    for char in text_1:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return "".join(result)
print("dsdadsa")