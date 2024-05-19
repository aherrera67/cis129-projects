def is_palindrome(a): 
    a = ''.join(char.lower() for char in a if char.isalnum())
    stack = []
    for char in a:
        stack.append(char)
    
    reversed_a = ''
    while stack:
        reversed_a += stack.pop()
    return a == reversed_a

print(is_palindrome("bienvenido")) #true
print(is_palindrome("goodbye")) #true
print(is_palindrome("asta la vista")) #true
print(is_palindrome("hello")) #false