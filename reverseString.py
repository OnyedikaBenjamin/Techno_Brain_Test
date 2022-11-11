# method 1

Text = "a string of the words in reverse order concatenated by a single space"[
    ::-1]


print(Text)

# Method 2


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "a string of the words in reverse order concatenated by a single space"

print("The original string is : ", end="")
print(s)

print("The reversed string is: ", end="")
print(reverse(s))
