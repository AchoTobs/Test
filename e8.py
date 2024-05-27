reverse_string= lambda s: s if len(s) <= 1 else reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
print(reverse_string("python"))
print(reverse_string(""))
