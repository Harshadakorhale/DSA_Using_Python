def reverse_string(s):
    stack =[]
    for char in s:
        stack.append(char)
    reverse_list =[]
    while stack:
        reverse_list.append(stack.pop())
    return "".join(reverse_list)
original_string="Hello World"
reverse_string = reverse_string(original_string)
print(f"Original String : {original_string}")

print(f"Reverse String : {reverse_string}")
